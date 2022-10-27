lista= [18, 50, 210, 80, 145, 333, 70, 30]
#Apartado 1
for i in lista:
    if i %10==0 & i <200:
        print(i)
    else: 
        print("No cumple las condiciones")
#Apartado 2
for i in lista:
    if i > 200:
        print("Stop")
    else: 
        print(i)
        
    
#Apartado 3
lista.sort()
print(lista)
#Apartado 4
if 145 in lista:
    print(145)
else:
    print(-1)