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

    # Le Joueur (Carré Bleu)
    taille_carre = 50
    carre = pygame.Rect(LARGEUR // 2 - taille_carre // 2, HAUTEUR // 2 - taille_carre // 2, taille_carre, taille_carre)
    vitesse = 7

    # 2. La Cible (Carré Rouge)
    taille_cible = 30
    # On génère des coordonnées X et Y aléatoires dans les limites de l'écran
    cible_x = random.randint(0, LARGEUR - taille_cible)
    cible_y = random.randint(0, HAUTEUR - taille_cible)
    cible = pygame.Rect(cible_x, cible_y, taille_cible, taille_cible)

    # 3. Le Score et la Police d'écriture
    score = 0
    # None utilise la police par défaut de Pygame, 36 est la taille
    police = pygame.font.SysFont("Arial", 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        touches = pygame.key.get_pressed() 

        # Déplacement du joueur
        if touches[pygame.K_LEFT] or touches[pygame.K_q]: 
            carre.x -= vitesse
        if touches[pygame.K_RIGHT] or touches[pygame.K_d]: 
            carre.x += vitesse
        if touches[pygame.K_UP] or touches[pygame.K_z]:
            carre.y -= vitesse
        if touches[pygame.K_DOWN] or touches[pygame.K_s]:
            carre.y += vitesse

        carre.clamp_ip(limite_ecran)

        # 4. Détection de la collision
        # colliderect renvoie True si le carré bleu et le carré rouge se touchent
        if carre.colliderect(cible):
            score += 1 # On augmente le score
            # On déplace la cible à une nouvelle position aléatoire
            cible.x = random.randint(0, LARGEUR - taille_cible)
            cible.y = random.randint(0, HAUTEUR - taille_cible)

        # --- DESSIN ---
        screen.fill(BLANC)
        
        # Dessin de la cible (Rouge)
        pygame.draw.rect(screen, ROUGE, cible)
        
        # Dessin du joueur (Bleu)
        pygame.draw.rect(screen, BLEU, carre)

        # 5. Affichage du Score à l'écran
        # On crée une image textuelle : "Texte", Antialiasing (True), Couleur
        surface_texte = police.render(f"Score : {score}", True, NOIR)
        # On affiche cette image aux coordonnées (20, 20)
        screen.blit(surface_texte, (20, 20))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()