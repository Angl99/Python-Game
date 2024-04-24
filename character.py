from weapon import fists
from weapon import short_bow


class Character:

    # class-level variable: race = "Human"

    def __init__(self, name: str, health: int) -> None:
        # variables inside init are unique to the object or object-level variables
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(
            f"{self.name} dealt {self.weapon.damage} damage to "
            f"{target.name} with {self.weapon.name}"
        )


# Creating a Hero and Enemy subclass which inherits from the Character class
class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)

        self.default_weapon = self.weapon

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: str) -> None:
        super().__init__(name, health)
        self.weapon = short_bow
