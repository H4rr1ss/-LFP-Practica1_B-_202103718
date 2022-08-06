#Para organizar bien las ramas y ser más ordenado al hacer codigo
#Rama main
#Rama develop
#rama write code

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

#-----Subida de archivos
# git commit -m "mensaje con el que identifique los cambios realizados"

#-----Subir a repositorio remoto todo lo guardado en esa rama
# git push origin nombre_rama



#-----Pasar el codigo de "rama = writeCode" a "rama = develop"
# 1. me cambio a rama develop
# 2. comando "git pull origin rama_writeCode"(cargó localmente)
    # llevar cambios de la rama writeCode a la rama develop
# 3. subir cambios locales a repositorio remoto


print("pasar develop a rama main")

# 1. Creo una rama realese-1.0.0
# 2. Mando rama realese-1.0.0 a repositorio remoto
# 3. voy a mi rama main
# 4. git pull origin realese-1.0.0
# 5. git push origin main
