n1 = int(input('total no dinheiro'))
n2 = int(input('total saida'))

s1 = n1+n2

n3 = int(input('saldo anterior'))

s2 = s1-n3

n4 = int(input('total credito'))
n5 = int(input('total debito'))

s3 = n4+n5
s4 = s2+s3
s5 = n1-n3

print('dinheiro', s2)
print('credito', n4)
print('debito', n5)
print('saida', n2)
print('saldo', s5)
print('saldo anterior', n3)
print('saldo atual', n1)
print('total', s4)


