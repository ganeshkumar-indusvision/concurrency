class Animal:
    def speak(self, name):
        return f"...generic sound from {name}"

class Dog(Animal):
    def speak(self, name):
        if name == "Rex":
            return "Woof!"          # child handles this case
        return super().speak(name)  # everything else -> parent





d = Dog()
print(d.speak("Rex"))    # Woof!          <- child's branch
print(d.speak("Tom"))    # ...generic sound from Tom   <- super() branch