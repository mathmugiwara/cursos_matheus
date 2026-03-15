from docx import Document

doc = Document('curso_python_modulo01.docx')

with open('docx_content.txt', 'w', encoding='utf-8') as f:
    for para in doc.paragraphs:
        if para.text.strip():
            style = para.style.name if para.style else "Normal"
            f.write(f"[{style}] {para.text}\n")

print("Done - docx_content.txt written")
