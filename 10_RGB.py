from abc import ABC, abstractmethod

class ComuterColor(ABC):
    @classmethod
    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def __mul__(self, other):
        pass

    @classmethod
    @abstractmethod
    def __rmul__(self, other):
        pass

class Color(ComuterColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        if self.red == other.red and self.green == other.green and self.blue == other.blue:
            return True
        return False

    def __add__(self, other):
        new_red = (self.red + other.red) // 2
        new_green = (self.green + other.green) // 2
        new_blue = (self.blue + other.blue) // 2
        return Color(new_red, new_green, new_blue)

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        contrast_level = - 256 * (1 - c)
        F = 259 * (contrast_level + 255) / (255 * (259 - contrast_level))
        L_red_new = int(F * (self.red - 128) + 128)
        L_green_new = int(F * (self.green - 128) + 128)
        L_blue_new = int(F * (self.blue - 128) + 128)
        new_color = Color(L_red_new, L_green_new, L_blue_new)
        return new_color

    def __rmul__(self, c):
        return self.__mul__(c)

red = Color(255, 0, 0)
redred = Color(255, 0, 0)
red2 = Color(255, 0, 1)
green = Color(0, 255, 0)
print(red)
print(red)
print(red == red2)
print(red == red)
print(red + green)
print([red, redred, red2, green])
print(set([red, redred, red2, green]))
print(red * 0.5)
print(green * 0.678)