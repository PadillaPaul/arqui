from datos.book import Book
from datos.book_repository import BookRepository
from negocio.book_service import BookService
from presentacion.book_controller import BookController

def display_menu():
    print("Bienvenido al sistema de gestión de biblioteca.")
    print("Por favor, seleccione una opción:")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Buscar libro por título")
    print("4. Salir")

def add_book(repository):
    title = input("Ingrese el título del libro: ")
    author = input("Ingrese el autor del libro: ")
    book = Book(title, author)
    repository.add_book(book)
    print("Libro agregado exitosamente.")

def remove_book(repository):
    title = input("Ingrese el título del libro que desea eliminar: ")
    books = repository.find_by_title(title)
    if books:
        for index, book in enumerate(books):
            print(f"{index + 1}. Título: {book.title}, Autor: {book.author}")
        choice = int(input("Seleccione el número del libro que desea eliminar: "))
        if 1 <= choice <= len(books):
            repository.remove_book(books[choice - 1])
            print("Libro eliminado exitosamente.")
        else:
            print("Selección inválida.")
    else:
        print("No se encontraron libros con ese título.")

def search_by_title(controller):
    title = input("Ingrese el título del libro que desea buscar: ")
    books = controller.search_by_title(title)
    if books:
        for index, book in enumerate(books):
            print(f"{index + 1}. Título: {book.title}, Autor: {book.author}")
    else:
        print("No se encontraron libros con ese título.")

if __name__ == "__main__":
    repository = BookRepository()
    service = BookService(repository)
    controller = BookController(service)

    while True:
        display_menu()
        option = input("Ingrese el número de la opción que desea: ")

        if option == "1":
            add_book(repository)
        elif option == "2":
            remove_book(repository)
        elif option == "3":
            search_by_title(controller)
        elif option == "4":
            print("¡Gracias por usar el sistema de gestión de biblioteca!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
