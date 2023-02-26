# Multiplayer Roguelike version n°1 :

The objective of this test is to create a demo to be run on a raspberry.

The client :
- will run a pygame app and send to the server his informations (player position, actions, etc).
- get the level information and display them
- but could also be run offline.

The server :
- will just recive and analyse (anti cheat, etc) the information and save them.
- send to the clients all level information : map, enemis
- must have an interface with an admin to be turn On/Off.

# TODO :
- Choose connection type : TCP (safe but slow) / UDP (fast but unsafe).
- admin interface to control the server (an admin client ?).
- the client recive a small image, analyse each pixel = 1 tile, and draw the map depending on the color of the pixel.
