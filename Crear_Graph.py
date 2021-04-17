from graphviz import Digraph
import os
os.environ["PATH"]  += os.pathsep + 'D:/Program Files (x86)/Graphviz/bin/'

def generate(lista):

    dot = Digraph(name='Agenda', node_attr={'shape': 'record'}, edge_attr={'dir':'both'})
    dot #doctestL +ELLIPSIS
    cnt = 1
    temp = lista.head
    while(temp != None):
        name = 'A' + str(cnt)
        info = "Nombre: " + str(temp.nombre) + "\\nApellido: " + str(temp.apellido) + "\\nTelefono: " + str(temp.telefono)
        dot.node(name,info)
        if(cnt > 1):
            dot.edge('A'+str(cnt-1),name)
        temp = temp.next
        cnt+=1
    
    dot.render('Grafica.dot', view=True)