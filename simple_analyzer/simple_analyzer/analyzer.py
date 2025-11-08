class Analyzer:
    def __init__(self):
        self._lst = []

    def add_number(self, x):
        self._lst.append(x)

    def even_count(self):
        return sum(1 for n in self._lst if n % 2 == 0)

    def odd_count(self):
        return sum(1 for n in self._lst if n % 2 != 0)

    def highest_number(self):
        if len(self._lst) == 0:
            return None
        return max(self._lst)

    def increasing_pairs(self):
        count = 0
        for i in range(1, len(self._lst)):
            if self._lst[i] > self._lst[i - 1]:
                count += 1
        return count
