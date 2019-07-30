class CharacterCount:
    def __init__(self, x):  # constructor of class
        self.x = x

    def setVal(self, x: str):
        self.x = x

    def countChars(self):
        count = 0
        for c in self.x:
            if c is not ' ':  # ignore spaces
                count += 1
        return count


c = CharacterCount('welcome to Python')
c.setVal('Welcome to Python')
print(c.countChars())
