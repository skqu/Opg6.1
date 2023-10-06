from random import randint
class Room: 
    """
    name: Room
    description:
    class to handle the room. This class, create new rooms, which can be access. 
    The room has a size to it, and bottom left corner is denoted 0,0. 
    To move around in the room, the hero change position relative to 0,0. 
    """


    def __init__(self, size, monsters, hero) -> None:
        """
        Name: constructor
        Description: The constructor for the room. When constructed the room needs a size denoted [0,0] and a list of monsters. 
        param: size: The size of the room. Bottom left corner is 0,0. The size is denoted [x,y]. 
        param: monsters: The monsters which is spawned within the roon. 
        """
        self.spawn(monsters, hero)
        self.__monsters__ = monsters
        self.__hero__ = hero
        self.__size__ = size

    
    def __sizeof__(self) -> list:
        """
        name: sizeof
        description: overwrite sizeof function for the room. 
        return: self.__size__: the size of the room. 
        """
        return self.__size__


    def description(self) -> str:
        """
        Name: description
        description: Random generate a description, of the room. 
        return: description: The final description of the room. 
        """
        desc_size = ""
        int_x = self.__size__[0]
        int_y = self.__size__[1]
        
        for j in range(0, int_y+1):
            desc_size += "\n"
            if (j == 0) or (j == int_y):
                for i in range(0,int_x+1):
                    desc_size += "_"
            else:
                for i in range(0,int_x+1):
                    if (i == 0) or (i == int_x):
                        desc_size += "|"
                    elif self.__hero__:
                        if (self.__hero__.pos[0] == i) and (self.__hero__.pos[1] == j): 
                            desc_size += "H"
                        else:
                            for monster in self.__monsters__:  
                                if (monster.get_stat["pos"][0] == i) and (monster.get_stat["pos"][1] == j): 
                                    desc_size += "M"
                                else:
                                    desc_size += " "
                    else:
                        desc_size += " "    
                        
        return desc_size
        

    def spawn(self, monsters, hero) -> None:
        """
        Name: spawn
        description: spawn monsters in the list. 
        param: monsters: A list containing the monsters. 
        """
        for monster in monsters:
            x_pos = randint(0, self.__size__[0])
            y_pos = randint(0, self.__size__[1])
            monster.monster_move([x_pos, y_pos])    
        
        if hero:
            hero.heroMove([0,0], 0)



if __name__ == "__main__":
    """
    Run Test
    """
    first_floor = Room([20,30],[], [])
    print(first_floor.__sizeof__())
    print(first_floor.description())