#Personajes
define reina = Character('Reina  Eileen', color ="#C28110")

define mago = Character('mago', color= "#A28110")

# creamos una flag osea una variable
default nombre = False





#imagenes 
# image backgroundpng = "bg washington"
image backgroundpng = "Futon_Room.png"

image ReinaE = "eileen happy.png"

image magoE = "mago.png"

#inicio del juego
label start:

    #sonido musica
    play music  "audio/musicafondo.mp3"

    #scene es para los backgrounds
    scene backgroundpng
    with fade

    "Hola que tal"
    "Buenos dias"   
    stop music

    #show es para mostrar personajes  se pone por encima del background 
    # show ReinaE
    #at left, right, center para la posicion del personaje
    show ReinaE at right
    with fade

    reina "Yo soy la reina"
    # show magoE at topleft 
    show magoE at Position(xpos = 100,ypos= 850)  
    play sound "audio/BongoMenu3.wav"
    reina "me voy"
    #hide oculta  a un personaje  y lo elimina de la escena,
    # en este caso de la escena principal
    
    hide ReinaE
    #dissolve  hace desaparecer gradualmente el personaje
    with dissolve

    #hacer una pregunta
    mago "¿Como te llamas?"

    #menu para las opciones de preguntas 
menu:
        #salto al label de nombre osea a la opcion
        #siempre se debe poner los puntos :
        "me llamo sergio":
        # salto al labe  nombre     
            jump nombre
        "no te lo voy a decir":
            jump nonombre1       


    #mensaje de que se termino el juego
    # "Se termina el juego"
return

label nombre:
    #cambiar la variable su valor
    $ nombre = True
    mago "Un gusto conocerte"
    jump terminar        


label nonombre1:
    mago "que pinche mamon eres"

    jump terminar        

label terminar:

if nombre:
    mago "Recuerdo que me disjiste tu nombre"
else:
    mago "Recuerdo que no me disjiste tu nombre"











