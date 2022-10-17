import pygame
import pyscroll
import pytmx


#Concept de OGbzz
class Game:
    def __init__(self) -> None:
        #Création de la fenêtre du Jeu
        self.screen = pygame.display.set_mode((800 , 600))
        pygame.display.set_caption("PygmeOG")
        
        #Charger la carte (tmx)
        tmx_data = pytmx.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        #Dessin du groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        
        pass

#Boucle du jeu
def run(self):
    running = True

    while running:
        
        self.group.draw(self.screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
            
pygame.quit()