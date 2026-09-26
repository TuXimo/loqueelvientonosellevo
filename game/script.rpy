# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define p = Character("Parquita", color="#120000")
define r= Character("Renzo", color="#a41136")
define v= Character("Valentina", color="#FFC7F0")
define m= Character("Muerte", color="#000000")




label start:

    $renpy.pause(3.0, hard=True)

    scene bg room

    show p

    "Dicen que la Muerte nunca descansa"
    "Pero eso es mentira... "
    "Una mentira vieja como el viento y letal como la misma Muerte"
    "Una vez, la Parca, la Huesuda, la Muerte... {w} decidió tomarse dos semanas de vacaciones en una isla olvidada  "
    "Todo parecía estar tranquilo hasta que recibió una llamada, el superior le tenía una misión"

    m "¿Un ciclón?"
    
    "La Muerte suspiró y dijo"

    m " La verdad es que estoy de vacaciones durante dos semanas... pero tengo a alguien a quien mandar con una sonrisa llamo, tomó el teléfono y llamó a una joven becaria."
    m "Parkita, tengo una misión muy importante para ti"

    "Parkita levantó la mirada, algo confundida"

    p "¿Para mí?"

    "Preguntó con timidez"

    m "Serás mi reemplazo durante estas dos semanas, será tu prueba para ver si estás preparada"

    "La Muerte le entregó su vieja guadaña, una guadaña demasiado grande y pesada junto una túnica, la joven apenas podía sostenerla mientras intentaba acomodarse la túnica negra que le habían dado "

    p "¿Y qué se supone que tengo que hacer?"

    "La Muerte le entregó entonces un pequeño libro."

    m "Cosecha almas para mí y sobre todo sigue las reglas que te di"

    "Parkita abrió el libro"
    "Había demasiadas reglas"

    p "¿Y si no las sigo?"

    "La Muerte sonrió de forma que incomodaba a Parkita "
    
    m "Te deseo suerte y buena cosecha"

    "Parkita tragó saliva mientras pensaba una sola cosa ¿Tan difícil es?"
    "La Muerte se dio media vuelta y comenzó a alejarse, hacia los cocos y la playa mientras soltó una frase "

    m "Es un trabajo que te matará lentamente haha"

    "Parkita se quedó en silencio ¿Eso se supone que era un chiste?"
    "La Muerte ya se había ido y así comenzó el primer día de vacaciones de la Muerte y el primer día de trabajo de Parkita."

    
    return
