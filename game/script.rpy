#Personajes
define reina = Character('Reina  Eileen', color ="#C28110")

#imagenes 
image backgroundpng = "bg washington"

image ReinaE = "eileen happy.png"


#inicio del juego
label start:
    #scene es para los backgrounds
    scene backgroundpng
    with fade

    "Hola que tal"
    "Buenos dias"   
    #show es para mostrar personajes  se pone por encima del background 
    # show ReinaE
    
    show ReinaE
    with fade

    reina "Yo soy la reina"
    reina "me voy"
    #hide oculta  a un personaje  y lo elimina de la escena,
    # en este caso de la escena principal
    
    hide ReinaE
    #dissolve  hace desaparecer gradualmente el personaje
    with dissolve


    "Se termina el juego"
    




