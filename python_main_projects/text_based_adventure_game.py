import random
import json

# Class to represent the player
class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []
        self.current_room = 'start'
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def use_item(self, item):
        if item == 'health_potion':
            self.heal(20)
            self.inventory.remove('health_potion')
            print(f"You used a health potion. Your health is now {self.health}.")
        else:
            print(f"You can't use {item}.")

# Class to represent the game world
class Game:
    def __init__(self):
        self.rooms = {
            'start': {'description': 'You are in a small room with a wooden door to the north.', 'exits': {'north': 'room1'}, 'items': ['health_potion']},
            'room1': {'description': 'A dusty old room with a table and a locked door to the east.', 'exits': {'east': 'room2', 'south': 'start'}, 'items': ['sword']},
            'room2': {'description': 'A dark and eerie room, filled with the scent of decay.', 'exits': {'west': 'room1'}, 'items': []}
        }
        self.enemies = {
            'room1': {'name': 'Goblin', 'health': 30, 'attack': 5, 'defense': 2},
            'room2': {'name': 'Zombie', 'health': 50, 'attack': 8, 'defense': 5}
        }
        self.player = None
        self.game_state = {}

    def start_game(self):
        print("Welcome to the Text-Based Adventure Game!")
        name = input("Enter your character's name: ")
        self.player = Player(name, health=100, attack=10, defense=5)
        self.load_game_state()

    def describe_room(self):
        room = self.rooms[self.player.current_room]
        print("\n" + room['description'])
        if room['items']:
            print("Items in this room: " + ', '.join(room['items']))
    
    def show_inventory(self):
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory: " + ', '.join(self.player.inventory))
    
    def move(self, direction):
        current_room = self.player.current_room
        if direction in self.rooms[current_room]['exits']:
            self.player.current_room = self.rooms[current_room]['exits'][direction]
            print(f"You moved {direction}.")
            self.describe_room()
        else:
            print("You can't go that way.")
    
    def encounter_enemy(self):
        enemy_name = self.enemies.get(self.player.current_room, None)
        if not enemy_name:
            print("There are no enemies here.")
            return
        
        print(f"A wild {enemy_name['name']} appears!")
        print(f"Enemy Health: {enemy_name['health']}")
        
        # Simple combat loop
        while enemy_name['health'] > 0 and self.player.health > 0:
            action = input("What will you do? (Attack/Use item): ").lower()
            
            if action == 'attack':
                damage = self.player.attack - enemy_name['defense']
                if damage > 0:
                    enemy_name['health'] -= damage
                    print(f"You attack the {enemy_name['name']} for {damage} damage.")
                else:
                    print("Your attack was too weak!")
                
                if enemy_name['health'] > 0:
                    enemy_damage = enemy_name['attack'] - self.player.defense
                    if enemy_damage > 0:
                        self.player.take_damage(enemy_damage)
                        print(f"The {enemy_name['name']} attacks you for {enemy_damage} damage!")
                    else:
                        print(f"The {enemy_name['name']}'s attack was too weak!")
                
            elif action == 'use item':
                self.show_inventory()
                item = input("Enter the item you want to use: ").lower()
                if item in self.player.inventory:
                    self.player.use_item(item)
                else:
                    print("You don't have that item.")
            else:
                print("Invalid action. Please choose 'Attack' or 'Use item'.")
        
        if self.player.health <= 0:
            print("You have died. Game Over!")
            self.save_game_state()
            return False
        
        print(f"You defeated the {enemy_name['name']}!")
        return True

    def save_game_state(self):
        self.game_state = {
            'player': {
                'name': self.player.name,
                'health': self.player.health,
                'attack': self.player.attack,
                'defense': self.player.defense,
                'inventory': self.player.inventory,
                'current_room': self.player.current_room
            }
        }
        with open('savegame.json', 'w') as save_file:
            json.dump(self.game_state, save_file)
        print("Game saved!")

    def load_game_state(self):
        try:
            with open('savegame.json', 'r') as save_file:
                self.game_state = json.load(save_file)
                player_data = self.game_state['player']
                self.player = Player(player_data['name'], player_data['health'], player_data['attack'], player_data['defense'])
                self.player.inventory = player_data['inventory']
                self.player.current_room = player_data['current_room']
                print("Game loaded!")
        except FileNotFoundError:
            print("No saved game found. Starting a new game.")

    def game_loop(self):
        while self.player.health > 0:
            self.describe_room()
            action = input("\nWhat would you like to do? (Move/Inventory/Save/Exit): ").lower()
            
            if action == 'move':
                direction = input("Which direction? (north/south/east/west): ").lower()
                self.move(direction)
            
            elif action == 'inventory':
                self.show_inventory()
            
            elif action == 'save':
                self.save_game_state()
            
            elif action == 'exit':
                print("Goodbye!")
                break
            
            else:
                print("Invalid action. Please choose 'Move', 'Inventory', 'Save', or 'Exit'.")

            if self.player.current_room in self.enemies:
                if not self.encounter_enemy():
                    break

        if self.player.health <= 0:
            print("Game Over!")
            return

# Main function to run the game
def main():
    game = Game()
    game.start_game()
    game.game_loop()

if __name__ == '__main__':
    main()
