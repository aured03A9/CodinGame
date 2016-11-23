message = input()
bmessage = ''
cmessage = ''
n = ''

for c in message:
    bmessage += format(ord(c), '07b')
#   bmessage += '{0:07b}'.format(ord(c))

for b in bmessage:
    if b == '1' and b != n:
        cmessage += ' 0 '
    elif b == '0' and b != n:
        cmessage += ' 00 '
    n = b
    cmessage += '0'

print(cmessage.strip())
