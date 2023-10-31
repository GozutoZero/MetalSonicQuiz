import json

def cargar_datos(archivo):
    try:
        with open(archivo, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    return data

def guardar_datos(archivo, data):
    with open(archivo, "w") as json_file:
        json.dump(data, json_file, indent=4)
        
def Filtro(data_aux, pregunta, respuesta):
    data_aux = [personaje for personaje in data_aux if personaje[pregunta] == respuesta]
    return data_aux

def buscarPersonaje(data, pregunta, respuesta):
    coincidencias = [personaje for personaje in data if personaje[pregunta] == respuesta]
    if len(coincidencias) == 1:
        return coincidencias[0]["Personaje"]
    return None

def nuevo_p(data, genero, lado, armas, whisp, tecnologia, principal, chaose, superf, vuela, zombot):
    archivo = "Sonic.json"
    data_p=cargar_datos(archivo)
    
    if genero is None:
        genero =input("¿Que genero es tu personaje? (Hombre, Mujer, No Tiene)\n")
    if lado is None:
        lado =input("¿De que lado esta tu personaje? (Bueno, Malo, Relativamente)\n")
    if armas is None:
        armas =input("¿Tu personaje usa armas? (Si, No, Relativamente)\n")
    if whisp is None:
        whisp =input("¿Tu personaje tiene amistad con los Wisp? (Si, No, Relativamente)\n")
    if tecnologia is None:
        tecnologia =input("¿Tu personaje tiene conexion con la tecnologia? (Si, No, Relativamente)\n")
    if principal is None:
        principal =input("¿Tu personaje es de los principales? (Si, No, Relativamente)\n")
    if chaose is None:
        chaose =input("¿Tu personaje a tenido en su poder una Esmeralda del Caos? (Si, No, Relativamente)\n")
    if superf is None:
        superf =input("¿Tu personaje tiene una forma Super? (Si, No, Relativamente)\n")
    if vuela is None:
        vuela =input("¿Tu personaje puede volar? (Si, No, Relativamente)\n")
    if zombot is None:
        zombot =input("¿Tu personaje se llego a convertir en zombot? (Si, No, Relativamente)\n")

    Nom=input("¿Cual es su nombre?\n")
    TXT={
        "Personaje": Nom ,
        "Genero": genero ,
        "Lado": lado ,
        "Armas": armas ,
        "Whisp": whisp ,
        "Tecnologia": tecnologia ,
        "Principal": principal ,
        "ChaosE": chaose ,
        "Super": superf ,
        "Vuela": vuela ,
        "Zombot": zombot
        }
    data_p.append(TXT)
    
    preguntas = [
        ("Genero", genero),
        ("Lado", lado),
        ("Armas", armas),
        ("Whisp", whisp),
        ("Tecnologia", tecnologia),
        ("Principal", principal),
        ("ChaosE", chaose),
        ("Super", superf),
        ("Vuela", vuela),
        ("Zombot", zombot)
    ]
    for pregunta, respuesta in preguntas:
      data_p=Filtro(data_p, pregunta, respuesta)
      personaje = buscarPersonaje(data_p, pregunta, respuesta)
      if personaje:
          print("Tu personaje fue agregado correctamente")
          break
    if not personaje:
        print("Tu personaje ya estaba en mi base de datos -_-\n")
        return data
      
    data.append(TXT)
    guardar_datos(archivo, data)
    print("MSQ: Nuevos datos adquiridos\n")
    return data

def main():
    archivo = "Sonic.json"
    data = cargar_datos(archivo)
    data_aux = cargar_datos(archivo)
    print("Bot: Hola, soy Metal Sonic Quiz, se todo sobre Sonic, sus amigos y hasta sus no-amigos.\nPuedo diferenciarlos con estas preguntas:")

    genero = None
    lado = None
    armas = None
    whisp = None
    tecnologia = None
    principal = None
    chaose = None
    superf = None
    vuela = None
    zombot = None

    preguntas = [
        ("Genero", "¿Que genero es tu personaje? (Hombre, Mujer, No Tiene)"),
        ("Lado", "¿De que lado esta tu personaje? (Bueno, Malo, Relativamente)"),
        ("Armas", "¿Tu personaje usa armas? (Si, No, Relativamente)"),
        ("Whisp", "¿Tu personaje tiene amistad con los Wisp? (Si, No, Relativamente)"),
        ("Tecnologia", "¿Tu personaje tiene conexion con la tecnologia? (Si, No, Relativamente)"),
        ("Principal", "¿Tu personaje es de los principales? (Si, No, Relativamente)"),
        ("ChaosE", "¿Tu personaje a tenido en su poder una Esmeralda del Caos? (Si, No, Relativamente)"),
        ("Super", "¿Tu personaje tiene una forma Super? (Si, No, Relativamente)"),
        ("Vuela", "¿Tu personaje puede volar? (Si, No, Relativamente)"),
        ("Zombot", "¿Tu personaje se llego a convertir en zombot? (Si, No, Relativamente)")
    ]

    for pregunta, descripcion in preguntas:
        respuesta = input(f"MSQ: {descripcion}: \n").strip()
        if pregunta == "Genero":
            genero = respuesta
        elif pregunta == "Lado":
            lado = respuesta
        elif pregunta == "Armas":
            armas = respuesta
        elif pregunta == "Whisp":
            whisp = respuesta
        elif pregunta == "Tecnologia":
            tecnologia = respuesta
        elif pregunta == "Principal":
            principal = respuesta
        elif pregunta == "ChaosE":
            chaose = respuesta
        elif pregunta == "Super":
            superf = respuesta
        elif pregunta == "Vuela":
            vuela = respuesta
        elif pregunta == "Zombot":
            zombot = respuesta
        data_aux=Filtro(data_aux, pregunta, respuesta)
        personaje = buscarPersonaje(data_aux, pregunta, respuesta)
        if personaje:
            print(f"MSQ: Se quien es. . .¡Es {personaje}!")
            respuesta=input("¿Estoy en lo cierto?\n(si, no)\n")
            if respuesta.lower() == "no":
                nuevo_p(data, genero, lado, armas, whisp, tecnologia, principal, chaose, superf, vuela, zombot)
            break

    if not personaje:
        print("MSQ: Tu personaje no estaen mis datos>:|")
        nuevo_p(data, genero, lado, armas, whisp, tecnologia, principal, chaose, superf, vuela, zombot)
        
while (True):
    finish=input("Bot:Para continuar presione enter\nBot: Para salir pulse q\n")
    if finish.lower() == "q":
        print("MSQ: NOs vemos.")
        break
    main()
