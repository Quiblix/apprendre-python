import pygame
import sys
import random # 1. On importe random pour positionner la cible au hasard

def main():
    LARGEUR = 1000
    HAUTEUR = 600

    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
    limite_ecran = screen.get_rect()
    pygame.display.set_caption("Mon Jeu - Chasse aux cibles")
    clock = pygame.time.Clock()
    
    # Couleurs
    BLANC = (255, 255, 255)
    BLEU = (0, 100, 255)
    ROUGE = (255, 50, 50)
    NOIR = (0, 0, 0)
    obstacles = []
    timer = 90

    # Variables de physique
    gravite = 0.3
    force_saut = 15
    vitesse_y = 0
    vitesse_x = 6

    carre_l = LARGEUR // 2
    carre_h = HAUTEUR - 150

    
    # Le Joueur (Carré Bleu)
    scale = 1.8
    taille_carre = int(25 * scale)
    carre = pygame.Rect(carre_l - taille_carre // 2, carre_h - taille_carre // 2, taille_carre, taille_carre)

    SOL = carre_h + (taille_carre/2)

    au_sol = True


    largeur_obstacles =  15 * scale
    hauteur_obstacles = 20 * scale
    x_apparition = LARGEUR
    y_apparition = SOL - hauteur_obstacles
    sommet_a = 20
    sommet_b = 20
    sommet_c = 20
    x_apparition_2 = LARGEUR
    y_apparition_2 = SOL - hauteur_obstacles

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP]:
             carre.y -= force_saut
             au_sol = False

        if au_sol != True :
            vitesse_y += gravite
            carre.y += int(vitesse_y)

        if carre.bottom >= SOL :
           vitesse_y = 0
           carre.y = carre_h - taille_carre // 2
           au_sol = True

        # On affiche tous les obstacles de la liste
        timer -= 1

        if timer <= 0:
            # 1. Crée un nouveau Rect
            nouvel_obstacle = pygame.Rect(x_apparition, y_apparition, largeur_obstacles, hauteur_obstacles) 
            # 2. AJOUTE le nouvel obstacle à ta liste 'obstacles'
            obstacles.append(nouvel_obstacle)
            
            # 3. RECOUVRE le timer pour le prochain obstacle
            timer = random.randint(60, 120)

            type_obstacle = random.choice(["rectangle", "triangle"])
        
        # Pour chaque obstacle de la liste, on le fait avancer vers la gauche
        for obs in obstacles:
            obs.x -= vitesse_x
            if carre.colliderect(obs):
                score -= 1

        if score != 0 :
            main()
        


        # --- DESSIN ---
        screen.fill(BLANC)
        pygame.draw.line(screen,NOIR, (0, SOL), (LARGEUR, SOL),2)
        for obs in obstacles:
            pygame.draw.rect(screen, ROUGE, obs)
        
        # Dessin du joueur (Bleu)
        pygame.draw.rect(screen, BLEU, carre)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()