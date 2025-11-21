import jocs
while(True):
    print("\n -- Benvingut/da al mini arcade -- \n")
    print("1.Juga al pedra, paper o tisora")
    print("2.Juga al endevina el numero")
    print("S. Sortir")
    opcio = input("Selecciona un joc: ")
    match opcio:
        case "1":
            print("\n Entrant al joc de Pedra, Paper o Tisora...")
            jocs.janken()
        case "2":
            print("\n Entrant al joc d'endevinar el numero...")
            jocs.nana()
        case "S" | "s":
            print("Gracies per jugar! Fins aviat!")
            break
        case _:
            print("Opcio no valida. Si us plau, tria una opcio valida.")