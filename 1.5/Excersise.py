class Human:
    def __init__(self, name, height, weight, hobby, beloved_food):
        self.name = name
        self.height =  height
        self.weight = weight
        self.bmi = self.count_bmi()
        self.hobby = hobby
        self.beloved_food = beloved_food

    def speak(self):
        print("I'm telling the truth")

    def count_bmi(self):
        return self.weight /((self.height / 100)**2)

    def diff_to_norm(self):
        diff = 0
        if self.bmi >= 25:
            diff = self.weight - 25 * (self.height / 100) * (self.height / 100)
        elif self.bmi < 18.5:
            diff = 18.5 * (self.height / 100) * (self.height / 100) - self.weight
        return diff

    def save_data(self):
        import json
        with open('.json'.format(self.name), "w") as f:
            f.write(json.dumps({"name": self.name, "height": self.height, "weight": self.weight, "hobby" : self.hobby, "beloved food": self.beloved_food}))

# Zakładając, że aby schudnąć 1 kg trzeba spalić 6000kcal, napisz funkcjonalność, która powie użytkownikowi, ile powinien
# godzin biegać(500kcal/h) / jeździć rowerem(600kcal/h) / uprawiać hobby(250kcal/h) / grać w szachy(150kcal/h) / etc.
# aby być w normie (to_burn).

    def to_burn(self):
        time_to_burn = 0
        if self.bmi < 25:
            return time_to_burn
        kcal_to_burn = self.diff_to_norm() * 6000
        if self.hobby == "biegi":
            time_to_burn = kcal_to_burn / 500
        elif self.hobby == "rower":
            time_to_burn = kcal_to_burn / 600
        elif self.hobby == "hobby":
            time_to_burn = kcal_to_burn / 250
        elif self.hobby == "szachy":
            time_to_burn = kcal_to_burn / 150
        return time_to_burn

    def to_eat(self):
        amount_to_eat = 0
        if self.bmi > 18.5:
            return amount_to_eat
        kcal_to_eat = self.diff_to_norm() * 6000
        if self.beloved_food == "ziemniaki":
            amount_to_eat = kcal_to_eat / 450 * 100
        elif self.beloved_food == "czekolada":
            amount_to_eat = kcal_to_eat / 80 * 100
        return amount_to_eat

    def what_to_do(self):
        if self.bmi < 18.5:
            print("{0} ma niedowagę, jej/jego BMI wynosi {3:.2f}, powinna/powinien przytyć {4:.2f} i w tym celu zjeść {1} w ilości {2:.0f} gramów.".format(self.name, self.beloved_food, self.to_eat(), self.bmi, self.diff_to_norm()))
        elif self.bmi >= 25.0:
            print("{0} ma nadwagę, jej/jego BMI wynosi {3:.2f}, powinna/powinien schudnąć {4:.2f} i w tym celu poświęcić {1:.2f} godzin na {2}.".format(self.name, self.to_burn(), self.hobby, self.bmi, self.diff_to_norm()))
        else:
            print("{0} ma wagę w normie, jej/jego BMI wynosi {1:.2f}".format(self.name, self.bmi))

class Politician(Human):
    bribed = False

    def speak(self):
        if self.bribed:
            super().speak()
        else:
            print("I'm lying because I can")

    def recive_bribe(self):
        self.bribed = True

adam = Human("Adam", 150, 170, "rower", "ziemniaki")
artur = Politician("Artur", 185, 52, "hobby", "czekolada")
zofia = Politician("Zofia", 166, 56, "szachy", "czekolada")
anna = Human("Anna", 166, 80, "gotowanie", "ziemniaki")
artur.recive_bribe()
people = [adam, artur, zofia, anna]
for person in people:
    print(person.name)
    person.save_data()
    person.what_to_do()
