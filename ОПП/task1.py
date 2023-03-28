# python - объекто - орентированный язык 
# python - и в тоже время  процедурный язык


class Cow():
    def __init__(self, name, weight, sound='my-my'):
        self.weight = weight
        self.sound = sound
        self.name = name

    def eat(self, food):
        self.weight += food    

    def domilk(liter):
        weight -= liter * 0.7            

class Goose():
    def __init__(self, name, weight, sound='cri-cri'):
        self.weight = weight
        self.sound = sound
        self.name = name
    def eat(self, food):
            self.weight += food    

class Sheep():
    def __init__(self, name, weight, sound='be-be'):
        self.weight = weight
        self.sound = sound
        self.name = name
    def eat(self, food):
            self.weight += food    

class Chicken():
    def __init__(self, name, weight, sound='ko-ko', agg=0):
        self.weight = weight
        self.sound = 'ko-ko'
        self.agg = agg
        self.name = name
        
    def eat(self, food):
        self.weight += food
    def takeagg(self, amount):
         self.agg -= amount

class Goat():
    def __init__(self, name, weight, sound='be-be-be'):
        self.weight = weight
        self.sound = 'be-be-be'
        self.name = name
    def eat(self, food):
        self.weight += food

    def domilk(liter):
        weight -= liter * 0.7

class Duck():
    def __init__(self, name, weight, sound='cry-cry'):
        self.weight = weight
        self.sound = sound
        self.name = name
    def eat(self, food):
        self.weight += food

kukareku = Chicken(name='Kukareku',agg=2,weight=12)
koko = Chicken(name='koko',agg=20,weight=10)
Grey = Goose(name='Grey',weight=17)
White = Goose(name='White',weight=19)
Manka = Cow(name='Manka',weight=144)
Barashek = Sheep(name='Barashek',weight=46)
Kudriavy = Sheep(name='Kudriavy',weight=54) 
Horn = Goat(name='Horn',weight=35)
Hooves = Goat(name='Hooves',weight=34)
Kruakva = Duck(name='Kruakva',weight=42)

Grey.eat(10)

# Общий вес
print(f'Общий вес всех животных: {kukareku.weight + koko.weight + Grey.weight + White.weight + Manka.weight + Barashek.weight + Kudriavy.weight + Horn.weight + Hooves.weight + Kruakva.weight}')

#Самое тяжелое животное
allweight = {kukareku.name: kukareku.weight,  koko.name: koko.weight, Grey.name: Grey.weight, White.name: White.weight, Manka.name: Manka.weight, Barashek.name: Barashek.weight, Kudriavy.name: Kudriavy.weight, Horn.name: Horn.weight, Hooves.name: Hooves.weight, Kruakva.name: Kruakva.weight}
print(allweight)
max_weight = max(allweight.values())
final_dict = {k:v for k, v in allweight.items() if v == max_weight}
list_dict = list(final_dict.keys())
print(f'Самое тяжелое животное: {list_dict[0]}')