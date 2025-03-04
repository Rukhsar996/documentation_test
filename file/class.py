class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def __add__(self, a, b):
        """
        Adds two numbers together.

        Parameters:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

        Returns:
        int or float: The sum of a and b.
        """
        return a + b

class Animal:
    """Base class for all animals.

    Attributes:
        name (str): The name of the animal.
        product (str): The product of the animal (e.g., Milk, wool, eggs).
    """

    def __init__(self, name, product):
        """Initialize the animal with a name and product.

        Args:
            name (str): The name of the animal.
            product (str): The product the animal produces.
        """
        self.name = name
        self.product = product
        print('I am inside the class, I was called to make', name, 'to produce', product)


class Cow(Animal):
    def __str__(self):
        return f"{self.name} is giving {self.product}"

    def speak(self, sound):
        """Makes the Animal speak.

        Args:
            sound (str): The sound the animal makes.

        Returns:
            str: A message indicating what sound the animal is making.
        """
        return f"{self.name} is making this sound: {sound}"



