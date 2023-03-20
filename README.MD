# Inteligent Terminal Assistant

## TODO:

- [ ] Implementar el sistema de Keywords en el programa.
- [ ] Implementar el sistema de Addons en el programa.
- [ ] Capacidad de ejecutar los comandos que nos devuelve CODEX.

## ¿Qué es?

Es un proyecto de código abierto, que busca crear un asistente de voz para la terminal, con el fin de facilitar la interacción con el sistema operativo, y con el usuario.

## ¿Cómo funciona?

Utilizando OpenAI Codex podemos transformar lenguaje humano en comandos de terminal, y viceversa.
Esto quiere decir, que a parte de conseguir realizar una orden (algunas muy complejas), también puede interpretar la salida de estas ordenes y responder a preguntas concretas.

## Ingeniería del prompt.

Cuando generamos texto usando un LLM (Large Language Model) usamos un inicio que se conoce como **PROMPT**.
Este prompt es el que le dice al modelo que tipo de texto queremos generar, y por lo tanto, es muy importante que sea lo más descriptivo posible.

También nos da la flexibilidad de poder cambiar dicho prompt en runtime.

### Partes del Prompt.

El prompt se compone de 3 partes:
- **Contexto**: El contexto del texto que vamos a generar. Explicandole al modelo cual es la intención que buscas.
- **Ejemplos**: Para facilitar la generación de texto, podemos darle ejemplos de lo que queremos que genere, en este caso peticiones convertidas a comandos.
- **Pregunta**: El principio de lo que queremos que genere.

En este caso, nuestro programa es capaz de mutar el contexto y los ejemplos para conseguir algunos efectos interesantes:

- Un sistema de addons, con el que podemos agregar diferentes comandos en forma de archivos py.
- Ejemplos más específicos a la pregunta elegida, para poder obtener una falsa sensación de aprendizaje o memoria.

### Sistema de Addons.

El sistema de addons, es un sistema que permite agregar comandos a nuestro asistente, de forma muy sencilla.
Para ello, solo tenemos que crear un archivo py, y añadirlo a la carpeta addons, junto a un texto con el mismo nombre que el archivo, que contenga la descripción del comando.
Esto será añadido al **contexto** en el prompt, haciendo que la inteligencia artificial pueda aprender a usar dicho comando.

### Limitaciones del sistema de Addons.

En teoría, cualquier archivo py que tenga unas entradas y unas salidas bien definidas puede ser usado como addon.
Sin embargo, hay algunas limitaciones que debemos tener en cuenta:

- El archivo debe tener un nombre que no contenga espacios.
- El archivo debe tener un nombre que no contenga caracteres especiales.
- El archivo debe tener un nombre explicativo de lo que hace, así será más fácil que el modelo entienda su función.

### Ejemplos de Addons.

- **google**: Busca en google la pregunta que le hagamos.

### Ejemplos más específicos (La teoría de las Keywords).

Si preguntamos sobre un tema en concreto, nos gustaría que nuestro asistente fuera capaz de recordar la información que hemos hablado previamente.
Para eso, podemos usar el sistema de **Keywords**.

Extraeremos las palabras claves generadas en cualquier interaccion, y las usamos para clasificarlas en el momento de guardarlas.
Antes de generar el texto, el programa buscará en la base de datos de ejemplos, si hay alguno que contenga las palabras claves, y si es así, lo añadirá al prompt. De esta forma, conseguimos que el asistente recuerde lo que hemos hablado previamente.

Por limitaciones de las peticiones, solo se añadiran a la lista de ejemplos inicial, un máximo de 5 interacciones con las palabras claves.
En caso de no haber palabras clave disponibles, se añadirán las 5 ultimas interacciones.


