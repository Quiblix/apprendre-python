nombre1 = float(input("Entrez le premier nombre : "))
operation = input("Entrez l'opération (+, -, *, /) : ")
nombre2 = float(input("Entrez le deuxième nombre : "))

def main():
    resultat = eval(f"{nombre1} {operation} {nombre2}")
    print(resultat)

if __name__ == "__main__":
    main()