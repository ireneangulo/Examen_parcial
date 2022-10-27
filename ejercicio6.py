def crear_matriz(numero_filas, numero_columnas):
    matriz= [None]*numero_filas
    for i in range(numero_filas):
        matriz[i]= [None]*numero_columnas
    return matriz

def determinante_grado_3(m):
    A1= m[0][0]*m[1][1]*m[2][2]+m[1][0]*m[2][1]*m[0][2]+m[2][0]*m[1][2]*m[2][1]
    A2= m[0][2]*m[1][1]*m[2][0]+m[1][2]*m[2][1]*m[0][0]+m[0][1]*m[1][0]*m[2][2]
    return A1-A2
def dibujar_matriz(m):
    print("La matriz es: ")
    for i in range(len(m)): 
        print(m[i])
matriz= ([3,6,4], [7,1,8], [9,5,2])
dibujar_matriz(matriz)
print("El determinante segun el metodo de Sarrus es: ", determinante_grado_3(matriz))