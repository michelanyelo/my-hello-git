# Apuntes
# cd "directorio proyecto"
# git config --global user.name "USUARIO PC"
# git config --global user.email "USUARIO CORREO"
# git init
# git branch -m main (renombrar branch master a main)
# git add "archivo.py" agregar a la cola
# git commit -m "mensaje con los cambios hechos"
# git checkout "archivo.py o hash o main" cambiar puntero a cualquier fotografía
# git config --global alias.historial "log --graph --decorate --all --oneline" Alias historial añadido al archivo global
# git diff Muestra los cambios de los ficheros sin tomar una fotografia
# git reflog Muestra todo el historial de cambios
# git reset --hard "hash o alias" regresar al primer cambio y tambien al ultimo
# git branch "nombre" crear una instancia de rama
# git switch "cabecera (main o nombre del branch)" cambiar puntero de cabecera
# git merge "nombre de cabecera (puede ser main o nombre del branch)" Une las ramas independientes al main
# gir push Sube a github los cambios realizados en el local
# git fetch Descargará el contenido remoto sin modificar el estado del repositorio local
# git pull Descargará el contenido remoto con los cambios al local
# git clone "ssh" "nombre carpeta" Descarga el proyecto a la ubicacion mencionada
print("New Hello Git! with changes")
