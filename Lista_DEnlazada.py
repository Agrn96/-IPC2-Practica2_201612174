class node:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.next = None
        self.prev = None

class lista_DEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,nombre, apellido, telefono):
        newNode = node(nombre,apellido,telefono)
        if(self.head == None):
            self.head = newNode
        elif(self.head.next == None):
            self.tail = newNode
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def out(self):
        if(self.head == None):
            print("List is empty")
        else:
            temp = self.head
            while(temp != None):
                print(temp.nombre)
                temp = temp.next
                
