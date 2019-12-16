import sys

shift = int(sys.argv[2])
s = sys.argv[1].upper()
c = [chr(((ord(i) - 65 + shift) % 26) + 65) if i.isalpha() else i for i in s]
print(''.join(c))
