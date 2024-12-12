class Man:
    def __init__(self, n, s, sx):
        self.name = n
        self.surname = s
        self.sex = sx
    def mylove(self):
        print("Я люблю смотреть телевизор")
    def description(self):
        print("Меня зовут",self.name,self.surname)
person1 = Man("Александр", "Трошин", "мужчина")
person1.description()
person1.mylove()

class Woman(Man):
    def lovent(self):
        print("Я не люблю играть в футбол")
person2 = Woman("Валерия", "Петрова", "женщина")
person2.description()
person2.lovent()
