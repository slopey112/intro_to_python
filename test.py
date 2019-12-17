import sys

print(''.join([chr(((ord(i) - 65 + int(sys.argv[2])) % 26) + 65) if i.isalpha() else i for i in sys.argv[1].upper()]))
