class Cell:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        r = ""
        if self.val:
            r += f"{self.val}"

        return r

    def __len__(self):
        length = 0
        if self.val:
            length = len(f"{self.val}")
        return length

    def __eq__(self, other):
        return self.val == other.val
