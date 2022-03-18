class Cube:
    def __init__(self, l, w, h):
        self.l, self.w, self.h = l, w, h

    @classmethod  # 类方法
    def strand_cube(cls):
        return cls(1, 1, 1)


d = Cube.strand_cube()
