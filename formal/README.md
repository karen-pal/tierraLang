# tierraLang
lenguaje 

inspirado en la obra de Horacio Banegas

Pensado para livecodear con letras de Horacio, modificando videos hechos con IA

https://karen-pal.github.io/curso_construcci-n_sentidos/clase8_semantica/desaparezco.html

# Prereq
* node
* npm
* nearleyjs
* express
* cors

Escriben sus gramáticas en poema.ne usando BNF

# Generar automáticamente parser
Luego de escribir sus gramáticas, para generar un parser usen el comando

`nearleyc poema.ne -o poem.js`

## testear en la consola
nearley-test -i "brilla#abraza#sopla" poem.js

# Uso de senryu
levantar el server

node server.js

abrir desaparezco.html en un navegador.

introducir un poema. 

>Versos separados por numerales. Ver ejemplos

# Ejemplos
florece#florece#florece


florece#como una hoja de loto#florece


florece#como una hoja de loto#desaparezco


como gotas de rocio#desaparezco#sobre el arbol muerto
