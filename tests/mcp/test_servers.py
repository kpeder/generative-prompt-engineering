from generative_prompt_engineering.mcp.servers import get_mcp_server

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.tools import Tool
from mcp.server.fastmcp.resources import Resource
from pydantic import AnyUrl


SERVER_NAME = 'test_mcp'


def test_get_mcp_server() -> None:

    '''
    Test get_mcp_server() function and FastMCP registration.
    '''

    mcp = get_mcp_server(name=SERVER_NAME)

    assert isinstance(mcp, FastMCP)
    assert mcp.name == SERVER_NAME

    t_desc = 'A test tool that returns nothing.'

    @mcp.tool(description=t_desc)
    def test_tool():
        pass

    tools = list(mcp._tool_manager._tools.values())

    assert isinstance(tools, list)
    assert len(tools) == 1

    for tool in tools:
        assert isinstance(tool, Tool)
        assert tool.name == 'test_tool'
        assert tool.description == t_desc

    r_desc = 'A test resource that returns nothing.'
    r_uri = 'data://nothing'

    @mcp.resource(description=r_desc,
                  uri=r_uri)
    def test_resource():
        pass

    resources = list(mcp._resource_manager._resources.values())

    assert isinstance(resources, list)
    assert len(resources) == 1

    for resource in resources:
        assert isinstance(resource, Resource)
        assert resource.name == 'test_resource'
        assert resource.description == r_desc
        assert resource.uri == AnyUrl(r_uri)
