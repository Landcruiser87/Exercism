import random
import string

class Robot:
    def __init__(self):
        self.name = self.generate_name()
    def reset(self):
        self.name = self.generate_name()
    def generate_name(self):
        random.seed()
        name = ""
        for i in range(2):
            name += random.choice(string.ascii_uppercase)
        for i in range(3):
            name += random.choice(string.digits)
        return name
