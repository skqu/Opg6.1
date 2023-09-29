from hero import hero
import random

# Generate a random integer between a specific range (inclusive)
random_integer = random.randint(1, 10)


hercules = hero.hero()
archillis = hero.hero()

hercules.attack = random.randint(3,5)
hercules.defence = random.randint(1,2)
archillis.attack = random.randint(3,5)
archillis.defence = random.randint(1,2)

while (hercules.health) and (archillis.health):
    h_dmg = hercules.heroAttack()
    archillis.heroDamage(h_dmg)
    a_dmg = archillis.heroAttack()
    hercules.heroDamage(a_dmg)

    print("Hercules took: " + str(a_dmg - hercules.defence) + " damage and has: " + str(hercules.health) + " reamning")
    print("archillis took: " + str(h_dmg - archillis.defence) + " damage and has: " + str(archillis.health) + " reamning")

