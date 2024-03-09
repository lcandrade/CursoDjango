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
4. 