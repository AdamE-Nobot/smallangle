import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,)
def sin(number):
    """ sin generates a list of numbers from 0 to 2pi and calculates the sin of those numbers

    Args:
        number (_type_): amount of steps to cover the 0 to 2pi range
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n", 
    "--number",
    default=10,
)
def tan(number):
    """ tan generates a list of numbers from 0 to 2pi and calculates the tan of those numbers

    Args:
        number (_type_): amount of steps to cover the 0 to 2pi range
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()