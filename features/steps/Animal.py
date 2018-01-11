class Animal:
    name = ''
    happiness = 0

    def __init__(self, name, happiness):
        self.name = str(name)
        self.happiness = int(happiness)

    def pet(self):
        if (self.happiness < 95):
            self.happiness += 5
        else:
            self.happiness = 100

    def annoy(self):
        if (self.happiness > 5):
            self.happiness -= 5
        else:
            self.happiness = 0

    def speak(self):
        return 'Hello, my name is {}'.format(self.name)
