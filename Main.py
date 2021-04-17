from Crear_Graph import generate
from Lista_DEnlazada import lista_DEnlazada


lista = lista_DEnlazada()

def verify(lista, tele):
    temp = lista.head
    while(temp != None):
        if(temp.telefono == tele):
            return False
        temp = temp.next
    return True

def main(lista):
    try:
        x=0
        while(x!=4):
            print("\n1. Ingresar nuevo contacto\n2. Buscar contacto\n3. Visualizar agenda\n4. Salir\nIngrese la opcion que desea:", end=" ")
            x = int(input())
            if(x==1):
                
                print("\nIngrese nombre: ",end="")
                nombre = input()
                print("Ingrese apellido: ",end="")
                apellido = input()
                print("Ingrese numero de telefono: ", end="")
                telefono = int(input())
                while(telefono < 10000000 or telefono > 99999999):
                    print("Error con el numero de telefono (Insuficiente digitos)")
                    telefono = int(input())                       
                
                if(verify(lista,telefono)):
                    lista.add(nombre, apellido, telefono)
                    print("El contacto se ha agregado exitosamente")
                else:
                    print("El contacto ya existe")
            elif(x==2):
                print("\nIngrese el numero por buscar: ",end="")
                telefono = int(input())

                temp = lista.head
                while(temp != None):
                    if(temp.telefono == telefono):
                        print("Nombre: " + str(temp.nombre))
                        print("Apellido: " + str(temp.apellido))
                        print("Numero de telfono: " + str(temp.telefono))
                        break
                    temp = temp.next
                    if(temp == None):
                        print("El numero de telefono no existe, regresando al menu principal")
            elif(x==3):
                generate(lista)
            elif(x==4):
                raise SystemExit(0)
    except:
        print("ERROR: Error con el opcion del menu")

main(lista)