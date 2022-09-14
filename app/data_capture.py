from collections import defaultdict

from app.utils.decorators import validate_number


class Stats:
    MAX_VALUE = 1000
    MIN_VALUE = 0

    def __init__(self, data) -> None:

        self.numbers_quantity = defaultdict(lambda: 0)
        self.num_g_than =  {}
        self.num_l_than = {}

        for num in data:
            self.numbers_quantity[num] += 1

        num_l = 0
        for num in range(self.MAX_VALUE + 1):
            num_l += self.numbers_quantity[num] 
            self.num_l_than[num + 1] =   num_l

        num_g = 0
        for num in range(self.MAX_VALUE + 1, self.MIN_VALUE - 1,-1):
            num_g += self.numbers_quantity[num] 
            self.num_g_than[num - 1] =   num_g

    @validate_number
    def less(self, number: int) -> int:
        '''
            Get the amount of numbers less than the parameter
            :param int number: value to check
        '''
        return self.num_l_than[number]

    @validate_number
    def greater(self, number: int) -> int:
        '''
            Get the amount of numbers greater than the param
            :param int number: value to check
        '''
        return self.num_g_than[number]

    @validate_number
    def between(self,lower: int, upper: int) -> int:
        '''
            Send a message to a recipient.
            :param int lower: Lower limit
            :param int upper: Upper limit
        '''
        if lower > upper:
            lower,upper = upper,lower
        return self.num_l_than[upper + 1] - self.num_l_than[lower - 1]


class DataCapture:

    def __init__(self) -> None:
        self.data = []
    @validate_number
    def add(self, number: int) -> None:
        '''
            Add number to the collection
            :param int number: value to add

        '''
        self.data.append(number)

    def build_stats(self) -> Stats:
        '''
            Return collection stats
        '''
        return Stats(self.data)

    def __str__(self) -> str:
        return ' '.join([str(number) for number in self.data])

