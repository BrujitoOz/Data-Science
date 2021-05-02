import itertools as itt

def conjuncion(p, q):
    z = (p and q)
    return z

def disyuncion(p, q):
    z = (p or q)
    return z

def negacion(p):
    z = not p
    return z

def implicacion(p, q):
    if (p == False):
        z = True
    else:
        z = q
    return z

def bicondicional(p, q):
    z = conjuncion(implicacion(p, q),implicacion(q, p))
    return z

# Integracion


datos = list(itt.product([False, True], repeat=7))

i = 0
for (b11,b21,p11,p12,p21,p22,p31) in datos:
        r1 = negacion(p11)
        r2 = bicondicional(b11,disyuncion(p12,p21))
        r3 = bicondicional(b21, disyuncion(disyuncion(p11,p22),p31))
        r4 = negacion(b11)
        r5 = b21
        bc = r1 and r2 and r3 and r4 and r5
        i +=1 
        print(b11,b21,p11,p12,p21,p22,p31, "\t | ",r1,r2,r3,r4,r5, bc)
"""
for (p, q) in datos:
    r1 = negacion(p)
    r2 = conjuncion(p, q)
    r3 = disyuncion(p, q)
    r4 = implicacion(p, q)
    r5 = bicondicional(p, q)
    i = i + 1
    print(i, " ", p, " ", q, "|", r1, " ", r2, " ", r3, " ", r4, " ",r5)
"""