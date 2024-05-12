import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Adventure Game")
        self.geometry("800x600")
        self.resizable(False, False)
        self.images = {}  # Dictionary to store image objects
        self.load_resources()
        self.initialize_game()

    def load_resources(self):
        # This function would ideally load images and any other resources
        # For now, it's empty because we don't have actual paths to images
        pass

    def initialize_game(self):
        # Destroy all widgets if any exist (safe destruction)
        for widget in self.winfo_children():
            widget.destroy()

        # Reset or initialize game state
        self.current_scene = 'scene1'
        self.score = 0
        self.health = 100

        # Create the UI components
        self.create_widgets()
        self.update_scene()

    def create_widgets(self):
        self.scene_label = tk.Label(self, text="", font=("Helvetica", 18), wraplength=760)
        self.scene_label.pack(pady=20, padx=20)

        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

        self.choice_button1 = tk.Button(self, font=("Helvetica", 14), command=lambda: self.process_choice('choice1'))
        self.choice_button1.pack(side=tk.LEFT, expand=True, fill="x", padx=20, pady=20)

        self.choice_button2 = tk.Button(self, font=("Helvetica", 14), command=lambda: self.process_choice('choice2'))
        self.choice_button2.pack(side=tk.RIGHT, expand=True, fill="x", padx=20, pady=20)

        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Helvetica", 14))
        self.score_label.pack(side=tk.LEFT, padx=20, pady=10)

        self.health_label = tk.Label(self, text=f"Health: {self.health}", font=("Helvetica", 14))
        self.health_label.pack(side=tk.RIGHT, padx=20, pady=10)

    def update_scene(self):
        scenes = {
            'scene1': ("You arrive at the castle gates and find them locked. Do you search for a key or try to climb the wall?", 'Search for key', 'Climb the wall', 'scene2', 'scene3'),
            # Add more scenes as needed
        }

        if self.current_scene in scenes:
            text, btn1_text, btn2_text, next1, next2 = scenes[self.current_scene]
            self.scene_label.config(text=text)
            self.choice_button1.config(text=btn1_text, command=lambda: self.process_choice(next1))
            self.choice_button2.config(text=btn2_text, command=lambda: self.process_choice(next2))

    def process_choice(self, next_scene):
        # Update game logic based on choice
        # Example logic (customize according to actual game needs)
        if next_scene == 'scene2':
            self.score += 5
        elif next_scene == 'scene3':
            self.health -= 10

        # Check for game over condition
        if self.health <= 0:
            self.game_over()
        else:
            self.current_scene = next_scene
            self.update_scene()

    def game_over(self):
        response = messagebox.askyesno("Game Over", "You have run out of health! Would you like to restart the game?")
        if response:
            self.initialize_game()
        else:
            self.destroy()

if __name__ == "__main__":
    game = AdventureGame()
    game.mainloop()
