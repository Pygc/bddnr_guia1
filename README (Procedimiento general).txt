--------------------------DESCARGA VISUAL STUDIO CODE Y PYTHON VERSIÓN 2.7.18---------------------------------------------------------

1) Al tener descargado e instalado Visual Studio Code, 
procedí a instalar python en la versión 2.7.18, desde su página oficial.

2) Luego ingresé al cmd desde la dirección "C:\Python27\Scripts" e instalé lo siguiente:
- pip install colorama
- pip install socks
- pip install requests
- pip install modules
- pip install bs4
- pip install virtualenv (para crear el entorno virtual)

------------------------------------------USO DEL PROGRAMA--------------------------------------------------------------------------------

3) Luego, para crear el "Entorno Virtual" cree una carpeta llamada "Entorno" en el escritorio del pc, 
para luego abrirla en el Visual Studio code e ingresar en la terminal: 

virtualenv -p python2.7.18 venv-python3

En el cual se crea mi entorno virtual, donde la carpeta se llama: "venv-python3", y
presenta unas subs-carpetas y archivos llamados: Include, Lib, libs, Scripts, .gitignore,
pyvenv.cfg

*(en "Scripts" voy a tener los comandos para activar y desactivar mi entorno virtual)

- Para activar mi entorno virtual voy a ingresar en la terminal lo siguiente:

.\venv-python3\Scripts\activate

* 4) En mi caso particular, me dio error y no se me activo, entonces para solucionarlo, 
ingresé a la paleta de comandos en la configuración de Visual Studio Code, y ahí ingresé a: 

"Terminal: Select Default Profile" para luego ingresar: 

"Command Prompt C:\WINDOWS\System32\cmd.exe"

Por consiguiente, volver a ingresar a la paleta de comandos e ingresar: "Python: Select Interpreter" para luego ingresar: 

"Python 2.7.18 ('venv-python3':venv) .\venv-python3\Scripts\python.exe" 

Ahí procedo a cerrar la terminal que estaba abierta, y vuelvo a abrir otra terminal, la cual al abrirse, 
ya mostrará la dirección del entorno virtual activado, es decir:

(venv-python3) C:\Users\patty\Desktop\cosas_ubb\9no_semestre\Bdd_No_Relacional-Electivo\Unidad 1\guia1\entorno>

(Después del paso 4, ya se puede activar sin ningún problema el entorno virtual desde la terminal, simplemente escribiendo:

".\venv-python3\Scripts\activate" )

5) En el cual procedo a ejecutar "pip list" en la terminal, 
para ver los paquetes que tengo instalados dentro del entorno virtual al momento de crearlo. 
Luego comencé a instalar otros paquetes dentro del entorno los cuales son:

- pip install flask
- pip install Django

6) Luego procedo a crear la carpeta: "src" en el entorno virtual, 
con tal de crear dentro el archivo: "cmongodb.py" donde programaré (más adelante) el CRUD y consulta, 
generando la conexión de python con la base de datos que haré en mongodb. 

Archivo el cual para ejecutarlo en la terminal debo escribir: 

"python .\src\cmongodb.py"

7) Para luego desactivar mi entorno virtual debo escribir en la terminal: "deactivate" y se mostrará:

C:\Users\patty\Desktop\cosas_ubb\9no_semestre\Bdd_No_Relacional-Electivo\Unidad 1\guia1\entorno>

---------------------------------------INDICACIÓN REQUERIMIENTOS---------------------------------------------------------------------

8)* Para exportar los paquetes instalados que tenemos en el entorno virtual, primero hay que activarlo con: 

".\venv-python3\Scripts\activate"

Y luego escribir en la terminal el comando:

"pip freeze > requirements.txt"

Y se crea un archivo en la carpeta "Entorno" llamado: "requirements.txt", 
donde se pueden ver efectivamente todos los paquetes que tenemos instalados. 

Esto ayudaría a volver a instalar los paquetes en una futura carpeta "Entorno" donde quiera volver a trabajar, 
en el cual traspaso la carpeta "src" y requirements.txt, creo nuevamente el entorno virtual en la terminal con el comando: 

"virtualenv -p python2.7.18 venv-python3"

y para instalar todos los paquetes anteriores debo escribir en la terminal: 

"pip install -r .\requirements.txt"

y ya al ejecutar "pip list" en la terminal puedo comprobar que tengo los paquetes instalados.
Los cuales son:


click==7.1.2
Django==1.11.29
Flask==1.1.4
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
pymongo==3.13.0
pytz==2024.1
Werkzeug==1.0.1

---------------------------------------DESCARGA MONGODB COMPASS------------------------------------------------------------------------

9) Procedo a descargar Mongodb compass desde su página oficial.

Luego ingreso a cmd y ejecuto: "mongod.exe --version" y me arroja que: 

"mongo.exe" no se reconocer como un comando interno o externo, programa o archivo por lotes ejecutable. 

