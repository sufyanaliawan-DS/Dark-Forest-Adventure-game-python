
import random


class Room:      #HERE I AM USING CLASS FOR GAME LIKE ENTRY, DESCRIPTON AND EXITS
    def __init__(self, description):
        self.description = description
        self.exits = {}
        self.items = []

    def set_exit(self, direction, neighbour):
        self.exits[direction] = neighbour

    def get_short_description(self):
        return self.description

    def get_long_description(self):
        return f'Location: {self.description}, Exits: {", ".join(self.get_exits())}.'

    def get_exits(self):
        return list(self.exits.keys())

    def enter(self, game):
        pass  # To be overridden in subclass

#THIS IS AN FIRST ROOM WHERE HE PICK THE ITEMS IF NECESSARY
class EquipmentRoom(Room):
    def enter(self, game):
        print(f"\nWelcome, {game.player_name}, to the Dark Forest Adventure!")
        print("You are at the entrance of the forest. You see various items that might be useful on your adventure.")
        items = ["Knife", "Energy Drink", "Jacket", "Money", "Key"]
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item}")
            self.items.append(item)
        print(f"{len(items) + 1}. Leave the room")

        while True:
            choice = input("Choose an item to collect (1-{}) or leave ({}): ".format(len(items), len(items) + 1))
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(items):
                    item = items[choice - 1]
                    if item not in game.equipment:
                        game.equipment.append(item)
                        self.items.remove(item)
                        print(f"You collected {item}.")
                    else:
                        print(f"You already have {item}.")
                elif choice == len(items) + 1:
                    print("You leave the room.")
                    break
                else:
                    print("Invalid choice. Try again.")
            else:
                print("Please enter a number.")

