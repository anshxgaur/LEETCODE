from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height) - 4
        self.pos = 0
        self.moved = False  # to handle edge case

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        p = self.pos

        if p < self.w:
            return [p, 0]
        p -= self.w

        if p < self.h - 1:
            return [self.w - 1, p + 1]
        p -= (self.h - 1)

        if p < self.w - 1:
            return [self.w - 2 - p, self.h - 1]
        p -= (self.w - 1)

        return [0, self.h - 2 - p]

    def getDir(self) -> str:
        if not self.moved:
            return "East"

        p = self.pos

        if p == 0:
            return "South"  # special case

        if p < self.w:
            return "East"
        p -= self.w

        if p < self.h - 1:
            return "North"
        p -= (self.h - 1)

        if p < self.w - 1:
            return "West"

        return "South"
