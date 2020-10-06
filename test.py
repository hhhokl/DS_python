class Conv:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        self.syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]
        
    def to_roman(self, num):    
        """
        :param self:
        :param n: int
        :return: str    
        """
        first_part_index = 0
        first_part = 0
        for val_item in self.val:
            if val_item - num < 0 and val_item > first_part:
                first_part = val_item
                first_part_index = self.val.index(val_item)
        second_part = num - first_part
        second_part_index = self.val.index(second_part)
        return f'{self.syb[first_part_index]}{self.syb[second_part_index]}'



print('Converted:', Conv().to_roman(44))