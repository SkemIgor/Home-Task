from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        quantity = self.size/6.5 + 0.5
        return quantity

class Suit(Clothes):
    @property
    def fabric_consumption(self):
        quantity = 2 * self.size + 0.3
        return quantity


c = Coat(50)
print(c.fabric_consumption)

s = Suit(178)
print(s.fabric_consumption)
