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
        self.__health__     = health
        self.__defence__    = defence
        self.__strength__   = strength
        self.__steps__      = steps
        self.__alive__      = True
        self.__pos__        = [0,0]


    def monster_attack(self) -> int:
        """
        name: monster_attack
        description: The method handles the attack of the monster. 
        return: The amount of attack the monster perform.
        """
        return self.__strength__


    def take_dmg(self, dmg) -> int:
        """
        name: take_dmg
        description: subtract the attack from the remaining health. 
        param: dmg: the dmg givin
        return: self.__health__ : the remaining health
        """
        if dmg > self.__defence__:
            self.__health__ -= (dmg - self.__defence__)

        if self.__health__ < 0:
            self.__health__ = 0
            self.__alive__ = False

        return self.__health__

    def monster_move(self, pos) -> list:
        """
        name: monster_move
        description: take det monsters position, and add the movement to that position. 
        Make a check to see if the ammount of steps is allowed. 
        param: pos: the position of the monster
        return: self.pos: the new position of the monster. 
        """
        int_step = 0
        list_tmp : list[int, int] = []
        
        for i in range(0,len(pos)):
            list_tmp.append(0)
            int_step += pos[i]
            list_tmp[i] = pos[i] + self.__pos__[i]
            if list_tmp[i] < 0: 
                list_tmp[i] = 0
            
        if int_step <= self.__steps__:
            self.__pos__ = list_tmp

        
        return self.__pos__

    def is_alive(self) -> bool:
        """
        name: is_alive
        description: Check if the hero is still alive. 
        param: none:
        return: self.alive: return true or false, wether or not it is alive. 
        """
        return self.__alive__

    def get_stat(self) -> dict:
        """
        name: get_stat()
        description: return the stat of the monster. 
        param: none:
        return: stat: dictionary with the stats. 
        """
        dict_stat = {
            "Health": self.__health__,
            "Attack": self.__strength__,
            "Defence": self.__defence__,
            "Steps": self.__steps__,
            "Position": self.__pos__
        }

        return dict_stat


if __name__ == "__main__":
    dracula = Monster(5,2,5,5)
    print(dracula.monster_move([1,1]))
    print(dracula.take_dmg(8))
    print(dracula.is_alive())
    print(dracula.get_stat())