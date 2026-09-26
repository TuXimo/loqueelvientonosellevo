label capitulo4:

    #scene bg room

    show parquita

    "Parkita permaneció sola en lo alto del edificio."
    "Miró hacia el enorme parque, después miró su libro y lo abrió una vez más, pero las reglas seguían sin darle una respuesta."
    "Por primera vez desde que comenzó su trabajo... Parkita tenía 3 almas que podía salvar, tan diferentes entre sí que era difícil decidir."

    "Recordó a cada una de las almas que conoció durante su travesía:"
    "Valentina: Podría aprender empatía por otros seres vivos."
    "Renzo: Podría aprender a cambiar y ser mejor para su familia."
    "Sebastián: A veces solo hay que esperar a la persona..."

    "El destino de estas tres vidas estaba en sus manos. Usando todo lo que había aprendido, tomó su decisión:"

    show parquita at left
    show valentina at center
    show renzo at right



    menu:
        "Salvar a Valentina":
            $ eleccion_final = "valentina"
            parquita "Valentina merece esta oportunidad... aprenderá a tener empatía por los seres que la rodean."
            "Parkita dio un paso atrás y devolvió el alma a Valentina."
            "En el hospital, Valentina despertó del coma con una nueva perspectiva y el deseo sincero de cambiar."

        "Salvar a Renzo":
            $ eleccion_final = "renzo"
            parquita "Renzo merece esta oportunidad... aprenderá a cambiar y ser mejor para su familia."
            "Parkita dio un paso atrás y devolvió el alma a Renzo."
            "Renzo abrió los ojos, sintiendo una profunda necesidad de reparar sus errores con sus seres queridos."

        "Salvar a Sebastián":
            $ eleccion_final = "sebastian"
            parquita "Sebastián merece esta oportunidad... a veces solo hay que esperar a la persona."
            "Parkita dio un paso atrás y devolvió el alma a Sebastián."
            "Sebastián volvió a respirar, recibiendo el tiempo necesario para encontrar su camino."

    "Con la decisión tomada, Parkita miró al cielo nocturno."
    "El viento sopló suavemente a su alrededor, llevándose consigo las dudas..."
    "El primer trabajo de la nueva Muerte había concluido."

    # [Nota de gameplay que el jugador elija a quien salvar
    # que use lo aprendido para tomar la decisión]  

    "FIN"

    return
