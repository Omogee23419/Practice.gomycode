class Text:
    def _init_(self, a, b):
        self.a = a
        self.b = b

    def _str_(self):
        return f"Test(a={self.a}, b={self.b})"

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b            