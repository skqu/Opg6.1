class Room: 
    """
    name: Room
    description:
    class to handle the room. This class, create new rooms, which can be access. 
    The room has a size to it, and bottom left corner is denoted 0,0. 
    To move around in the room, the hero change position relative to 0,0. 
    """


    def __init__(self, size, monsters) -> None:
        """
        Name: constructor
        Description: The constructor for the room. When constructed the room needs a size denoted [0,0] and a list of monsters. 
        param: size: The size of the room. Bottom left corner is 0,0. The size is denoted [x,y]. 
        param: monsters: The monsters which is spawned within the roon. 
        """


    def description(self) -> str:
        """
        Name: description
        description: Random generate a description, of the room. 
        return: description: The final description of the room. 
        """

    def spawn(self, monsters) -> None:
        """
        Name: spawn
        description: spawn monsters in the list. 
        param: monsters: A list containing the monsters. 
        """



if __name__ == "__main__":
    """
    Run Test
    """