from retrieve_urls import retrieve_urls
from extract_content import extract_content
from formattext import generate_pdf
from cleantext import clean
import re

# Main template for usage of all functions

# retrieve list of url based on an initial one and how many extra pages, urllink is a personalized url
list_url = retrieve_urls("urllink",15)

# code to extract reader content, cleaned for correct characters, and combine into one pdf
combined = ""
for url in list_url:
    combined += clean(extract_content(url))
    combined += '\n'

# the 2nd parameter is the method chosen to generate pdf, it specficies the html format
generate_pdf(combined,2)