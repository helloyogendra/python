from PyPDF2 import PdfReader, PdfWriter

file_name = r'C:\Users\YSingh\git\python\Tech_Notes\Bytebytego_System_Design_2023.pdf'
pages = (301, 344)

reader = PdfReader(file_name)
writer = PdfWriter()
page_range = range(pages[0], pages[1] + 1)

for page_num, page in enumerate(reader.pages, 1):
    if page_num in page_range:
        writer.add_page(page)

with open(f'{file_name}_page_{pages[0]}-{pages[1]}.pdf', 'wb') as out:
    writer.write(out)

print('Pdf writing done!!')