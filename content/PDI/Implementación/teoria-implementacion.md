# Implementacion de un Sistema Computacional

La implementación de un sistema computacional se refiere al proceso de llevar a cabo y poner en práctica un sistema de software para que cumpla con sus objetivos y funcione de manera efectiva. Es decir, refiere a lograr que el programa pueda finalmente ejecutarse como se espera.

Tras haber proyectado y diseñado el sistema, la tarea del desarrollador consiste en ponerlo en marcha ya sea alojándolo en un sitio web, o preparando el software para que pueda ser instalado en distintos dispositivos.

## Pruebas y entorno virtual

Para corroborar que el sistema sea funcional, es importante realizar pruebas para detectar fallas. Esto es un proceso esencial para garantizar la calidad, fiabilidad y rendimiento de un programa o aplicación.

Existen varios tipos:
- *Pruebas de unidad*: Se centran en probar componentes individuales del software (como módulos o funciones).
- *Pruebas de integración*: Verifican que los diferentes componentes del software se integren entre sí y funcionen como un sistema
- *Pruebas de sistema*: Evaluan el sistema en su totalidad.
- Etc

Para evitar que las pruebas arrojen resultados distintos de un dispositivo a otro se emplean los **entornos virtuales**. Estos son "entornos de software que permiten ejecutar sistemas informáticos de forma aislada dentro de un sistema". Esto asegura que, si se puede ejecutar un programa de dicha manera, se podrá ejecutar en prácticamente cualquier sistema compatible.

## Casos

- **Sitio/aplicación web**: Para que el proyecto esté al alcance de los usuarios, se debe encontrar alojado en un sitio web
- **Aplicación de escritorio**: Se debe poder instalar y ejecutar la aplicación, además, el instalador de la aplicación debe poder ser descargable via internet.
    Para poder lograr esto empleando flet deberemos de seguir los pasos que indica la <a href="https://flet.dev/docs/guides/python/packaging-desktop-app/">siguiente guía</a>:
    - *Obtener PyInstaller*: PyInstaller es un módulo que nos va a permitir convertir nuestros archivos ".py" 

