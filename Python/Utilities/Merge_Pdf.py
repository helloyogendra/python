# G:\My Drive\Documents\JobLetters\Sakesh

import os
from PyPDF2 import PdfMerger

x = [a for a in os.listdir("G:\\My Drive\\Documents\\JobLetters\\Sakesh") if a.endswith(".pdf") and a.startswith("S")]

merger = PdfMerger()

for pdf in sorted(x):
    merger.append(open("G:\\My Drive\\Documents\\JobLetters\\Sakesh\\" + pdf, 'rb'))

with open("G:\\My Drive\\Documents\\JobLetters\\Sakesh\\Signed.pdf", "wb") as fout:
    merger.write(fout)

print("Pdf files merged")