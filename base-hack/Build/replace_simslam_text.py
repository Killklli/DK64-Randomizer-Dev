'Adjust simian slam text for cosmetic 3rd melon fix.'
from typing import BinaryIO
pointer_table_address=1055824
pointer_table_index=12
text_index=39
def replaceSimSlam(fh):'Write new text.';B='big';A=fh;print('Replacing Simian Slam Text');A.seek(pointer_table_address+4*pointer_table_index);C=int.from_bytes(A.read(4),B);D=pointer_table_address+C;A.seek(D+4*text_index);E=int.from_bytes(A.read(4),B)+pointer_table_address;A.seek(E+798);F='3RD MELON\x00';A.write(F.encode('ascii'))