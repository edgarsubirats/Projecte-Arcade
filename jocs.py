from robot import robot
import time
import random
from robot import cara_creu_robot

def janken():
    print("-- Benvingut/da al joc de Pedra, Paper o Tisora! --\n")
    time.sleep(1)
    print ("1.Jugar a 3 rondes")
    print ("2.Jugar al millor de 5")
    match= input("Selecciona una opcio: ")
    if match == "1":
        rondes_max= 3 
    elif match == "2":
        rondes_max = 5
    else:
        print("Opcio no valida. Si us plau, tria 1 o 2.")
        return janken()
    time.sleep(1)
    contador_rondes= 0
    victories_jugador= 0
    victories_maquina= 0

    while contador_rondes < rondes_max:
        print(f"\n Has triat jugar {rondes_max} rondes. \n")
        opcions= input("Escull entre pedra, paper o tisora:").lower()
        if opcions.lower() not in ["pedra","paper" , "tisora"]:
            print("Opcio no valida. Si us plau, tria Pedra, Paper o Tisora.")
            continue
        maquina =robot().playing()
        contador_rondes += 1
        print (f"\n Ronda {contador_rondes}:")
        print (f"Jugador -> {opcions}")
        print (f"Maquina -> {maquina}")
        resultat = (opcions, maquina)
        if resultat == ("pedra","tisora") or resultat == ("paper","pedra") or resultat == ("tisora","paper"):
            print("Has guanyat aquesta ronda!")
            victories_jugador += 1
        elif resultat == ("tisora","pedra") or resultat == ("pedra","paper") or resultat == ("paper","tisora"):
            print("La maquina ha guanyat aquesta ronda!")
            victories_maquina += 1
        else:
            print("Aquesta ronda ha acabat en empat!")
        print (f"\n Marcador actual: Jugador {victories_jugador} - Maquina {victories_maquina}\n")
    print("El joc ha acabat!")

def nana():
    print("\n -- Benvingut/da al joc de endevinar el numero -- \n")
    time.sleep(1)
    numero_secret = random.randint(1, 100)
    intents = 0
    while True:
        endevina = input("Introdueix un numero entre 1 i 100: ")
        intents += 1
        endevina = int(endevina)
        if endevina < numero_secret:
            print("El numero es massa baix. Prova de nou.")
        elif endevina > numero_secret:
            print("El numero es massa alt. Prova de nou.")
        else:
            print(f"Felicitats! Has endevinat el numero {numero_secret} en {intents} intents.")
            break
        diferencia = abs(numero_secret - endevina)
        if diferencia <= 5:
            print("Calent!")
        elif diferencia <= 20:
            print("Vas per bon cami!")
        else:
            print("Fred!")
def cara_creu():
    print ("\n -- Benvingut/da al joc de Cara o Creu -- \n")
    time.sleep(1)
    jugador = input ("Tria Cara o Creu: ").lower()
    if jugador not in ["cara", "creu"]:
        print("Opcio no valida. Si us plau, tria Cara o Creu.")
        return cara_creu()
    maquina = cara_creu_robot().playing()
    print (f" Jugador -> {jugador}")
    print (f" Maquina -> {maquina}")
    if jugador == maquina:
        print("Has guanyat!")
    else:
        print("La maquina ha guanyat!")
    
        
if __name__ == "__main__":
    janken()
    nana()