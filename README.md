# PruebaTecnica

**GENERALIDADES**
- Las versiones que se usan en este proyecto son las de Python 3.8 y Django 3.0.7

Instrucciones:
    Configuracion de espacio de trabajo:
    *   Instalar python 3.8.2
    **  Actualizar pip a la version 20.1.1
            
            **pip install --upgrade pip**

    *** Instalacion de las dependencias:
            Ubicate con la terminal en le directorio crud_report/ (cd crud_report o dir crud_report) y
            ejecuta el siguiente comando:

                pip install -r requirements.txt

            Se instalaran todos los requerimientos necesarios para este proyecto.

**Problema 1 : ¿Cuántos Domingos?**

    La siguiente información es provista, pero la puede completar con otras fuentes:
    - El primero de enero de 1900 fue lunes.
    - Los meses de abril, junio, septiembre y noviembre tienen 30 días; los meses de enero, marzo, mayo,
    julio, agosto, octubre y diciembre tienen 31 días; y el mes de febrero tiene 28 días menos en los
    bisiestos cuando tiene 29 días.
    - Los años bisiestos ocurren cada 4 años
    - Si es inicio de siglo (año divisible por 100), no hay bisiesto a menos de que dicho año también sea
    divisible por 400. En dado caso, sí hay bisiesto.
    
    ¿Durante el siglo 20 (1 de enero de 1901 hasta 31 de diciembre de 2000), cuántos meses han empezado un
    domingo?

    **ANALISIS:**
        Para calcular el numero de meses que comienzan por un dia en especifico, es necesario lo siguiente:
        - Generador de fechas:
            Se necesita una funcion que sea capaz de generar las fechas que se necesitan.
        - Buscador de fechas:
            Este paso consite en realizar un arreglo que sea capaz de buscar la informacion deseada, es desir
            que compare las fechas generadas con la fecha que se desea.
        - Contador:
            Si los datos de busqueda coinciden con los datos generados entonces va contando en una variable
            la cantidad de datos positivos que se han encontrado.
        - Respuesta:
            Luego de que haya recorrido lainformacion, entonces el programa debera arrojar el resultado a la
            pregunta ¿Cuantos meses comienzan el dia deseado desde la fecha de inicio que queramos hasta la
            fecha final deseada?

    **DESARROLLO:**
        **Generador de fechas:**
            La libreria _datetime_ de python contiene una funcion **(rrule)** que es capaz de generar una
            lista iterable de fechas, de acuerdo con los parametros que le solicitemos, le introducimos el
            dato inicial, el dato final, y el modo como queremos que haga iteraciones (años, meses, dias),
            para nuestro caso se quiere que las iteraciones ocurran mes a mes, empezando por el dia que
            describamos en la fecha de inicio, es decir que si queremos encontrar el dia 2 de cada mes
            entonces lo declaramos implicitamente en la fecha de inicio.
        **Buscador:**
            En un bucle _for_ se iteran las fechas dadas por funcion rrule. Esta fecha se guardan en una
            variable y se le extrae el dia de la semana en ingles (Sunday, Monday, etc) para ser comparadas
            con el dia deseado, que proporciona el cliente.
        **Contador**:
            Mediante un comparador _if_ contamos los aciertos que tenga nuestra busqueda, este conteo lo
            vamos a ir ubicando en una variable que corresponde al numero de dias acertados que vamos
            encontrado. De esta forma, al culminar nuestras iteraciones, tendremos un valor total de aciertos
            para nuestra busqueda.
    
    **RESPUESTA:**
        La respuesta se va a enviar por medio de un web service, llamado por una peticion GET. La peticion se
        hara mediante una URI con el siguiente contenido:

            **Raiz:**
                Al ingrasar a la raiz vamos a encontrar un json que contiene con los datos de la solucion
                especifica a este problema _Encontrar cuantos meses comienzan por domingo desde el 1 de enero
                de 1901 hasta el 31 de diciembre de 2000,_ asi entonces esta raiz no cambia:
                                            
                                            http://127.0.0.1:8000/domingos/

            **Peticion:**
                El cliente puede solicitar el calculo a cualquier fecha que desee, incluyendo el valor _"?"_
                despues de la _Raiz_ y separando cada variable con un _&_, siguiendo los siguientes
                parametros:

                - format (**?format=json**):
                    Es el formato en el que quiere visualizar la respuesta, ya sea en un formato de API (en
                    minusculas), donde se visualiza en el formato standar de DRF o en formato JSON (En
                    minusculas), como se muestra en el ejemplo de abajo.

                - initial_date (**&initial_date=YYYY-MM-DD**):
                    Valor correspondiente a la fecha de inicio en formato YYYY-MM-DD.

                - final_date (**&final_date=YYYY-MM-DD**):
                    Valor correspondiente a la fecha de final en formato YYYY-MM-DD.

                - wday (**&wday=Monday**):
                    En ingles. Dia de la semana que involucra el numero de dia en el mes que queremos buscar
                    y que seria nuestro dato de conteo, en caso de que no se proporcione un dia especifico
                    este tomara _Sunday_ (Domingo), como valor por defecto.

                La peticion quedaria de la siguiente forma:

        http://127.0.0.1:8000/domingos/?format=json&initial_date=1901-01-01&final_date=2000-12-31&wday=Monday


