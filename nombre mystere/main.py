import random

def main():
    a = 1    
    nombre_aleatoire = random.randint(1, 100)
    reponse = int(input("Donne un chiffre entre 1 et 100 : "))

    while nombre_aleatoire != reponse:
        print("Il y a une différence de :")       
        print(abs(reponse - nombre_aleatoire))
        reponse = int(input("Donne un chiffre entre 1 et 100 : "))
        a += 1
        print("nb de tentatives", a)
        

    print("Bien joué !")

if __name__ == "__main__":
    main()