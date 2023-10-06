class Monster:
    """ 
    Name: Monster
    Description: 
    The monster class handles the monster and its attribute. 
    The monster can perform the following action:
    attack
    move. 
    The monster has some attributes wich defines the heath, defence, strength, steps, pos and room size. 
    
    """

    
    def __init__(self, health, defence, strength, steps) -> None:
        """
        name: __init__
        description: The constructor of the monster class. 
        This method initialize the monsters attribute. 
        param:  health: The Health points of the monster
        param: defence: The defence stat of the monster
        param: strength: The strength stat of the monster
        param: steps: The amount of steps the monster can take each turn. 
        """


    def monster_attack(self) -> int:
        """
        name: monster_attack
        description: The method handles the attack of the monster. 
        return: The amount of attack the monster perform.
        """


    def monster_move(self, pos) -> list:
        """
        name: monster_move
        description: take det monsters position, and add the movement to that position. 
        Make a check to see if the ammount of steps is allowed. 
        return: self.pos: the new position of the monster. 
        """

    def is_alive() -> bool:
        """
        name: is_alive
        description: Check if the hero is still alive. 
        param: none:
        return: self.alive: return true or false, wether or not it is alive. 
        """

    def get_stat() -> dict:
        """
        name: get_stat()
        description: return the stat of the monster. 
        param: none:
        return: stat: dictionary with the stats. 
        """