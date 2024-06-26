GENERO = ["ficcion", "No ficcion", "Ciencia"]


def registrar_libro(libro):
   libro = input("ingrese Titulo del libro: ").lower
   autor = input("Ingrese nombre del autor: ").lower
   genero = input("Ingrese el genero del libro (Ficcion/No Ficcion/Ciencia):").lower
   while genero not in GENERO:
       print("Ingrese un genero valido:")
       genero = input("Ingrese el genero del libro (Ficcion/No Ficcion/Ciencia): ").lower
   precio = int(input("Ingrese el precio del libro:"))
   
   
def listar_libros(libro):
    print("Lista de todos los libros")
    for libros in libro:
        print(libros)
        
        
def registrar_venta(libro):
    titulo = input("ingrese titulo: ")
    cantidad = int(input("ingrese la cantidad:"))
    preciototal = cantidad
    print(titulo, cantidad, preciototal)




