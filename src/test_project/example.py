# isort: off
from typing import Union

from loguru import logger

from config import config

# isort: on


logger.configure(**config.logging)


class ExampleClass:
    """
    This is a sample Python Template project class to demonstrate basic code and commenting style.
    """

    def __init__(self, place: str):
        """
        Creates a new ExampleClass to say hi from a ``place``
        :param place:
        """
        self.place = place

    def print_hi_from_place(self, name: str) -> str:
        """
        Prints hi to `name` from a `place`
        :param name: name to use
        return the printed string
        """
        str = f'Hi, {name}. From {self.place}'
        print(str)
        return str

    @classmethod
    def print_hi(cls, name: str) -> None:
        """ Says Hi to `name` """
        print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.

    @logger.catch(message='Intentional divide by zero to demonstrate exception logging. Pretty stack trace follows...')
    def divide_a_by_b(self, a: Union[int, float], b: Union[int, float]) -> float:
        return a / b


if __name__ == '__main__':
    # The class method can be called without instanciating the class
    ExampleClass.print_hi('You')

    # Instanciate the class at a location, then call the object's method
    ex = ExampleClass('Your Python Example Class')
    ex.print_hi_from_place('You')
