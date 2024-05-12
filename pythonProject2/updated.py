import tkinter as tk
from PIL import Image, ImageTk
class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Adventure Game")
        self.geometry("400x300")
        self.current_scene = 'scene1'
        self.score = 0
        self.health = 100

        self.scene_label = tk.Label(self, text="", font=("Arial", 14))
        self.scene_label.pack(pady=10)

        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

        self.choice_entry = tk.Entry(self, width=30, font=("Arial", 14))
        self.choice_entry.pack(pady=10)

        self.choice_button = tk.Button(self, text="Submit", font=("Arial", 14), command=self.submit_choice)
        self.choice_button.pack(pady=10)

        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Arial", 14), fg="white", bg="black")
        self.score_label.pack(pady=15)

        self.health_label = tk.Label(self, text=f"Health: {self.health}", font=("Arial", 14), fg="white", bg="black")
        self.health_label.pack(pady=5)

        self.update_scene()

    def update_scene(self):
        if self.current_scene == 'scene1':
            self.scene_label.config(text="You arrive at the castle gates and find them locked. \nDo you search for a key or try to climb the wall?\n Type 'key' or 'climb'")
            self.show_image("castle.jpg")

        elif self.current_scene == 'scene2':
            self.scene_label.config(
                text="You hear the monster's roar coming from the castle.\nDo you try to sneak past it or prepare to fight?\nType 'sneak' or 'fight'")
            self.show_image("monster.jpg")

        elif self.current_scene == 'scene3':
            self.scene_label.config(
                text="As you enter the castle, you find yourself in a dark and narrow corridor.\nDo you light a torch or try to navigate in the dark\nType 'torch' or 'dark'")
            self.show_image("dark_room.jpg")

        elif self.current_scene == 'scene4':
            self.scene_label.config(
                text="You come across a group of goblins blocking your way. Do you fight them or try to sneak past?\nType 'fight' or 'sneak'")
            self.show_image("goblins.jpg")

        elif self.current_scene == 'scene5':
            self.scene_label.config(
                text="You stumble upon a trap set by the monster. Do you try to disarm it or find a way around it?\nType 'disarm' or 'way around'")
            self.show_image("trap.jpg")

        elif self.current_scene == 'scene6':
            self.scene_label.config(
                text="You reach a dead end in the castle. Do you search for a hidden door or backtrack and try another route\nType 'door' or 'backtrack'")
            self.show_image("hiddendoor.jpg")

        elif self.current_scene == 'scene7':
            self.scene_label.config(
                text="You find yourself face to face with a giant spider. Do you fight it or try to avoid it?\nType 'fight' or 'avoid'")
            self.show_image("giant spider.jpg")

        elif self.current_scene == 'scene8':
            self.scene_label.config(text="You enter a room filled with poisonous gas. Do you hold your breath and try to find a way out or use an item to protect yourself?\nType 'breath' or 'item'")
            self.show_image("poisonous gas.jpg")

        elif self.current_scene == 'scene9':
            self.scene_label.config(
                text="You hear the princess's screams coming from a nearby room. Do you rush in or take a more cautious approach?\nType 'rush' or 'cautious approach'")
            self.show_image("screams.jpg")

        elif self.current_scene == 'scene10':
            self.scene_label.config(
                text="You find yourself in a room filled with traps. Do you try to disarm them or find a way to navigate through them?\nType 'disarm' or 'navigate'")
            self.show_image("traps.jpg")

        elif self.current_scene == 'scene11':
            self.scene_label.config(
                text="You come across a room filled with treasure. Do you take the time to loot it or continue your mission to save the princess?\nType 'loot' or 'continue'")
            self.show_image("treasure.jpg")

        elif self.current_scene == 'scene12':
            self.scene_label.config(
                text="You reach a bridge that leads to the princess's tower. Do you cross it or find another way to reach the tower?\nType 'cross' or 'another way'")
            self.show_image("bridge.jpg")

        elif self.current_scene == 'scene13':
            self.scene_label.config(
                text="You climb up to the top of the tower and find yourself face to face with the monster. Do you engage it in combat or try to find a way to outsmart it?\nType 'combat' or 'outsmart'")
            self.show_image("monster.jpg")

        elif self.current_scene == 'scene14':
            self.scene_label.config(
                text="You manage to defeat the monster but the princess is nowhere to be found. Do you search the tower for her or try to find clues about her whereabouts?\nType 'search' or 'clues'")
            self.show_image("monsterfight.jpg")

        elif self.current_scene == 'scene15':
            self.scene_label.config(
                text="You discover that the princess has been taken to a secret underground chamber. Do you find a way to access the chamber or seek help from others?\nType 'find a way' or 'help'")
            self.show_image("underground chamber.jpg")

        elif self.current_scene == 'scene16':
            self.scene_label.config(
                text="You come across a group of cultists performing a ritual to summon a demon. Do you stop them or continue your search for the princess?\nType 'stop' or 'continue'")
            self.show_image("summon a demon.jpg")

        elif self.current_scene == 'scene17':
            self.scene_label.config(
                text="You find yourself in a maze-like series of tunnels. Do you try to find your way through or find a way to create a map to navigate?\nType 'way through' or 'map'")
            self.show_image("series of tunnels.jpg")

        elif self.current_scene == 'scene18':
            self.scene_label.config(
                text="You finally find the princess, but she's cursed and slowly turning into a monster. Do you find a way to break the curse or risk leaving her behind?\nType 'break the curse' or 'leave'")
            self.show_image("cursed.jpg")

        elif self.current_scene == 'scene19':
            self.scene_label.config(
                text="You successfully broke the spell and saved the Princess. Game Over.")
            self.show_image("broke.jpg")
        elif self.current_scene == 'scene20':
            self.scene_label.config(
                text="You left the princess and headed back home. Game Over.")
            self.show_image("back home.jpg")

            self.choice_entry.pack_forget()
            self.choice_button.pack_forget()
        self.score_label.config(text=f"Score: {self.score}")
        self.health_label.config(text=f"Health: {self.health}")




    def show_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 200))
        photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=photo)
        self.image_label.image = photo



    def submit_choice(self):
        choice = self.choice_entry.get().lower()
        if self.current_scene == 'scene1':
            if choice == 'key':
                self.current_scene = 'scene2'
            elif choice == 'climb':
                self.current_scene = 'scene3'
                self.score += 10
        elif self.current_scene == 'scene2':
            if choice == 'sneak':
                self.current_scene = 'scene4'
                self.score += 10
            elif choice == 'fight':
                self.current_scene = 'scene5'
                self.score += 30
                self.health -=5
        elif self.current_scene == 'scene3':
            if choice == 'torch':
                self.current_scene = 'scene6'
            elif choice == 'dark':
                self.current_scene = 'scene7'
        elif self.current_scene == 'scene4':
            if choice == 'fight':
                self.current_scene = 'scene8'
                self.score += 30
                self.health -= 5
            elif choice == 'sneak':
                self.current_scene = 'scene9'
                self.score += 10
        elif self.current_scene == 'scene5':
            if choice == 'disarm':
                self.current_scene = 'scene10'
                self.score += 10
            elif choice == 'way around':
                self.current_scene = 'scene11'
                self.score += 10
        elif self.current_scene == 'scene6':
            if choice == 'door':
                self.current_scene = 'scene12'
                self.score += 10
            elif choice == 'backtrack':
                self.current_scene = 'scene13'
        elif self.current_scene == 'scene7':
            if choice == 'fight':
                self.current_scene = 'scene14'
                self.score += 30
                self.health -= 5
            elif choice == 'avoid':
                self.current_scene = 'scene15'
                self.score += 10
        elif self.current_scene == 'scene8':
            if choice == 'breath':
                self.current_scene = 'scene16'
                self.score += 10
                self.health -= 5
            elif choice == 'item':
                self.current_scene = 'scene17'
                self.score += 10
        elif self.current_scene == 'scene9':
            if choice == 'rush':
                self.current_scene = 'scene17'
                self.score -= 10
            elif choice == 'cautious approach':
                self.current_scene = 'scene16'
                self.score += 10
        elif self.current_scene == 'scene10':
            if choice == 'disarm':
                self.current_scene = 'scene16'
                self.score += 10
                self.health -= 5
            elif choice == 'navigate':
                self.current_scene = 'scene17'
                self.score += 10
        elif self.current_scene == 'scene11':
            if choice == 'loot':
                self.current_scene = 'scene17'
                self.score -= 10
            elif choice == 'continue':
                self.current_scene = 'scene16'
                self.score += 10
        elif self.current_scene == 'scene12':
            if choice == 'cross':
                self.current_scene = 'scene16'
                self.score += 10
                self.health = 100
            elif choice == 'another way':
                self.current_scene = 'scene17'
                self.score += 10
        elif self.current_scene == 'scene13':
            if choice == 'combat':
                self.current_scene = 'scene17'
                self.score += 30
                self.health -= 5
            elif choice == 'outsmart':
                self.current_scene = 'scene16'
                self.score += 10
        elif self.current_scene == 'scene14':
            if choice == 'search':
                self.current_scene = 'scene16'
                self.score += 10
            elif choice == 'clues':
                self.current_scene = 'scene17'
                self.score += 10
        elif self.current_scene == 'scene15':
            if choice == 'find a way':
                self.current_scene = 'scene17'
                self.score += 10
            elif choice == 'help':
                self.current_scene = 'scene16'
        elif self.current_scene == 'scene16':
            if choice == 'stop':
                self.score -=0
                self.current_scene = 'scene2'
            elif choice == 'continue':
                self.current_scene = 'scene18'
                self.score += 10
        elif self.current_scene == 'scene17':
            if choice == 'way through':
                self.current_scene = 'scene3'
                self.score =0
            elif choice == 'map':
                self.current_scene = 'scene18'
                self.score += 10
        elif self.current_scene == 'scene18':
            if choice == 'break the curse':
                self.current_scene = 'scene19'
                self.score += 20
            elif choice == 'leave':
                self.current_scene = 'scene20'
                self.score = 0

        self.score_label.config(text=f"Score: {self.score}")
        self.health_label.config(text=f"Health: {self.health}")
        self.choice_entry.delete(0, tk.END)
        self.update_scene()


game = AdventureGame()
game.mainloop()