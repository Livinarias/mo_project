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

4. **Archivo importación para endpoints del proyecto**

    [descargar archivo](endpoints/MO Project.postman_collection.json)

