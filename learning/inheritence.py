class Parent:
    def run(self):
        print("1. Parent.run entered")
        self.check()                              # ← who does this call?
        print("2. Parent.run leaving")

    def check(self):
        print("   Parent.check OK")


class Child(Parent):
    def run(self):
        print("0. Child.run entered")
        super().run()                             # ← what does this REALLY do?
        print("3. Child.run leaving")

    def check(self):
        print("   Child.check (signature changed!)")


c = Child()
print("object id:", id(c), "class:", type(c).__name__)
print()
c.run()