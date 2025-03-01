"""
Programming for linguists

Interfaces and classes of Binary operators
"""

from algorithms.calculator.reverse_polish_notation.digit import Digit
from algorithms.calculator.reverse_polish_notation.op import Op


class BinaryOp(Op):
    """
    Base class for Binary operators (operators with two arguments)
    """

    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        """
        The static function that computes the result of the binary operator
        Must be implemented in each class of particular operator

        :param first_element: float - first operand of the binary operator
        :param second_element: float - second operand of the binary operator
        :return: float - result of computing the operation in the "raw" (floating) format
        """
        raise NotImplementedError

    def __call__(self, first_element: Digit, second_element: Digit) -> Digit:
        """
        Magic method to provide computing of the operation. It is the wrapper for the static `function` method
        The main goal of this method is encapsulate work with operands as instances of Digit class

        :param first_element: Digit - first operand of the binary operator
        :param second_element: Digit - second operand of the binary operator
        :return: float - result of computing the operation as an instance of Digit class
        """
        first_digit = first_element.digit
        second_digit = second_element.digit
        return super().__call__(first_digit, second_digit)


class Plus(BinaryOp):
    """
    Implementation of operator +
    """

    symbol = '+'
    priority = 0
    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        result = first_element + second_element
        # print(result)
        return result


class Minus(BinaryOp):
    """
    Implementation of operator -
    """
    symbol = '-'
    priority = 0
    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        result = first_element - second_element
        return result


class Multiplier(BinaryOp):
    """
    Implementation of operator *
    """
    symbol = '*'
    priority = 1
    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        result = first_element * second_element
        return result


class Divider(BinaryOp):
    """
    Implementation of operator /
    """
    symbol = '/'
    priority = 1
    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        result = first_element / second_element
        return result


class Power(BinaryOp):
    """
    Implementation of operator ^
    """
    symbol = '^'
    priority = 2
    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        result = first_element ** second_element
        return result
