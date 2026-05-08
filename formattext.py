from weasyprint import HTML, CSS
from html import escape

def plaintext_to_html(text: str) -> str:
    from html import escape

    lines = text.splitlines()

    html_parts = []
    paragraph = []

    for line in lines:
        stripped = line.strip()

        # Empty line => end paragraph
        if not stripped:
            if paragraph:
                joined = " ".join(paragraph)
                html_parts.append(f"<p>{escape(joined)}</p>")
                paragraph = []
            continue

        if stripped.equals('...'):
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


def generate_pdf(text: str)->str:
    html = f"""
        <html>
        <head>
        <meta charset="utf-8">
        </head>
        <body>
        <article>
        {plaintext_to_html(text)}
        </article>
        </body>
        </html>
        """

    HTML(string=html).write_pdf(
    "output.pdf",
    stylesheets=["style.css"]
)