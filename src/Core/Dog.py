class Dog:
    def __init__(self, name, strength):
        self._name = name
        self._strength = strength

    def __str__(self):
        return f"Name: {self.name}\nStrength: {self.strength}"

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength