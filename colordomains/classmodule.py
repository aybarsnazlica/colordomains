class BFactorRange:
    def __init__(self, num_domains, ranges_list):
        self.num_domains = num_domains
        self.ranges_list = ranges_list

    def __repr__(self) -> str:
        return f"{self.num_domains} domains with indices: {self.ranges_list}"

    def __create_ranges(self):
        min, max = 20, 90
        diff = max - min  # from 20% to 90%
        incr = diff / (self.num_domains - 1)
        b_fact = list(range(min, max + 1, int(incr)))
        return [f"{b}.00" for b in b_fact]

    def to_table(self):
        return dict(zip(self.ranges_list, self.__create_ranges()))
