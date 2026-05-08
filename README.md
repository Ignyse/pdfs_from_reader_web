# pdfs_from_reader_web

# Concept
Retrieve the textual context from urls and is able to combine them in to a clean pdf with certain settings chosen by the user (like font, fontsize, space line etc). Inspired from how the reader view works.

# Dependencies
Using trafilatura for text extraction https://trafilatura.readthedocs.io/en/latest/

requests needed for correct request to url, that is not flagged as bot and unzips content if zipped https://pypi.org/project/requests/

weasyprint needed for html to pdf conversion https://doc.courtbouillon.org/weasyprint/stable/

playwright (to not be deemed a bot on website) https://github.com/microsoft/playwright