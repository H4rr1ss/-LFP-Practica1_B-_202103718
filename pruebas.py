print("Comandos importantes para GitHub")

#-----Creará una nueva rama (-b es cuando se crea rama)
# git checkout -b "nombre_rama" (solo agrega localmente)

#-----Para subir mi codigo de repositorio local a repositorio remoto
# git push origin nombre_rama   (origin = repo. remoto)

#-----Si he creado ramas remotamente, trae las nuevas al repositorio local
# git fetch origin

#-----para cambiar entre rama ya existente
# git checkout nombre_rama(a la que deseo moverme)


print("para subir codigo a GitHub(cambios de código en general)")

#-----Se utiliza (.) para agregar TODOS los cambios o puede agregar un archivo especifico
# git add .
# git add archivo_especifico.py


print("Realizar commit")

#-----Subida de archivos
# git commit -m "mensaje con el que identifique los cambios realizados"