**Problema 2: Derivar Contraseña (Ethical Hacking)**

    Un método de seguridad comúnmente utilizado por los bancos es preguntar tres caracteres aleatorios de una
    contraseña. Por ejemplo, si la contraseña es 531278, el banco puede preguntar por el 2do, 3er, y 5to,
    carácter; esperando que el usuario responda con la secuencia 3-1-7.
    
    El archivo keylog.txt contiene 50 secuencias correctas para una contraseña específica. Dado que cada una
    de las secuencias está en orden de primer carácter a último carácter, ¿Cuál es la contraseña más corta
    para la cual todas las secuencias son correctas?

    **ANALISIS:**
        Para determinar la manera de generar una constraseña a partir de los datos se tuvo en cuenta lo
        siguiente:
        1 La posicion de los digitos o caracteres en las constraseñas generan gerarquia.
        2 La gerarquia la genera el numero de sucesores que tiene un digito o caracter.
        3 El primer digito o caracter de la contraseña tiene mayor gerarquia debido a que lo suceden todos
        los otros digitos o caracteres
        4 El ultimo digito o caracter obtiene la menor gerarquia.
        5 Ningun digito o caracter tiene la misma gerarquia asi sean iguales.
        6 En caso de que sean iguales se tendra que tomar otras valoraciones para establecer la gerarquia de
        ese digito o caracter.
        7 Un digito o caracter _x_ no puede ocupar la posicion de un numero o caracter _y_.

    **DESARROLLO:**
        Para responder la pregunta del enunciado se desarrolla el analisis de lasiguiente forma:
            - Como la clave es numerica, se descarta que tenga caracteres en su composicion.
            - Se determinan cuantos digitos hay en total, creando una tupla con los digitos sin que se
            repitan.
            - Para determinar la gerarquia de un digito se hace una busqueda de los digitos que lo suceden,
            es decir se toma un digito _x_ y se busca entre las ternas que digitos se encuentran a su derecha
            y se guardan en otro arreglo.
            - De este ultimo arreglo se sacan los digitos repetidos, dejando una tupla con solo los digitos
            de interes.
            - Se hace un conteo del total de digitos que suceden a cada digito para establecer la gerarquia.
            - Para optener la contraseña se organizan los digitos de menor gerarquia a mayor gerarquia
            iniciando por la derecha.

    **RESPUESTA:**
        a respuesta se va a enviar por medio de un web service, llamado por una peticion GET. La peticion se
        hara mediante una URI con el siguiente contenido:

            **Raiz:**
                Al ingrasar a la raiz vamos a encontrar un json que contiene con los datos de la solucion
                especifica a este problema _Encontrar cuantos meses comienzan por domingo desde el 1 de enero
                de 1901 hasta el 31 de diciembre de 2000,_ asi entonces esta raiz no cambia:
                                              
                                            http://127.0.0.1:8000/keylog/

            **- Peticion:**
                El cliente puede solicitar el calculo de la contraseña con una data diferente alejercicio,
                incluyendo el valor _"?"_ despues de la _Raiz_ y separando cada variable con un _&_,
                siguiendo los siguientes parametros:

                - format (**?format=json**):
                    Es el formato en el que quiere visualizar la respuesta, ya sea en un formato de API (en
                    minusculas), donde se visualiza en el formato standar de DRF o en formato JSON (En
                    minusculas), como se muestra en el ejemplo de abajo. 

                - data (**&data=data**):
                    Por medio de esta variable se envian los datos con los que se quiere calcular otra
                    contraseña. Los datos deben ser enteros separados por comas (,) y sin espacios, de
                    nunguna forma deben estar entre comillas.

                La peticion quedaria de la siguiente forma:
                
        http://127.0.0.1:8000/keylog/?format=json&data=736,168,769,319,760,719,290,762,160,389,690,380,680,318,731,620,368,729,790,180,710,629,890,718,289,720,689,129,162,728,362,716,316
