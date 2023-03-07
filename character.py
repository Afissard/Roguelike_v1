import pygame

class Character:
    """
    Menu for characters creation
        - list of characters (max 4)
        - Name, races, classes
            - personality (general change with the race)
        - physical health : 'default_stat', 'current_statut'
        - mental health : 'default_stat', 'current_statut'
        - actions (attacks, items, interaction with the rest of the group)
    """
    def __init__(self, name:str):
        self.name = name or "nameless" # must be a string
        self.race = ""
        self.classe = ""
        self.position = "" # position in the group
        self.level = 0
        self.current_xp = 0

        # Character statistics are numbers and resistances are percentages/coefficients
        self.physical_health = {
            # area      health      resistance
            "head":         [100, 1.0],
            "body":         [100, 1.0],
            "right_arm":    [100, 1.0],
            "left_arm":     [100, 1.0],
            "right_leg":    [100, 1.0],
            "left_leg":     [100, 1.0],
        }

    def take_damage(self, damage, area):
        for pkey, pstat in self.physical_health():
            for i in area:
                if pkey == area:
                    pstat[0] = pstat[0] - pstat[1] * damage