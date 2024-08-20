
import fitz as pymudf
from PIL import Image
import io

# Open the PDF
pdf_document = "./test.pdf"
doc = pymudf.open(pdf_document)

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text("text")
    print(f"--- Page {page_num + 1} ---")
    print(text)

    for i in range(len(doc)):
        page = doc.load_page(i)
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(f"image_page_{i+1}_img_{img_index+1}.png")
            print(f"Extracted image {img_index+1} on page {i+1}")



# import os

# print(os.getcwd())
