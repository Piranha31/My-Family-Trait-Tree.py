class FamilyMember:
    def __init__(self, eye_color, height):
        self.eye_color = eye_color
        self.height = height

    def show_traits(self):
        print("eye color: ", self.eye_color)
        print("height: ", self.height)

class kid(FamilyMember):
    def __init__(self, name, age, eye_color, height):
        self.name = name
        self.age = age
        super().__init__(eye_color, height)

    def show_traits(self):
        print("name :", self.name)
        print("age :", self.age)
        super().show_traits()

    def favoriteHobby(self, hobby):
        print(self.name,"s favorite hobby is", hobby)

child = kid("maya", 10, "brown", 140)

child.show_traits()
child.favoriteHobby("Painting")

print("Is kid a subclass of family member ?", issubclass(kid, FamilyMember))