Lo cual quiere decir, aunque se haya instalado, hay añadirlo como una variable de entorno en 
el "Path" de mi sistema operativo para que pueda reconocerlo desde cualquier lugar.

Por lo que, en archivos de programa, abro la carpeta "MongoDB", luego "Server", luego "7.0" (la versión), 
luego "bin", en donde copio su ruta: "C:\Program Files\MongoDB\Server\7.0\bin" y 
procedo a añadirlas a sus variables de entorno. 

Me dirijo a: Configuración avanzada de este equipo, se accede a variables de entorno y en el "Path", 
agregamos el nuevo registro de la ruta: 
"C:\Program Files\MongoDB\Server\7.0\bin" 
y se acepta todo.

- Se vuelve a abrir el cmd y ejecuto el comando: "mongod.exe --version" y arroja correctamente:

C:\Users\patty>mongod.exe --version
db version v7.0.7
Build Info: {
    "version": "7.0.7",
    "gitVersion": "cfb08e1ab7ef741b4abdd0638351b322514c45bd",
    "modules": [],
    "allocator": "tcmalloc",
    "environment": {
        "distmod": "windows",
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}

Luego ejecutamos el comando: "mongod", y me arroja error diciendo que el directorio de la data no ha sido encontrado. 
Entonces en el "Disco local (C:)", creamos la carpeta "data" y dentro de esa carpeta creamos otra llamada: "db", 
el cual servirá como directorio donde mongodb deposite allí los archivos propios del servidor, 
incluyendo los archivos relacionados con cada base de datos que tengamos.

- Nuevamente se ejecuta en el cmd, el comando: "mongod", y ahora si se queda ejecutando, 
esperando la conexión con mongodb compass, que se hace al momento de presionar "Connect" en el mismo.


--------------------------------------------EXPLICACIÓN ESQUEMA DE LA BD--------------------------------------------------------------

10) Luego en "Databases" pongo el "+" y creo mi base de datos, 
donde le doy el nombre de "vuelos" y a la collection, le doy el nombre de "reservas", 
para luego agregar datos de pasajeros con reservas de vuelos para trabajar con esos datos en el programa python, 
a través del entorno virtual en la terminal.

En donde, 
- La tabla pasajeros, tiene Id y nombre_pasajero
- La tabla reserva, tiene numero_vuelo, asiento, fecha
- La tabla vuelo, tiene origen, destino

los datos son:

[{
  "_id": {
    "$oid": "660a349d83b8927ea61cc3a2"
  },
  "nombre_pasajero": "Pedro Sanchez",
  "numero_vuelo": "DEF456",
  "origen": "Ciudad C",
  "destino": "Ciudad A",
  "fecha": "2024-06-10",
  "asiento": "3C"
},
{
  "_id": {
    "$oid": "660acd6abde33c798095eda9"
  },
  "asiento": "2B",
  "nombre_pasajero": "Maria Gonzalez",
  "fecha": "2024-05-04",
  "destino": "Ciudad E",
  "origen": "Ciudad D",
  "numero_vuelo": "XYZ89"
},
{
  "_id": {
    "$oid": "660ae378e5e685bc6b27344a"
  },
  "asiento": "3D",
  "nombre_pasajero": "Carlos Sanchez",
  "fecha": "2024-03-03",
  "destino": "Canete",
  "origen": "Chillan",
  "numero_vuelo": "HDF734"
},
{
  "_id": {
    "$oid": "660b9a1416d5b0e86ed9d138"
  },
  "asiento": "1A",
  "nombre_pasajero": "Juan Perez",
  "fecha": "2024-04-15",
  "destino": "Ciudad B",
  "origen": "Ciudad A",
  "numero_vuelo": "ABC123"
}]


-------------------------------------------CONEXIÓN A LA BD------------------------------------------------------------------------

11) Luego generé la conexión entre python y mongodb a través de la codificación del programa: 

from pymongo import MongoClient

# Establecer conexion a MongoDB
cliente = MongoClient('mongodb://localhost:27017/vuelos')
db = cliente.vuelos
coleccion = db.reservas

---------------------------------------USO DEL CÓDIGO EN LA TERMINAL----------------------------------------------------------------

12) Y ya empecé a codificar el CRUD y consulta, para poder trabajar los datos agregados en la base de datos de mongodb.
En el cual, al ejecutar el código en la terminal, arrojará el siguiente menú:

Menu:
1. Crear reserva de vuelo
2. Obtener todas las reservas de vuelo
3. Obtener reserva de vuelo por nombre de pasajero
4. Actualizar reserva de vuelo por nombre de pasajero
5. Eliminar reserva de vuelo por nombre de pasajero
6. (Consulta) Mostrar nombre pasajeros que reservaron en un mes y anio especifico
0. Salir

Ingrese el numero de la opcion que desea ejecutar: 

Y AL INGRESAR EL NUMERO DEL MENU, permitirá las funciones CRUD en los datos agregados en la base de datos de mongodb, 
además de ejecutar una "consulta" adicional.
