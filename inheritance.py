class State:
    def __init__(self, capital):
        self.capital = capital
    def __str__(self):
        return f"{self.capital}"
class Uzbekistan(State):
    def __init__(self, capital, language):
        super().__init__(capital)
        self.language = language
    def Uzbekistan1(self):
        print(self.capital, self.language)
Uzbekistan = Uzbekistan("The capital: Tashkent", "uzbek")

class Azerbaijan(State):
    def __init__(self, capital, language, city):
        super().__init__(capital)
        self.language= language
        self.city = city
    def Azerbaijan1(self):
        print(self.capital, self.language, self.city)
Azerbaijan = Azerbaijan("The capital: Baku", "Azerbaijan language","city: 65")


print(Azerbaijan.Azerbaijan1())
