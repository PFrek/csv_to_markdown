class Cell:
    def __init__(self, val, none_str=""):
        self.val = val
        self.none_str = none_str

    def __repr__(self):
        if self.val:
            return f"{self.val}"

        return self.none_str

    def __len__(self):
        if self.val:
            return len(f"{self.val}")

        return len(self.none_str)

    def __eq__(self, other):
        return self.val == other.val
