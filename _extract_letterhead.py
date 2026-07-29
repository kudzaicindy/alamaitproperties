import fitz
import os

pdf = r"c:\Users\HP\OneDrive\Desktop\alamait profile\Alamait Private Ltd -Letterhead (1) (2).pdf"
out = r"c:\Users\HP\OneDrive\Desktop\alamait profile\_pdf_extract"
os.makedirs(out, exist_ok=True)
doc = fitz.open(pdf)
page = doc[0]
for i, img in enumerate(page.get_images(full=True)):
    xref = img[0]
    base = doc.extract_image(xref)
    ext = base["ext"]
    path = os.path.join(out, f"img_{i}_{xref}.{ext}")
    with open(path, "wb") as f:
        f.write(base["image"])
    print(path, base["width"], base["height"])
# fast color sample: 1x scale, top 10% rows, step 8
pix = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
w, h = pix.width, pix.height
band = int(h * 0.1)
from collections import Counter

ctr = Counter()
for y in range(0, band, 2):
    row = y * w * pix.n
    for x in range(0, w, 8):
        i = row + x * pix.n
        r, g, b = pix.samples[i], pix.samples[i + 1], pix.samples[i + 2]
        if (r, g, b) != (255, 255, 255):
            ctr[(r // 5 * 5, g // 5 * 5, b // 5 * 5)] += 1
print("top_colors", ctr.most_common(20))
