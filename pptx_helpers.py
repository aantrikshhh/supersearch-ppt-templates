"""Shared helpers for manipulating PPTX slides via python-pptx + lxml."""

import copy
from lxml import etree

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def replace_paragraph_text(para, new_text):
    runs = para.findall(f"{A}r")
    if not runs:
        return

    first_run = runs[0]
    for r in runs[1:]:
        para.remove(r)
    for br in para.findall(f"{A}br"):
        para.remove(br)

    lines = new_text.split("\n")
    t = first_run.find(f"{A}t")
    if t is None:
        t = etree.SubElement(first_run, f"{A}t")
    t.text = lines[0]

    for line in lines[1:]:
        br = etree.SubElement(para, f"{A}br")
        rPr_src = first_run.find(f"{A}rPr")
        if rPr_src is not None:
            br_rPr = copy.deepcopy(rPr_src)
            br_rPr.tag = f"{A}rPr"
            br.append(br_rPr)
        new_r = copy.deepcopy(first_run)
        new_t = new_r.find(f"{A}t")
        new_t.text = line
        para.append(new_r)


def set_shape_text(shape, new_text):
    tf = shape.text_frame
    txBody = tf._txBody
    paras = txBody.findall(f"{A}p")
    if not paras:
        return
    first = paras[0]
    for p in paras[1:]:
        txBody.remove(p)

    blocks = new_text.split("\n\n") if "\n\n" in new_text else [new_text]
    replace_paragraph_text(first, blocks[0])

    for block in blocks[1:]:
        new_p = copy.deepcopy(first)
        replace_paragraph_text(new_p, block)
        txBody.append(new_p)


def find_shape_by_text(slide, substr):
    for shape in slide.shapes:
        if shape.has_text_frame and substr in shape.text_frame.text:
            return shape
    return None


def replace_in_shape(shape, replacements):
    """Paragraph-level substring replace. Collapses runs when a match spans
    multiple runs (handles the template's split-run XML patterns).
    Supports multiple replacements per paragraph."""
    if not shape.has_text_frame:
        return
    txBody = shape.text_frame._txBody
    for para in txBody.findall(f"{A}p"):
        full = "".join(
            (t.text or "") for t in para.iter(f"{A}t")
        )
        collapsed = False
        for old, new in replacements:
            if old in full:
                full = full.replace(old, new)
                collapsed = True
        if collapsed:
            runs = para.findall(f"{A}r")
            if not runs:
                continue
            first_run = runs[0]
            t = first_run.find(f"{A}t")
            if t is None:
                continue
            t.text = full
            for r in runs[1:]:
                para.remove(r)


def replace_bullet_column(shape, items):
    txBody = shape.text_frame._txBody
    paras = txBody.findall(f"{A}p")
    if not paras:
        return

    ref_para = paras[0]
    ref_pPr = ref_para.find(f"{A}pPr")
    ref_runs = ref_para.findall(f"{A}r")
    if len(ref_runs) < 2 or ref_pPr is None:
        return
    bold_run_tpl = copy.deepcopy(ref_runs[0])
    plain_run_tpl = copy.deepcopy(ref_runs[1])

    for p in paras:
        txBody.remove(p)

    for name, desc in items:
        new_p = etree.SubElement(txBody, f"{A}p")
        new_p.append(copy.deepcopy(ref_pPr))

        br = copy.deepcopy(bold_run_tpl)
        br.find(f"{A}t").text = name
        new_p.append(br)

        pr = copy.deepcopy(plain_run_tpl)
        t = pr.find(f"{A}t")
        t.text = desc
        t.set(
            "{http://www.w3.org/XML/1998/namespace}space", "preserve"
        )
        new_p.append(pr)


def deep_copy_row_template(style_tbl_xml, values):
    row = copy.deepcopy(style_tbl_xml)
    tcs = row.findall(f"{A}tc")
    for tc, val in zip(tcs, values):
        txBody = tc.find(f"{A}txBody")
        paras = txBody.findall(f"{A}p")
        for p in paras[1:]:
            txBody.remove(p)
        para = paras[0]
        replace_paragraph_text(para, val)
    return row
