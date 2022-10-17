# OGbzz-Risk-Co-
Début du code source d'un jeu 2D visant à éliminer toutes les entités mutantes "abeilles" avant qu'elles n'atteignent la population

Je majoritairement eu des complications pour les chemins d'accès aux différents outils comme pip, où j'ai dû redéfinir une nouvelle 
variable d'environnement, mais en vain. Alors que j'y ai passé une trentaine de minute, j'ai stoppé mon acharnement pour
simplement utilisé cd me permettant de directement montrer le chemin à prendre au terminal. 

(Fatigant pour peu mais c'est un de 
mes défauts, à ne pas vouloir lâcher l'affaires, je ne comprends toujours pas pourquoi mon terminal ne redéfinit pas le Path...)

Pour le module pytmx, (le format d'importation de la carte et éléments de décors dans python)
j'ai eu de gros problèmes concernant ses attributs... pytmx.utile_pygame.load_pygame() semblait ne pas exister
malgré leurs présences à l'execution de : pprint(dir(pytmx))
Tout comme mon message d'erreur concernant gun pour l'attribut run.
