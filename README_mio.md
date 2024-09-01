# SOCIAL OPLESK
### 🏴‍☠️ HACKS - BACKEND - 1

<br/>
1.- Clone el repo
    git clone https://github.com/magahr/hack_backend_python_1.git

2.-Entre en le directorio de repo 
   cd hack_backend_python_1

3.-Cree el ambiente virtual
   python  -m venv .venv

4.-Cree el .gitignore y cloque a:
   # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/   
5.- Salir de Visual CODE

6.- Entrar a la carpeta del repo

7.- Abrir Visual Code desde la carpeta del repo para que se vea .venv ignorado

8.-Active el ambiente virtual
   Pasar a la consola command prompt
   Pasar al directorio del repo:
      cd hack_backend_python_1
   Activar el ambiente
   .venv\Scripts\activate

9.-Cree el ambiente con requirements.txt
   pip install -r requirements.txt 

10.-Levante el servidor:
   Ejecutar servidor app.py en terminal: 
   flask run --debug 


NOTA: en caso de no reconocer el comando "pytest"
          ejecutar el pytest así: python -m pytest test_hack.py -v
                                  pytest -v test_server.py::test_hack_1
                        python -m pytest -v test_server.py::test_hack_1

Control de version:

git commit -m "Making environment"
git commit -m "Making all commit"

