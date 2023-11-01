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

### Creación de un entorno virtual

Dentro de la carpeta que contenga la carpeta de nuestro proyecto ejecutar el siguiente comando:

```cmd
python -m venv env
```

Esto nos creará la carpeta 'env', que contiene las siguientes subcarpetas:

<img src="img/carpetaEnv.png" alt="Carpeta env">

Podemos ejecutar nuestro entorno virtual ejecutando la sentencia

```cmd
env\Scripts\activate
```

Tras esto se nos indicará que estamos dentro de un entorno virtual. Lo interesante de todo esto es que si ejecutamos "pip list", para mostrar todas las librerias de python que tenemos instaladas nos aparecerán solamente las básicas, no contaremos ni con flet, ni con mysql, entre otros. 

Por otro lado, si intentamos ejecutar la aplicación nos dirá que no tenemos instaladas las librerias

Es solamente cuestión de volver a instalarlas, pero esta vez dentro del entorno virtual. Recuerden que para instalar dichos paquetes se usaban los siguientes comandos (ademas de los comandos para las librerias que hayan puesto ustedes en cada proyecto):

```cmd
pip install flet, flet-route, mysql, mysql-connector-python
```

Si tras instalar las librerias dentro del entorno y ejecutando la aplicación esta se muestra, nuestra aplicación debería funcionar en otros dispositivos tambien

## Casos

- **Sitio/aplicación web**: Para que el proyecto esté al alcance de los usuarios, se debe encontrar alojado en un sitio web. Se puede consultar la <a href="https://flet.dev/docs/guides/python/publishing-static-website">guia</a>
- **Aplicación de escritorio**: Se debe poder instalar y ejecutar la aplicación, además, el instalador de la aplicación debe poder ser descargable via internet.
    Para poder lograr esto empleando flet deberemos de seguir los pasos que indica la <a href="https://flet.dev/docs/guides/python/packaging-desktop-app/">guía</a>
- **Aplicación móvil**: Se debe obtener un archivo apk para poder instalar en el celular. Se puede consultar el siguiente <a href="https://www.youtube.com/watch?v=oglPs0lSh1Y&ab_channel=SriEdyNurcahyo">video</a>

