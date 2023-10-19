class StoryNode:
    def __init__(self, text, choices=None):
        self.text = text
        self.choices = choices if choices else []

    def add_choice(self, choice, target_node):
        self.choices.append((choice, target_node))

class Game:
    def __init__(self, start_node):
        self.current_node = start_node

    def play(self):
        while self.current_node:
            print(self.current_node.text)
            
            if not self.current_node.choices:
                print("The adventure ends here.")
                break
                
            for i, (choice, target) in enumerate(self.current_node.choices, 1):
                print(f"{i}. {choice}")
            
            choice_index = int(input("Choose a number: ")) - 1
            
            if 0 <= choice_index < len(self.current_node.choices):
                _, target_node = self.current_node.choices[choice_index]
                self.current_node = target_node
            else:
                print("Invalid choice. Please select a valid option.")

# Define your story
start = StoryNode("You find yourself in a dark forest. Do you go left or right?")
left_node = StoryNode("You encounter a friendly squirrel.", [("Pet the squirrel", None)])
right_node = StoryNode("You stumble upon a hidden treasure chest.", [("Open the chest", None)])

start.add_choice("Go left", left_node)
start.add_choice("Go right", right_node)

# Create the game
game = Game(start)

# Play the game
game.play()
