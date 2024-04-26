from character import Hero, Enemy
from weapon import short_bow, iron_sword
import os

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)

enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

while True:
    os.system("clear")
    
    hero.attack(enemy)
    enemy.attack(hero)

    # print(f"Health of {hero.name}: {hero.health}")
    # print(f"Health of {enemy.name}: {enemy.health}")

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
