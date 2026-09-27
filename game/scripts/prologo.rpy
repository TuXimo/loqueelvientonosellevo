label prologo:

    $ renpy.pause(3.0, hard=True)


    # Música de fondo del prólogo, en loop
    play music "audio/prologo_tema.mp3" loop fadein 1.0

    scene fondo_prologo with fade

    "Dicen que la Muerte nunca descansa."
    "Pero eso es mentira."
    "Una mentira vieja como el viento y letal como la misma Muerte."
    "Una vez, la Parca, la Huesuda, la Muerte... {w} decidió tomarse dos semanas de vacaciones en una isla olvidada."
    "Todo parecía estar tranquilo hasta que recibió una llamada, el superior le tenía una misión."

    muerte "¿Un ciclón?"
    
    "La Muerte suspiró y dijo"

    muerte "La verdad es que estoy de vacaciones durante dos semanas... pero tengo a alguien a quien mandar con una sonrisa."
    
    "Tomó el teléfono y llamó a una joven becaria."

    muerte "Parkita, tengo una misión muy importante para ti."

    scene fondo_prologo1 with fade
    show parquita nerviosa

    "Parkita levantó la mirada, algo confundida."

    parquita "¿Para mí?"

    "Preguntó con timidez."

    muerte "Serás mi reemplazo durante estas dos semanas, será tu prueba para ver si estás preparada."

    "La Muerte le entregó su vieja guadaña, una guadaña demasiado grande y pesada junto a una túnica. La joven apenas podía sostenerla mientras intentaba acomodársela."

    parquita "¿Y qué se supone que tengo que hacer?"

    "La Muerte le entregó entonces un pequeño libro."

    muerte "Cosecha almas para mí y sobre todo sigue las reglas que te di."

    "Parkita abrió el libro."
    "Había demasiadas reglas."

    parquita "¿Y si no las sigo?"

    "La Muerte sonrió de forma que incomodaba a Parkita."
    
    muerte "Te deseo suerte y buena cosecha."

    "Parkita tragó saliva mientras pensaba una sola cosa: ¿Tan difícil es?"
    "La Muerte se dio media vuelta y comenzó a alejarse, hacia los cocos y la playa mientras soltó una frase:"

    muerte "Es un trabajo que te matará lentamente haha."

    "Parkita se quedó en silencio. ¿Eso se supone que era un chiste?"
    "La Muerte ya se había ido y así comenzó el primer día de vacaciones de la Muerte y el primer día de trabajo de Parkita."

    return

