score = 0
liste = {"France": "Paris","Espagne":"Madrid","Italie":"Rome"}
for pays in liste:
   reponse = input(f"Quelle est la capitale du {pays} :")
   if reponse == liste[pays] : 
        print("Bonne réponse ")
        score += 1 
        print(score)
   else:
            print("Mauvaise réponse")
            score -= 1
            print(score)
