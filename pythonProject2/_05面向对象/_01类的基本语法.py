class Reget:
    length, width = 0.0, 0.0

    def get_area(self):
        return self.length * self.width


r = Reget()
r.length = 10
r.width = 5
print(r.get_area())