# arqui

## Requisitos

- Python 3.9 o superior

## Instalación

 Clona el repositorio:

bash
git clone https://github.com/PadillaPaul/arqui

ejecutar el main.py

listo

## Sistema de Gestión de Biblioteca 

Este proyecto es un sistema de gestión de biblioteca implementado en Python, utilizando una arquitectura de tres capas (Datos, Negocio, Presentación) y aplicando los principios SOLID y varios patrones de diseño (Bridge, Adapter, Strategy).


## Estructura del Proyecto

library_system/
├── data/
│   ├── __init__.py
│   └── book_repository.py
├── business/
│   ├── __init__.py
│   ├── book_service.py
│   └── search_strategy.py
├── presentation/
│   ├── __init__.py
│   └── book_controller.py
└── main.py


## Principios SOLID:

S:Single Responsibility Principle: Cada clase tiene una única responsabilidad.

O:Open/Closed Principle: Las clases están abiertas para extensión pero cerradas para modificación.

L:Liskov Substitution Principle: Las clases derivadas deben ser sustituibles por sus clases base.

I: Interface Segregation Principle (ISP) – Se crean interfaces específicas para cada funcionalidad.

D: Dependency Inversion Principle (DIP) – Las clases de alto nivel no dependen de clases de bajo nivel, sino de abstracciones.


## Patrones de Diseño:

### Bridge Pattern: 

Este patrón se utiliza en la relación entre las clases BookRepository y BookService. El BookRepository actúa como una interfaz para acceder a los datos de los libros, mientras que BookService es responsable de la lógica de negocio relacionada con los libros. La separación de estas dos responsabilidades permite que cada una pueda cambiar independientemente de la otra.


### Adapter Pattern: 

Este patrón se utiliza en la relación entre las clases Book y BookAdapter. En este caso, BookAdapter actúa como un adaptador para permitir que el BookController trabaje con objetos Book y diccionarios de información de libros. El adaptador encapsula la lógica para convertir entre los dos formatos de datos diferentes.


### Strategy Pattern: 

Este patrón se utiliza en las clases TitleSearchStrategy y AuthorSearchStrategy dentro del archivo search_strategy.py. Estas clases implementan la interfaz común SearchStrategy y proporcionan diferentes estrategias para buscar libros por título y autor. La estrategia se puede cambiar dinámicamente en el BookService según los requisitos de búsqueda del usuario.


## Arquitectura en 3 capas:

Capa de acceso a datos: datos
Capa de negocio: negocio
Capa de presentación: presentacion

