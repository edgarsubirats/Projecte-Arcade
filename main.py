from jocs import janken
while(True):
    print("\n -- Benvingut/da al mini arcade -- \n")
    print("1.Juga al pedra, paper o tisora")
    print("2.Juga al endevina el numero")
    print("S. Sortir")
    opcio = input("Selecciona un joc: ")
    match opcio:
        case "1":
            janken()
        #case "2":
        
        case "S" | "s":
            print("Gracies per jugar! Fins aviat!")
            break