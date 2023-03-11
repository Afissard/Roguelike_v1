# My Roguelike version n°1 :

The objective of this project is to create a (finished) game that be run on a raspberry or any other low spec computer.

## My idea (in french sorry):
Inspiré du jeu de la vie de Conway et autre simulation de vie (Dwarf Fortress, etc):
Le but est de simuler l'ssault d'un donjon générer procéduralement (nombre d'étage infini), et d'observer comment et jusqu'où sont capable d'allez les "héros".

---------------------------------
### Le monde se divise en 2 partie :
Overworld : un hub avec l'entrée du donjon, une tarverne (repos + quêtes), des magasins, (arène pour duel pvp ?).
Le donjon : Chaque niveau est procéduralement généré, avec des ennemis aléatoirement placé, tout les 10 niveaux un boss protège l'accès au niveau suivant.

---------------------------------
### Les "héros" :
But (dans l'ordre d'importance): 
	1: Ne pas mourir
	2: Allez le plus loins dans le donjons (classement compétif entre héros)
	3: Etre le plus fort des héros (niveaux, équipement, succès, richesse) (classement pvp ?)

### Mécanique/règles :	
- Les héros peuvent attaquer et tué les ennemis, qui leurs donnent de l'xp, de l'or et peut être de l'équipement (drop de boss à 100%, mais réserver au héros/groupe qui le tue).
- A chaque niveux passer un héros gagne 1 point de stat à investir (il a 25 points de statistique répartie aléatoirement au niveaux 1). Tout les 5 niveaux le héros débloque un nouveaux tier d'équipements.
- Un héros peut retourner (sauf exeption : piège, etc) quand il le souhaite au hub pour se reposer, vendre/acheter de l'équipements dans les magasins.
- Les héros peuvent créer/rejoindre/quitter des groupes (5 héros max) pour s'entre aider.

### Statistiques :
- PV 	: peut se regénérer avec des potions/sort ou passivement dans la taverne/avec de l'équipement.
- Mana 	: points pour lancer des sorts, se récupère passivement ainsi que comme les PV.
- Chance 	: affect les drops : or, équipements.
- Force 	: permet de porter équipement lourd, d'utiliser certaines armes.
- Agilité: permet de se déplacé plus vite, d'esquiver, d'utiliser certaines armes.
- Foi	: permet de lancer des sorts (avec Mana), d'utiliser certaines armes

### Comportement :
Le comportement de chaque héros est déterminer par une seed (4 bits = 1 stat) avec un % (1111 = 100% et 0000 = 0%).
- Tendance à rejoindre un groupe/jouer en solo
- Tendance à la compétition -> pret à tout pour monter dans le classement (même tuer d'autres héros pour obtenir son inventaire)
- Courage : tendance à mettre sa vie en danger ou à l'inverse fuir les combats/exploiter ses allié

---------------------------------
### Les "ennemis" :
But (dans l'ordre d'importance): 
	1: Tuer un maximum de héros pour recevoir une promotion

# TODO :
- *create a player* [done]
- A camera who follow the player
- create enemy and a simple combat system
- User interface
- generate random enemy for each level
- procedural level generation
- better graphics