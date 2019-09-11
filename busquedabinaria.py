import random
import math
import matplotlib.pyplot as plt

print("Este programa encuentra un número de un vector")
print("Por medio del Método de Divide y vencerás")
print

def binaria (vec, izq, der, llave, c, cont):
    c[0] += 1
    c[cont] += 1
    
    if izq > der:
        c[0] += 1
        c[cont] += 1
        return None
    
    c[0] += 4
    c[cont] += 4
    mit = (der+izq)//2
    
    c[0] += 2
    c[cont] += 2
    
    if vec[mit] == llave:
        c[0] += 1
        c[cont] += 1
        return mit
    elif vec[mit] > llave:
        return binaria(vec, izq, mit-1, llave, c, cont)
    else:
        return binaria(vec, mit+1, der, llave, c, cont)
        
    c[0] += 2
    c[cont] += 2
    
def burbuja (vec, i):
    j=0
    while j < i-1:
        k=j+1
        while k < i:
            if vec[j] > vec[k]:
                t = vec[j]
                vec[j] = vec[k]
                vec[k] = t
            k=k+1
        j=j+1
    return vec
    
i=10
cont = 0
x = range(10)
y = range(10)
lg = range(100)
c = list(range(11))

for j in range(11):
    c[j] = 0
    
while i <= 101:
    vec = range(i)
    x[cont] = i
    
    for j in range(i):
        vec[j] = random.randint(0,300)
    
    burbuja(vec, i)
    print("Vector de "+str(i)+" números:")
    print(vec)
    print
    
    pos = random.randint(0,i-1)
    temp = vec[pos]
    
    cont += 1

    posicion = binaria(vec, 0, i, temp, c, cont)
    
    print
    print("La posición del número "+str(temp)+" es: "+str(posicion))
    print
    
    i += 10
    y[cont-1] = c[cont]
    
print(x)
print(y)    

for j in range(100):
    lg[j] = math.log((j+1))

for j in range(10):
    y[j]*=0.1

plt.plot(lg, 'o-')
plt.plot(x, y,'o')
plt.ylim(0,10)