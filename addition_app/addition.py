# Goal: to create a class which can perform addition of two numbers
# How: create a class with a method which takes two numbers as input and returns the sum of the two numbers


class Addition:
    def __init__(self):
        pass

    def add_two_numbers(self, number1: int, number2: int) -> int:
        """
        Add two numbers and return sum

        :param number1: This is the first number for addition
        :param number2: This is the second number for addition
        :type number1: int
        :type number2: int
        :return sum: The sum of number1 and number2
        # :rtype: int # TODO: check on this and get back to interns
        """
        sum = number1 + number2
        return sum
