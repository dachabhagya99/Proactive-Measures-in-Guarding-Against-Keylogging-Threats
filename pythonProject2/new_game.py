import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Adventure Game")
        self.geometry("800x600")  # Larger size for better layout
        self.resizable(False, False)  # Disable resizing

        self.current_scene = 'scene1'
        self.score = 0
        self.health = 100
        self.images = {}  # To hold preloaded images

        self.load_resources()
        self.create_widgets()
        self.update_scene()

    def initialize_game(self):
        # Reset game state variables
        self.current_scene = 'scene1'
        self.score = 0
        self.health = 100

        # Clear and re-add widgets
        for widget in self.winfo_children():
            widget.destroy()
    def load_resources(self):
        # This function should ideally load all resources needed for the game
        pass

    def create_widgets(self):
        self.config(bg="#333")
        self.scene_label = tk.Label(self, text="", font=("Helvetica", 20), wraplength=760, bg="#333", fg="white")
        self.scene_label.pack(pady=(20, 10), padx=20, fill="x")

        self.image_label = tk.Label(self, bg="#333")
        self.image_label.pack(pady=20)

        self.choice_button1 = tk.Button(self, font=("Helvetica", 16), bg="#1177DD", fg="white",
                                        relief="flat", activebackground="#5599FF", activeforeground="white",
                                        command=self.submit_choice1)
        self.choice_button1.pack(side=tk.LEFT, fill="x", expand=True, padx=(20, 10), pady=20)

        self.choice_button2 = tk.Button(self, font=("Helvetica", 16), bg="#DD1111", fg="white",
                                        relief="flat", activebackground="#FF5555", activeforeground="white",
                                        command=self.submit_choice2)
        self.choice_button2.pack(side=tk.RIGHT, fill="x", expand=True, padx=(10, 20), pady=20)

        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Helvetica", 14), fg="white", bg="#555")
        self.score_label.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)

        self.health_label = tk.Label(self, text=f"Health: {self.health}", font=("Helvetica", 14), fg="white", bg="#555")
        self.health_label.pack(side=tk.RIGHT, padx=10, pady=10, fill="x", expand=True)

    def update_scene(self):
        scenes = {
            'scene1': ("You arrive at the castle gates and find them locked. "
                       "Do you search for a key or try to climb the wall?", 'key', 'climb', 'scene2', 'scene3'),
            'scene2': ("You hear the monster's roar coming from the castle. "
                       "Do you try to sneak past it or prepare to fight?", 'sneak', 'fight', 'scene4', 'scene5'),
            'scene3': ("As you enter the castle, you find yourself in a dark and narrow corridor. "
                       "Do you light a torch or try to navigate in the dark?", 'torch', 'dark', 'scene6', 'scene7'),
            'scene4': ("You come across a group of goblins blocking your way. "
                       "Do you fight them or try to sneak past?", 'fight', 'sneak', 'scene8', 'scene9'),
            'scene5': ("You stumble upon a trap set by the monster. "
                       "Do you try to disarm it or find a way around it?", 'disarm', 'way around', 'scene10', 'scene11'),
            'scene6': ("You reach a dead end in the castle. "
                       "Do you search for a hidden door or backtrack and try another route?", 'door', 'backtrack', 'scene12', 'scene13'),
            'scene7': ("You find yourself face to face with a giant spider. Do you fight it or try to avoid it?", 'fight', 'avoid', 'scene14', 'scene15'),
            'scene8': ("You enter a room filled with poisonous gas. "
                       "Do you hold your breath and try to find a way out or use an item to protect yourself?", 'breath', 'item', 'scene16', 'scene17'),
            'scene9': ("You hear the princess's screams coming from a nearby room. Do you rush in or take a more cautious approach?", 'rush', 'cautious approach', 'scene17', 'scene16'),
            'scene10': ("You find yourself in a room filled with traps. "
                        "Do you try to disarm them or find a way to navigate through them?", 'disarm', 'navigate', 'scene16', 'scene17'),
            'scene11': ("You come across a room filled with treasure. "
                        "Do you take the time to loot it or continue your mission to save the princess?", 'loot', 'continue', 'scene17', 'scene16'),
            'scene12': ("You reach a bridge that leads to the princess's tower. "
                        "Do you cross it or find another way to reach the tower?", 'cross', 'another way', 'scene16', 'scene17'),
            'scene13': ("You climb up to the top of the tower and find yourself face to face with the monster."
                        " Do you engage it in combat or try to find a way to outsmart it?", 'combat', 'outsmart', 'scene17', 'scene16'),
            'scene14': ("You manage to defeat the monster but the princess is nowhere to be found. "
                        "Do you search the tower for her or try to find clues about her whereabouts?", 'search', 'clues', 'scene16', 'scene17'),
            'scene15': ("You discover that the princess has been taken to a secret underground chamber. "
                        "Do you find a way to access the chamber or seek help from others?", 'find a way', 'help', 'scene17', 'scene16'),
            'scene16': ("You come across a group of cultists performing a ritual to summon a demon. "
                        "Do you stop them or continue your search for the princess?", 'stop', 'continue', 'scene2', 'scene18'),
            'scene17': ("You find yourself in a maze-like series of tunnels. "
                        "Do you try to find your way through or find a way to create a map to navigate?", 'way through', 'map', 'scene3', 'scene18'),
            'scene18': ("You finally find the princess, but she's cursed and slowly turning into a monster. "
                        "Do you find a way to break the curse or risk leaving her behind?", 'break the curse', 'leave', 'scene19', 'scene20'),
            'scene19': ("You successfully broke the spell and saved the Princess. Game Over.", '', '', '', ''),
            'scene20': ("You left the princess and headed back home. Game Over.", '', '', '', '')
        }

        if self.current_scene in scenes:
            text, btn1_text, btn2_text, next_scene1, next_scene2 = scenes[self.current_scene]
            self.scene_label.config(text=text)
            self.choice_button1.config(text=btn1_text, state=tk.NORMAL if btn1_text else tk.DISABLED)
            self.choice_button2.config(text=btn2_text, state=tk.NORMAL if btn2_text else tk.DISABLED)
            self.choice_button1.next_scene = next_scene1
            self.choice_button2.next_scene = next_scene2
            self.show_image(f"images/{self.current_scene}.jpg")
        else:
            self.choice_button1.pack_forget()
            self.choice_button2.pack_forget()

        self.score_label.config(text=f"Score: {self.score}")
        self.health_label.config(text=f"Health: {self.health}")

    def show_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((300, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except IOError:
            print(f"Error: Unable to load image {image_path}")

    def submit_choice1(self):
        self.process_choice(self.choice_button1.next_scene)

    def submit_choice2(self):
        self.process_choice(self.choice_button2.next_scene)

    def process_choice(self, next_scene):
        # Scoring and health impact for each scene decision
        if self.current_scene == 'scene1':
            if next_scene == 'scene3':  # Climbing the wall
                self.score += 10
                self.health -= 10  # Risky to climb, might get hurt
            elif next_scene == 'scene2':  # Searching for a key
                self.score += 5  # Safer but slower option

        elif self.current_scene == 'scene2':
            if next_scene == 'scene4':  # Sneaking past the monster
                self.score += 15
            elif next_scene == 'scene5':  # Preparing to fight
                self.score += 20
                self.health -= 15  # Fighting is risky

        elif self.current_scene == 'scene3':
            if next_scene == 'scene6':  # Lighting a torch
                self.score += 5
            elif next_scene == 'scene7':  # Navigating in the dark
                self.score += 10
                self.health -= 5  # Risk of stumbling or getting lost

        elif self.current_scene == 'scene4':
            if next_scene == 'scene8':  # Fight goblins
                self.score += 20
                self.health -= 10
            elif next_scene == 'scene9':  # Sneak past
                self.score += 15

        elif self.current_scene == 'scene5':
            if next_scene == 'scene10':  # Disarm the trap
                self.score += 25
                self.health -= 20
            elif next_scene == 'scene11':  # Find a way around
                self.score += 10

        elif self.current_scene == 'scene6':
            if next_scene == 'scene12':  # Search for a hidden door
                self.score += 15
            elif next_scene == 'scene13':  # Backtrack
                self.score += 5

        elif self.current_scene == 'scene7':
            if next_scene == 'scene14':  # Fight the spider
                self.score += 20
                self.health -= 25
            elif next_scene == 'scene15':  # Avoid the spider
                self.score += 10

        elif self.current_scene == 'scene8':
            if next_scene == 'scene16':  # Hold breath
                self.score += 10
            elif next_scene == 'scene17':  # Use item
                self.score += 5
                self.health += 10  # Gaining health due to protective measures

        elif self.current_scene == 'scene9':
            if next_scene == 'scene17':  # Rush in
                self.score += 20
                self.health -= 10
            elif next_scene == 'scene16':  # Cautious approach
                self.score += 15

        elif self.current_scene == 'scene10':
            if next_scene == 'scene16':  # Disarm traps
                self.score += 30
                self.health -= 15
            elif next_scene == 'scene17':  # Navigate through
                self.score += 20

        elif self.current_scene == 'scene11':
            if next_scene == 'scene17':  # Loot treasure
                self.score += 25
            elif next_scene == 'scene16':  # Continue mission
                self.score += 10

        elif self.current_scene == 'scene12':
            if next_scene == 'scene16':  # Cross the bridge
                self.score += 20
                self.health -= 10  # The bridge may be risky
            elif next_scene == 'scene17':  # Find another way
                self.score += 15

        elif self.current_scene == 'scene13':
            if next_scene == 'scene17':  # Engage in combat
                self.score += 30
                self.health -= 20
            elif next_scene == 'scene16':  # Outsmart the monster
                self.score += 25

        elif self.current_scene == 'scene14':
            if next_scene == 'scene16':  # Search the tower
                self.score += 15
            elif next_scene == 'scene17':  # Find clues
                self.score += 10

        elif self.current_scene == 'scene15':
            if next_scene == 'scene17':  # Find a way to the chamber
                self.score += 25
            elif next_scene == 'scene16':  # Seek help
                self.score += 20

        elif self.current_scene == 'scene16':
            if next_scene == 'scene2':  # Stop the cultists
                self.score += 40
                self.health -= 10
            elif next_scene == 'scene18':  # Continue search
                self.score += 15

        elif self.current_scene == 'scene17':
            if next_scene == 'scene3':  # Find your way through tunnels
                self.score += 25
                self.health -= 15
            elif next_scene == 'scene18':  # Create a map
                self.score += 20

        elif self.current_scene == 'scene18':
            if next_scene == 'scene19':  # Break the curse
                self.score += 50
                self.health += 10  # Restoring health with magic
            elif next_scene == 'scene20':  # Leave the princess
                self.score += 10
        if self.health <= 0:
            self.game_over()
        self.current_scene = next_scene
        self.update_scene()

    def game_over(self):
        response = messagebox.askyesno("Game Over", "You have died. Would you like to restart the game?")
        if response:
            self.initialize_game()  # Reset the game
        else:
            self.quit()  # Properly close the tkinter window
game = AdventureGame()
game.mainloop()
