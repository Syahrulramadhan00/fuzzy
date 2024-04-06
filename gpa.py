class GPA:
    def __init__(self, gpa):
        self.gpa = gpa
        self.titik1 = 0
        self.titik2 = 2.2
        self.titik3 = 3.0
        self.titik4 = 3.8

    def low(self):
        if self.gpa >= self.titik1 and self.gpa <= self.titik2:
            return 1
        elif self.gpa > self.titik2 and self.gpa < self.titik3:
            return (self.titik3 - self.gpa) / (self.titik3 - self.titik2)
        else:
            return 0

    def medium(self):
        if self.gpa == self.titik3:
            return 1
        elif self.gpa > self.titik2 and self.gpa < self.titik3:
            return (self.gpa - self.titik2) / (self.titik3 - self.titik2)
        elif self.gpa > self.titik3 and self.gpa < self.titik4:
            return (self.titik4 - self.gpa) / (self.titik4 - self.titik3)
        else:
            return 0

    def high(self):
        if self.gpa >= self.titik3 and self.gpa <= self.titik4:
            return (self.gpa - self.titik3) / (self.titik4 - self.titik3)
        elif self.gpa > self.titik4:
            return 1
        else:
            return 0

