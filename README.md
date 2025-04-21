Universidad de Manizales
Ingenieria de Sistemas
Harold David Garces Casas
Jerónimo Montoya Osorio
Programacion I
Contexto de la problematica:

Gestión de Tareas o Recordatorios en una Aplicación de Productividad
Descripción del problema:
En muchas ocasiones, las personas tienen problemas para gestionar sus tareas diarias, ya sea por olvidos, desorganización o falta de una plataforma que centralice todo. Esto puede generar pérdida de productividad. Una posible solución sería desarrollar una aplicación de gestión de tareas, donde los usuarios puedan agregar, editar y eliminar recordatorios, así como marcar tareas como completadas.

Como implementamos lo visto en clase frente a esta problematica?

Se implementaron clases como Task, BaseTask y ListTask, con sus respectivos atributos y métodos, permitiendo la creación de objetos con estado y comportamiento propio. Se utilizaron constructores (__init__) para inicializar instancias, encapsulando los datos mediante atributos privados y proporcionando acceso a través de métodos públicos; Además, se aplicó herencia, al extender la clase BaseTask desde una interfaz abstracta ITask, fomentando la reutilización de código y la abstracción. También se empleó la agregación, ya que la clase ListTask mantiene una colección de objetos Task.

Por otro lado, sigue el patrón de diseño Modelo-Vista-Controlador (MVC), lo cual permite separar la lógica de negocio (modelo), la presentación de datos (vista) y la interacción con el usuario (controlador). Esta estructura mejora la organización del código, su mantenimiento y escalabilidad a largo plazo(segun lo requiera el cliente). La clase Vista(view) maneja exclusivamente la visualización e interacción con el usuario, Controlador(controller) coordina la comunicación entre la vista y los modelos, y las clases del modelo(model) gestionan la lógica y persistencia de las Task.