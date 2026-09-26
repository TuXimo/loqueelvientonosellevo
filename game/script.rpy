# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define prota = Character("Parquita", color="#120000")
define r= Character("Renzo", color="#F285B8")
define v= Character("Valentina", color="#FFC7F0")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "parquita happy.png" al directorio
    # 'images'.

    show prota

    # Presenta las líneas del diálogo.

    prota "Has creado un nuevo juego Ren'Py."

    prota "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
