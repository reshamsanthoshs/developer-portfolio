from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Return sum of two numbers """
    return a+b

tools = [add]
