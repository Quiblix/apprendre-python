nombre1 = float(input("Entrez le premier nombre : "))
operation = input("Entrez l'opération (+, -, *, /) : ")
nombre2 = float(input("Entrez le deuxième nombre : "))

def main():
    if nombre2 == 0:
        nombre3 = float(input("Division par zéro impossible. Entrez le troisième nombre :"))
        resultat = eval(f"{nombre1} {operation} {nombre3}")
        print("resultat :", resultat)
    else:
        resultat = eval(f"{nombre1} {operation} {nombre2}")
        print("resultat :", resultat)

if __name__ == "__main__":
    main()
