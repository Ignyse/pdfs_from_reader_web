# PDFs from Reader Web

## Concept

A lightweight tool that extracts clean readable content from web pages and compiles it into a well-formatted PDF.

It mimics browser “reader mode” by stripping away clutter (ads, navigation, scripts) and keeping only the core textual content. Multiple URLs can be combined into a single structured PDF with user-defined formatting options.

Use cases:
- Saving long-form articles for offline reading
- Combining multiple references into a single document
- Creating clean research packs from web sources

---

## Features

- Extract main readable text from any URL
- Combine multiple web pages into a single PDF
- Clean “reader mode” style output
- Custom PDF formatting:
  - Font family
  - Font size
  - Line spacing
  - Page layout

---

## How It Works

1. Fetch webpage content
2. Render page (when needed) to bypass bot protection
3. Extract main text content
4. Clean and structure extracted text
5. Convert structured HTML → PDF
6. [Optional] If users requests -> detects urls patterns and automatically fetch sequential pages, applying the same extraction pipeline

---

## Dependencies

### Content Extraction
- **trafilatura**  
  Extracts clean main-text content from web pages  
  https://trafilatura.readthedocs.io/en/latest/

### HTTP Requests
- **requests**  
  Handles HTTP fetching, headers, and compressed responses  
  https://pypi.org/project/requests/

### Anti-Bot Rendering
- **playwright**  
  Headless browser used to bypass bot detection and render dynamic pages  
  https://github.com/microsoft/playwright

### PDF Generation
- **weasyprint**  
  Converts structured HTML into high-quality PDFs  
  https://doc.courtbouillon.org/weasyprint/stable/


