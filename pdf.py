# pip install PyPDF2

''''
example from a youtube
from PYPDF2 import PdfFileWriter ,PdfFileReader
writer = PdfFileWriter()
file = 'test_file.pdf'
reader = PdffileReader(file)
for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))
writer.encrypt('Password')
with open(f'test_file.pdf','wb') as file:
    writer.write(file)
print('PDF encrypted')
'''


from pypdf import PdfReader, PdfWriter

reader = PdfReader("test_file.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("Password")

with open("test_file_encrypted.pdf", "wb") as f:
    writer.write(f)

print("PDF encrypted successfully!")
