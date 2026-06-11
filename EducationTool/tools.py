from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Return sum of two numbers """
    return a+b

def area(a: int, b: int) -> int:
    """
    Calculate the area of a rectangle.

    Args:
        length: length of rectangle
        width: width of rectangle
    """
    print(f"area called with a={a}, b={b}")
    return a*b
