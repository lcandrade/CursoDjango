# CURSO DJANGO

## Pasos para versionar el código con git
1. Extraer todas las dependencias del proyecto
```
pip freeze > requirements.txt
```
2. inicializar el repositorio 
```
git init
```
3. Crear el archivo .gitignore en la raiz del proyecto (para que no se versione archivos que no deben ser versionados)
```
# Django #
envdj
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
```
4. Agregar archivos para seguimiento, git add . y git status (visualiza los cambios realizados en el código)
```
git add .
git status
```
5. Realizar commit
```
git commit -m "creacion del proyecto y aplicaciones departamentos, empleados y home"
```
6. Opcional, si es la primera ver en usar git, ejecutar los siguientes comandos:
```
git config --global user.email "lcecilia09@gmail.com"
git config --global user.name "Laura Cecilia Andrade"
```
7. Ejecutar git branch (para verificar la rama actual del trabajo)
```
git branch
```
8. Renombrar la rama master por main
```
git branch -M main
```
9. Agregar la direccion remota del repositorio
```
git remote add origin https://github.com/lcandrade/CursoDjango.git
```
10. Consultar la direccion remota del repositorio
```
git remote --v
```
11. Empujar o subir el proyecto al repositorio
```
git push -u origin main
```
12. 