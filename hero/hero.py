class hero:
    """
    This is the hero class which define how the hero is defined. 
    This hero can pickup loot item from the monster, take damage and do on off defence, attack or move. 
    The hero needs som attributes to define the attack power, defence power, backpack, equipment and health. 
    """
    
    def __init__(self):
        """
        The constructor sets the default value of the hero class, and also add the default items to the backpack. 
        """
        self.equipment = []
        self.health = 20
        self.attack = 0
        self.defence = 0
        self.backpack = ["Rope", "fint and steel", "candle"]
        self.stand = "move"

    def heroPickup(self, item):
        """
        This is method for picking up items from the ground. 
        The items, that are collected, is placed in the backpack. 
        There is only room for ten items in the backpack. 

        param: item: string containing the information about the item dropped
        return: amount: the amount of item in the backpack.
        """
        if len(self.backpack) < 11:
            self.backpack.append(item)
        
        return len(self.backpack)

    def heroDamage(self, damage):
        """
        The damage method, is used for the hero to take damage. 
        If the damage is greate or equal to remaining health, the hero is dead. 
        
        param: damage: The amount of damage inflicted on hero. 
        return: health: The remaining health of the hero. 
        """
        if damage < self.health:
            self.health -= (damage -self.defence)
        else:
            self.health = 0
        
        return self.health

    def heroDefence(self):
        """
        Hero take defence stannds and boost defence stats by 1.5 times the hero stat, 
        but the hero also reduced the amount of attack by 0.5 times the hero stat.

        """
        if self.stand != "defence":
            self.attack = 0.5 * self.attack
            self.defence = 1.5 * self.attack
            self.stand = "defence"


    def heroAttack(self):
        """
        Hero perform attack. 

        return: amount: the amount of total attack
        """
        return self.attack

    def heroMove(self, pos, dir, steps):
        """
        Move the hero around the board.
        The board is made of 2d grid pattern described in a list [x,y]. 
        l is the same as minus x
        r is the same as x
        u is the same as y
        d is the same as minus y

        param: pos: The current possint in the 2d grid.
        param: dir: The direction of movement, l, r, u, d
        param: steps: The amount of steps to perform the movement. 
        return: pos: the new position in 2d grid. 
        """
        
        if dir == "l":
            steps = steps * -1
            pos[0] += steps
        elif dir == "r":
            pos[0] += steps
        elif dir == "d":
            steps = steps * -1
            pos[1] += steps
        elif dir == "u":
            pos[1] += steps

        return pos
        

if __name__ == "__main__":
    hercules = hero()
    print(hercules.heroMove([5,5], "d", 1))