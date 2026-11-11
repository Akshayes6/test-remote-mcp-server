from fastmcp import FastMCP
import random
import json

mcp = FastMCP('simple calc server')

@mcp.tool
def add(a: int, b: int) -> int:

    """
    add two numbers together.

    args: 
    a: first number
    b: second number

    returns:
    the sum of a and b

    """

    return a + b

if __name__ == "__main__":
    mcp.run(transport= 'http', host= '0.0.0.0', port= 8000)
