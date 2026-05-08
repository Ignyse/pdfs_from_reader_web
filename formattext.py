from weasyprint import HTML, CSS
from html import escape

def plaintext_to_html(text: str, method: int) -> str:
    from html import escape

    lines = text.splitlines()
    if method ==1:
        return tight_paragraph(lines)
    elif method ==2:
        return flexible_paragraph(lines)
    
# def flexible_paragraph(lines:str) -> str:
#     html_parts = []
#     paragraph = []
#     for line in lines:
#         stripped = line.strip()
#         if (stripped.isupper() and len(stripped) < 80) or (stripped.startswith('Chapter') and len(stripped) < 80):
#             html_parts.append(f"<h1>{escape(stripped.title())}</h1>")

#         elif stripped == '...':
#             html_parts.append(f"<hr class='divider'>")
#         else:
#             html_parts.append(f"<p>{escape(stripped)}</p>")
#     return "\n".join(html_parts)

def flexible_paragraph(lines:str) -> str:
    html_parts = []
    paragraph = []
    for line in lines:
        stripped = line.strip()

        # save the previous line as one pragraph if it encounters a quote

        if stripped.startswith('"') or stripped.startswith('“') or stripped.startswith("'") or stripped.startswith("Comments") :
            joined = ' '.join(paragraph)
            html_parts.append(f"<p>{escape(joined)}</p>")
            paragraph = []

        if stripped.startswith('Comments'):
            continue
        if stripped == '...':
            html_parts.append(f"<hr class='divider'>")
            continue
        if (stripped.isupper() and len(stripped) < 80) or (stripped.startswith('Chapter') and len(stripped) < 80):
            html_parts.append(f"<h1>{escape(stripped.title())}</h1>")
            continue
        paragraph.append(stripped)
        
    if paragraph:
        joined = " ".join(paragraph)
        html_parts.append(f"<p>{escape(joined)}</p>")

    return "\n".join(html_parts)

def tight_paragraph(lines :str) -> str:
    html_parts = []
    paragraph = []
    for line in lines:
        stripped = line.strip()
        print(stripped)
        # Empty line => end paragraph
        if not stripped:
            if paragraph:
                joined = " ".join(paragraph)
                html_parts.append(f"<p>{escape(joined)}</p>")
                paragraph = []
            continue

        if stripped == '...':
            if paragraph:
                joined = " ".join(paragraph)
                html_parts.append(f"<p>{escape(joined)}</p>")
                paragraph = []
            html_parts.append(f"<hr class='divider'>")
        #  heading heuristic, either whole chapter title is uppercase, or has explicitly chapter included
        if (stripped.isupper() and len(stripped) < 80) or (stripped.startswith('Chapter') and len(stripped) < 80):
            if paragraph:
                joined = " ".join(paragraph)
                html_parts.append(f"<p>{escape(joined)}</p>")
                paragraph = []

            html_parts.append(f"<h1>{escape(stripped.title())}</h1>")
        else:
            paragraph.append(stripped)

    if paragraph:
        joined = " ".join(paragraph)
        html_parts.append(f"<p>{escape(joined)}</p>")

    return "\n".join(html_parts)


def generate_pdf(text: str, method: int)->str:
    html = f"""
        <html>
        <head>
        <meta charset="utf-8">
        </head>
        <body>
        <article>
        {plaintext_to_html(text, method)}
        </article>
        </body>
        </html>
        """

    HTML(string=html).write_pdf(
    "output.pdf",
    stylesheets=["style.css"]
)