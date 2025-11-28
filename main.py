import jocs
import time

while(True):
    dibuix1 = print("""
⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⠉⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣀⣿⣿⣿⣀⣀⣀⣀⣀⣀⣀⣀⣿⣿⣿⣀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀
⣤⣤⣼⣿⣿⣿⣿⣿⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣿⣿⣿⣿⣿⣤⣤⣤
⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿
⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿
⣿⣿⡇⠀⠀⢸⣿⣿⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⣿⡇⠀⠀⣿⣿⣿
⠛⠛⠃⠀⠀⠘⠛⠛⣤⣤⣤⣤⣤⡀⠀⠀⢠⣤⣤⣤⣤⣤⠛⠛⠃⠀⠀⠛⠛⠛
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠃⠀⠀⠘⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("\n -- Benvingut/da al mini arcade -- \n")
    print("1.Juga al pedra, paper o tisora")
    print("2.Juga al endevina el numero")
    print("3.Juga al cara o creu")
    print("4.Juga al tres en ratlla")
    print("S. Sortir")

    opcio = input("Selecciona un joc: ")
    match opcio:
        case "1":
            print("\n Entrant al joc de Pedra, Paper o Tisora...")
            time.sleep(2)
            jocs.janken()
            time.sleep(2)
        case "2":
            print("\n Entrant al joc d'endevinar el numero...")
            time.sleep(2)
            jocs.nana()
            time.sleep(2)
        case "3":
            print("\n Entrant al joc de Cara o Creu...")
            time.sleep(2)
            jocs.cara_creu()
            time.sleep(2)
        case "4":
            print("\n Entrant al joc de Tres en Ratlla...")
            time.sleep(2)
            jocs.tres_en_ratlla()
            time.sleep(2)
        case "S" | "s":
            print("Gracies per jugar! Fins aviat!")
            break
        case _:
            print("Opcio no valida. Si us plau, tria una opcio valida.")
            time.sleep(2)