import random

#Funcion para validar que los numeros no se repitan
def Sinrepetir(num, contra):
    unico=True
    for i in range(len(contra)): 
        if num == contra[i]:
            unico= False
            break
    return unico


password=[]
c=''
num=0 

#for donde se llena el arreglo password con  numeros aleatorios entre 33 y 125
for g in range(0,15,1):
    num=(random.randint(33,125))
    if Sinrepetir(num,password):
        password.append(num)

print( password)

#cambiamos de numeros a caracteres segun la tabla ASCII
for i in password:
    c= c + chr(i)

print("Su Password es: " + c)
    