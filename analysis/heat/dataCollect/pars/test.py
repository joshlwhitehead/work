import re


josh = '324()34'

new = re.sub(r'[^0-9]','',josh)
print(new)