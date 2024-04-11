class Predikat:
    def __init__(self, predikat):
        self.predikat = predikat
        self.titik1 = 0
        self.titik2 = 60
        self.titik3 = 70
        self.titik4 = 80
        self.titik5 = 90
        self.titik6 = 100

    def poor(self):
        if self.predikat >= self.titik1 and self.predikat <= self.titik2:
            return 1
        elif self.predikat > self.titik2 and self.predikat < self.titik3:
            return (float)(self.titik3 - self.predikat) / (self.titik3 - self.titik2)
        else:
            return 0
        pass

    def fair(self):
        if self.predikat == self.titik3 :
            return 1
        elif self.predikat > self.titik2 and self.predikat < self.titik3:
            return (float)(self.predikat - self.titik2) / (self.titik3 - self.titik2)
        elif self.predikat > self.titik3 and self.predikat < self.titik4:
            return (float)(self.titik4 - self.predikat) / (self.titik4 - self.titik3)
        else:
            return 0

    def good(self):
        if self.predikat == self.titik4 :
            return 1
        elif self.predikat > self.titik3 and self.predikat < self.titik4:
            return (float)(self.predikat - self.titik3) / (self.titik4 - self.titik3)
        elif self.predikat > self.titik4 and self.predikat < self.titik5:
            return (float)(self.titik5 - self.predikat) / (self.titik5 - self.titik4)
        else:
            return 0

    def very_good(self):
        if self.predikat == self.titik5 :
            return 1
        elif self.predikat > self.titik4 and self.predikat < self.titik5:
            return (float)(self.predikat - self.titik4) / (self.titik5 - self.titik4)
        elif self.predikat > self.titik5 and self.predikat < self.titik6:
            return (float)(self.titik6 - self.predikat) / (self.titik6 - self.titik5)
        else:
            return 0

    def excellent(self):
        if self.predikat >= self.titik5 and self.predikat <= self.titik6:
            return (float)(self.predikat - self.titik5) / (self.titik6 - self.titik5)
        elif self.predikat > self.titik6:
            return 1
        else:
            return 0