#THIS CODE IS TREES CHAMBER ROOM WHERE PERSON WILL PLAY MATH PUZZLE GAME
class TreesChamber(Room):
    def enter(self, game):
        print("\nYou find yourself in a chamber surrounded by tall trees.")
        print("Before you stands a large gate.")

        # Random math puzzle
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2

        while True:
            try:
                user_answer = int(input(f"What is {num1} + {num2}? "))
                if user_answer == correct_answer:
                    print("Correct! You solved the puzzle.")
                    game.equipment.extend(['Oxygen Cylinder', 'Life Jacket'])
                    print("You find swimming equipment and add it to your gear.")
                    break
                else:
                    print("Incorrect. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # SOME TIME IT WILL COLLECT THINGS OR SOMETIME NOT
        self.items.append("Torch")
        self.items.append("Map")
        print("You also find a Torch and a Map in the chamber.")

#HERE FOR CROSSING RIVER WILL PICK EQUIPMENT
class RiverRoom(Room):
    def enter(self, game):
        print("\nYou've reached the river side.")

        if 'Life Jacket' in game.equipment and 'Oxygen Cylinder' in game.equipment:
            print("You have the necessary equipment (Life Jacket and Oxygen Cylinder) to swim across the river.")
            while True:
                swim_choice = input("Do you want to swim across the river? (yes/no): ").strip().lower()
                if swim_choice == "yes":
                    print("You swim across the river safely.")
                    break
                elif swim_choice == "no":
                    print("You decide not to swim across the river.")
                    break
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
        else:
            print("You don't have the necessary equipment to swim across the river.")

        # Add items to the room
        self.items.append("Boat")
        self.items.append("Fishing Rod")
        print("You also find a Boat and a Fishing Rod by the river.")


class CaveRoom(Room):
    def enter(self, game):
        print("\nYou enter a dark cave. It's getting colder, and your energy is draining.")

        # THIS IS THE SCEOND MATH PUZZLE
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2

        while True:
            try:
                user_answer = int(input(f"What is {num1} x {num2}? "))
                if user_answer == correct_answer:
                    print("Correct! You solved the puzzle.")
                    break
                else:
                    print("Incorrect. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print("You must drop all items from your equipment and drink the Energy Drink to regain your strength.")

        if 'Energy Drink' in game.equipment:
            game.equipment = []  # IF NEED DROP ALL ITEMS
            print("You drop all items from your equipment and drink the Energy Drink.")
            print("You feel refreshed and regain your strength.")

            # Add new items to equipment
            game.equipment.extend(['Mountain Shoes', 'Rope'])
            print("You find Mountain Shoes and a Rope to help you climb the mountain.")
        else:
            print("You don't have an Energy Drink to regain your strength.")

        # Add items to the room
        self.items.append("Crystal")
        self.items.append("Pickaxe")
        print("You also find a Crystal and a Pickaxe in the cave.")

#THIS IS MOUNTAIN ROOM HERE PERSON WILL CLIMB IT OR DIRECTLY TO ANOTHER ROOM NO GAME HERE
class MountainRoom(Room):
    def enter(self, game):
        print("\nYou approach the mountain side. It's a steep climb, but you have Mountain Shoes and a Rope.")

        if 'Mountain Shoes' in game.equipment and 'Rope' in game.equipment:
            print("You use your Mountain Shoes and Rope to safely climb the mountain.")
        else:
            print("You don't have the necessary equipment to climb the mountain.")

        # Add items to the room
        self.items.append("Climbing Gear")
        self.items.append("Mountain Guide Book")
        print("You also find Climbing Gear and a Mountain Guide Book on the mountain.")


class LabyrinthRoom(Room):
    def enter(self, game):
        print("\nYou enter an underground labyrinth. It's a maze with multiple paths.")
        print("One path leads to the Secret Chamber, but you need to answer a question to find the right way.")
#THIS IS AN THIRD GAME TO SELECT RIGHT PATH
        countries_capitals = {
            "France": "Paris",
            "Germany": "Berlin",
            "Italy": "Rome",
            "Spain": "Madrid",
            "Japan": "Tokyo",
        }

        random_country = random.choice(list(countries_capitals.keys()))
        correct_capital = countries_capitals[random_country]

        while True:
            capital_guess = input(f"What is the capital of {random_country}? ").strip()
            if capital_guess.lower() == correct_capital.lower():
                print("Correct! You've found the correct path to the Secret Chamber.")
                break
            else:
                print("That's not the correct capital. Try again.")

        # Add items to the room
        self.items.append("Compass")
        self.items.append("Notebook")
        print("You also find a Compass and a Notebook in the labyrinth.")

#HERE HE HAS TWO TO THREE OPTION FOR SELECT THE RIGHT PATH
class SecretChamber(Room):
    def enter(self, game):
        print("\nYou find a mysterious chamber. It's a junction with three different paths.")
        print("One path leads to the Dark Secret Room, another to the Exit Room, and the third is a dead end.")

        while True:
            chosen_path = input("Choose your path (Dark Secret Room / Exit Room / Dead End): ").strip().lower()
            if chosen_path.lower() == "dark secret room":
                print("You choose the path to the Dark Secret Room.")
                break
            elif chosen_path.lower() == "exit room":
                print("You choose the path to the Exit Room.")
                break
            elif chosen_path.lower() == "dead end":
                print("You choose the dead end path, but there's nothing here.")
                break
            else:
                print("Invalid choice. Try again.")


class DarkSecretRoom(Room):
    def enter(self, game):
        print("\nYou enter a dark secret room. It's pitch black inside.")
        print("You hear a strange sound, and red rays of light start scanning the room.")

        # FOURTH GAME  game: Riddle
        print("A voice echoes in the room:")
        print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind.")
        print("What am I?")

        answer = "an echo"

        while True:
            riddle_attempt = input("Your answer: ").strip().lower()
            if riddle_attempt == answer:
                print("Congratulations! The room begins to brighten, and a hidden passage is revealed.")
                break
            else:
                print("The room remains shrouded in darkness. Try again.")

        # Add items to the room
        self.items.append("Enchanted Gem")
        self.items.append("Crystal Ball")
        print("You also find an Enchanted Gem and a Crystal Ball in the dark secret room.")


class EnchantedForest(Room):
    def enter(self, game):
        print("\nYou enter an enchanted forest with glowing trees and magical creatures.")
        print("The air is filled with a sense of wonder and mystery.")

        # Add items to the room
        self.items.append("Fairy Dust")
        self.items.append("Magic Amulet")
        print("You also find Fairy Dust and a Magic Amulet in the enchanted forest.")


class AbandonedHut(Room):
    def enter(self, game):
        print("\nYou discover an abandoned hut hidden deep within the forest.")
        print("The hut is old and covered in vines, but there might be something valuable inside.")

        # Add items to the room
        self.items.append("Ancient Book")
        self.items.append("Golden Key")
        print("You also find an Ancient Book and a Golden Key inside the abandoned hut.")

#LAST PART OF GAME WHERE HE CAN EXIT GAME WITHOUT SUCCES OR COMPLETED MISSION
class ExitRoom(Room):
    def enter(self, game):
        print("\nCongratulations, {}! You've completed your adventure. You can exit the forest now.".format(
            game.player_name))
        print("Mission accomplished!")


class Game:
    def __init__(self):
        self.create_rooms()
        self.current_room = self.starting_room
        self.equipment = []
        self.player_name = ""
#LIST OF ALL ROOMS HERE
    def create_rooms(self):
        self.starting_room = EquipmentRoom("You are at the entrance of the forest.")
        self.trees_chamber = TreesChamber("You find yourself in a chamber surrounded by tall trees.")
        self.river_room = RiverRoom("You've reached the river side.")
        self.cave_room = CaveRoom("You enter a dark cave.")
        self.mountain_room = MountainRoom("You approach the mountain side.")
        self.labyrinth_room = LabyrinthRoom("You enter an underground labyrinth.")
        self.secret_chamber = SecretChamber("You find a mysterious chamber.")
        self.dark_secret_room = DarkSecretRoom("You enter a dark secret room.")
        self.enchanted_forest = EnchantedForest("You enter an enchanted forest.")
        self.abandoned_hut = AbandonedHut("You discover an abandoned hut.")
        self.exit_room = ExitRoom("Congratulations! You've completed your adventure. You can exit the forest now.")

        # Set EXITS OF EACH ROOM 
        self.starting_room.set_exit("north", self.trees_chamber)
        self.trees_chamber.set_exit("south", self.starting_room)
        self.trees_chamber.set_exit("west", self.river_room)
        self.river_room.set_exit("east", self.trees_chamber)
        self.cave_room.set_exit("south", self.trees_chamber)
        self.trees_chamber.set_exit("north", self.cave_room)
        self.trees_chamber.set_exit("east", self.mountain_room)
        self.mountain_room.set_exit("west", self.trees_chamber)
        self.trees_chamber.set_exit("south", self.labyrinth_room)
        self.labyrinth_room.set_exit("north", self.trees_chamber)
        self.labyrinth_room.set_exit("west", self.secret_chamber)
        self.secret_chamber.set_exit("east", self.dark_secret_room)
        self.secret_chamber.set_exit("north", self.enchanted_forest)
        self.enchanted_forest.set_exit("south", self.secret_chamber)
        self.enchanted_forest.set_exit("west", self.abandoned_hut)
        self.abandoned_hut.set_exit("east", self.enchanted_forest)
        self.dark_secret_room.set_exit("west", self.exit_room)

    def play(self):
        self.player_name = input("Enter your name: ")
        print(f"\nWelcome, {self.player_name}, to the Dark Forest Adventure!")

        while True:
            print(self.current_room.get_long_description())
            command = input("Choose your action or direction to move: ").lower().strip()
            if command in self.current_room.get_exits():
                self.move_to(command)
            else:
                print("Invalid action or direction.")

    def move_to(self, direction):
        next_room = self.current_room.exits.get(direction)
        if next_room:
            self.current_room = next_room
            self.current_room.enter(self)
        else:
            print("You can't go that way.")


if __name__ == "__main__":
    game = Game()
    game.play()
