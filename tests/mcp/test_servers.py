from generative_prompt_engineering.mcp.servers import get_mcp_server

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.tools import Tool


SERVER_NAME = 'test_mcp'


def test_get_mcp_server() -> None:

    '''
    Test get_mcp_server() function.
    '''

    mcp = get_mcp_server(name=SERVER_NAME)

    assert isinstance(mcp, FastMCP)
    assert mcp.name == SERVER_NAME

    desc = 'A test tool that returns nothing.'

    @mcp.tool(description=desc)
    def test_tool():
        pass

    tools = list(mcp._tool_manager._tools.values())

    assert isinstance(tools, list)
    assert len(tools) == 1

    for tool in tools:
        assert isinstance(tool, Tool)
        assert tool.name == 'test_tool'
        assert tool.description == desc
