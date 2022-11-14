a  = [0,1,2,10,99]
b = bytearray(a)
for x in b:
    print(x)
    

b[0]  = 88
for x in b:
    print(x)
