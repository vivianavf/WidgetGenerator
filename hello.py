import json

class Node:
    def __init__(self, data, text, link):
        self.item = data
        self.nref = None
        self.pref = None
        self.text = text
        self.link = link

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    def print_LL(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def __iter__(self):
        return _IteradorListaEnlazada(self.start_node)

    def __str__(self):
       
        # defining a blank res variable
        res = ""
         
        # initializing ptr to head
        ptr = self.start_node
         
       # traversing and adding it to res
        while ptr:
            res += str(ptr.item) + ", "
            ptr = ptr.nref
 
       # removing trailing commas
        res = res.strip(", ")
         
        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

    def insert_at_end(self, data, text, link):
            if self.start_node is None:
                new_node = Node(data, text, link)
                self.start_node = new_node
                return
            n = self.start_node
            while n.nref is not None:
                n = n.nref
            new_node = Node(data, text, link)
            n.nref = new_node
            new_node.pref = n

    def insert_after_item(self, x, data, text, link):
            if self.start_node is None:
                print("List is empty")
                return
            else:
                n = self.start_node
                while n is not None:
                    if n.item == x:
                        break
                    n = n.nref
                if n is None:
                    print("item not in the list")
                else:
                    new_node = Node(data, text, link)
                    new_node.pref = n
                    new_node.nref = n.nref
                    if n.nref is not None:
                        n.nref.prev = new_node
                    n.nref = new_node

class _IteradorListaEnlazada(object):
    " Iterador para la clase ListaEnlazada "
    def __init__(self, prim):
        """ Constructor del iterador.
            prim es el primer elemento de la lista. """
        self.actual = prim

    def next(self):
        """ Devuelve uno a uno los elementos de la lista. """
        if self.actual == None:
            raise StopIteration("No hay más elementos en la lista")

        # Guarda el dato
        dato = self.actual.dato
        # Avanza en la lista
        self.actual = self.actual.prox
        # Devuelve el dato
        return dato

def crearLista():
    linkedList = DoublyLinkedList()
    "Leer Archivo Json"
    
    with open('datos.json', encoding='utf-8') as file:
        data = json.load(file)

    "Crear Lista Enlazada"
    for i in data:
        linkedList.insert_at_end(i, i, data[i])

    linkedList.print_LL()

    return linkedList

lista_enlazada = crearLista()

"Insertar despues de un item"
antes = input("Insertar después de: ->")
despues = input("Insertar item: ->")
print("https://ready2cut.blogspot.com/search/label/")
link = input("Insertar link: ->")
lista_enlazada.insert_after_item(antes, despues, despues, link)

nuevos_datos = {}

def guardarDatos(linked_list):
    if linked_list.start_node is None:
        print("List has no element")
        return
    else:
        n = linked_list.start_node
        while n is not None:
            nuevos_datos[n.item] = n.link
            n = n.nref

guardarDatos(lista_enlazada)

"Guardar Archivo Json"
with open('datos.json', 'w', encoding="utf-8") as file:
    json.dump(nuevos_datos, file, ensure_ascii=False, indent=4)

lista_enlazada_nueva = crearLista()


def textoHTML(linked_list):
    listaHTML = []
    contador = 0
    a = "<b:widget-setting name='text-" 
    b = "'>"
    c = "</b:widget-setting>"

    if linked_list.start_node is None:
        print("List has no element")
        return
    else:
        n = linked_list.start_node
        while n is not None:
            listaHTML.append(a + str(contador) + b + n.text + c)
            n = n.nref
            contador += 1
    return listaHTML

def linkHTML(linked_list):
    listaHTML = []
    contador = 0
    a = "<b:widget-setting name='link-"
    b = "'>"
    c = "</b:widget-setting>"

    if linked_list.start_node is None:
        print("List has no element")
        return
    else:
        n = linked_list.start_node
        while n is not None:
            listaHTML.append(a + str(contador) + b + n.link + c)
            n = n.nref
            contador += 1
    return listaHTML

textos = textoHTML(lista_enlazada_nueva)
links = linkHTML(lista_enlazada_nueva)

f = open ('widgets.txt','w')
f.write("<b:widget-settings>"+'\n')
f.write("<b:widget-setting name='sorting'>NONE</b:widget-setting>"+'\n')
for i in textos:
    f.write(i+'\n')    
for i in links:
    f.write(i+'\n')
f.write("</b:widget-settings>"+'\n')
f.close()