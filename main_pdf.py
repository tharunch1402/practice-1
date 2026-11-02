from pypdf import PdfReader
reader = PdfReader("data-1/daily_diet_plan_nutrients.pdf")
text = ""
for page in reader.pages:
 text += page.extract_text() or ""
print("Pages:", len(reader.pages))
print(text[:1000])
