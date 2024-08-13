# MO PROJECT

Este proyecto es un ejemplo de un backend en django (monolito), el cual me permite crear clientes, dichos clientes tendran un score (capacidad de endeudamiento),
a partir de esa capacidad de endeudamiento, pueden crear prestamos (loans), cabe aclarar que esos prestamos estan limitados al score del cliente.

Por ultimo la tabla de pagos y detalles de pagos, me permite organizar los registros cuando el cliente genera un pago para disminución de la deuda, estos pagos no pueden superar el monto de la deuda o el (outstanding), además cuando el cliente realiza sus pagos, dicho campo disminuye el valor como un control en las deudas.

## Validaciones importantes:

- los clientes se peuden crear con un endpoint o por medio de un arhcivo plano (.csv).
- el status del prestamo se modificara dependiendo de los calculos del programa.
- existe un endpoint para ver el balance del cliente.
- los detalles del pago se crean automaticamente ua vez se consuma el endpoint de pagos, al igual que actualizan el status y el outstanding del prestamo.

## Recursos Adicionales

1. [**Link del proyecto en github vista kanban**](https://github.com/users/Livinarias/projects/4)

2. [**Link del proyecto en github vista board**](https://github.com/users/Livinarias/projects/4/views/2)

3. [**Link del front-page**](https://startbootstrap.com/theme/creative)

4. **Archivo importación para endpoints del proyecto en postman**

    Este archivo esta en la carpeta endpoints del proyecto

5. [**Archivo de ejemplo para cargar clientes**](archivo_plano/test_customers.csv)

6. **Archivo dockerfile para la creación de la iamgen y el .dockerignore para iniciar de cero la aplicación**


## Pasos para Dockerizar la aplicación

1. **Clonar el repositorio**
    - git clone -b main https://github.com/Livinarias/mo_project

### Pasos para Windows

2. [**Instalar Docker Desktop**](https://docs.docker.com/desktop/install/windows-install/)

3. **En la terminal ejecutar los siguientes comandos**
    - docker build -t django_app .
    - docker run -p 8000:8000 django_app

4. [**Abrir en el navegador el siguiente link cuando el termine de crearse la imagen**](http://localhost:8000/)

5. **En la terminal dentro del docker**
    - crear el super usuario

### Para Linux/Unix

2. **En la terminal ejecutar los siguientes comandos**
    - docker build -t django_app .
    - docker run -p 8000:8000 django_app

3. [**Abrir en el navegador el siguiente link cuando el termine de crearse la imagen**](http://localhost:8000/)

4. **En la terminal dentro del docker**
    - crear el super usuario