class Pet:
    def __init__(self, name):
        """
        Initializes the pet's attributes.
        """
        self.name = name
        self.hunger = 5       # 0 = full, 10 = starving
        self.happiness = 5    # 0 = sad, 10 = very happy
        self.energy = 5       # 0 = exhausted, 10 = energetic

    def feed(self):
        """
        Feed the pet to reduce hunger.
        """
        self.hunger = max(0, self.hunger - 2)
        print(f"{self.name} has been fed!")

    def play(self):
        """
        Play with the pet to increase happiness and reduce energy.
        """
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
        else:
            self.happiness = min(10, self.happiness + 2)
            self.energy -= 2
            print(f"{self.name} had fun playing!")

    def sleep(self):
        """
        Let the pet sleep to restore energy.
        """
        self.energy = min(10, self.energy + 3)
        print(f"{self.name} took a nap and feels refreshed!")

    def update(self):
        """
        Simulates the passage of time by adjusting attributes.
        """
        self.hunger = min(10, self.hunger + 1)
        self.happiness = max(0, self.happiness - 1)
        self.energy = max(0, self.energy - 1)

    def status(self):
        """
        Displays the current status of the pet.
        """
        print(f"\nStatus of {self.name}:")
        print(f"Hunger    : {self.hunger}/10")
        print(f"Happiness : {self.happiness}/10")
        print(f"Energy    : {self.energy}/10\n")

    def is_alive(self):
        """
        Checks if the pet is still alive.
        """
        return self.hunger < 10 and self.energy > 0
