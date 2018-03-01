class Dog:
    def __init__(self, name, strength):
        self._name = name
        self.strength = strength

    @property
    def name(self):
        return self.__name