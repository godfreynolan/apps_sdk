from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def multiply(a:int, b:int) -> int:
    """
    Multiply two numbers.
    """
    return a * b

if __name__ == "__main__":
    mcp.run(
        transport="http",
        port=8080
    )
