class Pack:
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight
        self.value_per_weight = value / weight
        self.used = False

    def __str__(self):
        return f"Pack(value={self.value}, weight={self.weight}, value_per_weight={self.value_per_weight}, used={self.used})"