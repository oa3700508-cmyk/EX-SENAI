class Animal:
    def __init__(self, name):
        self.name = name
    def fazer_som(self):
        return "..."

class Cachorro(Animal):
        def fazer_som(self):
            return f"{self.name} diz: Au Au!"

class Gato(Animal):
        def fazer_som(self):
            s = super().fazer_som()
            return f"{self.name}: Miau! ({s})"

animais = [Cachorro("Rex"), Gato("Yuumi")]
for a in animais:
     print(a.fazer_som())            