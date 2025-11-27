import jocs
import time
while(True):
    print("\n -- Benvingut/da al mini arcade -- \n")
    print("1.Juga al pedra, paper o tisora")
    print("2.Juga al endevina el numero")
    print("3.Juga al cara o creu")
    print("S. Sortir")
    opcio = input("Selecciona un joc: ")
    match opcio:
        case "1":
            print("\n Entrant al joc de Pedra, Paper o Tisora...")
            jocs.janken()
            time.sleep(2)
        case "2":
            print("\n Entrant al joc d'endevinar el numero...")
            jocs.nana()
            time.sleep(2)
        case "3":
            print("\n Entrant al joc de Cara o Creu...")
            jocs.cara_creu()
            time.sleep(2)
        case "S" | "s":
            print("Gracies per jugar! Fins aviat!")
            break
        case _:
            print("Opcio no valida. Si us plau, tria una opcio valida.")
            time.sleep(2)