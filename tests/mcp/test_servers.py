from generative_prompt_engineering.mcp.clients import run_stdio_client
from generative_prompt_engineering.mcp.servers import get_mcp_server

from mcp import StdioServerParameters
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import Prompt
from mcp.server.fastmcp.tools import Tool
from mcp.server.fastmcp.resources import Resource
from pydantic import AnyUrl

import asyncio
import pytest


SERVER_NAME = 'test_mcp'
SERVER_PARAMS = StdioServerParameters(command='uv',
                                      args=['run', '-m', 'generative_prompt_engineering.examples.test_mcp_server'],
                                      env=None)


def test_get_mcp_server() -> None:

    '''
    Test get_mcp_server() function and FastMCP registration.
    '''

    mcp = get_mcp_server(name=SERVER_NAME)

    assert isinstance(mcp, FastMCP)
    assert mcp.name == SERVER_NAME

    p_desc = 'A test prompt.'

    @mcp.prompt(description=p_desc)
    def test_prompt():
        return 'This is a test prompt.'

    prompts = list(mcp._prompt_manager._prompts.values())

    assert isinstance(prompts, list)
    assert len(prompts) == 1

    for prompt in prompts:
        assert isinstance(prompt, Prompt)
        assert prompt.name == 'test_prompt'
        assert prompt.description == p_desc

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


@pytest.mark.asyncio
async def test_run_stdio_client():

    '''
    Test async context managed stdio client session.
    '''

    async with run_stdio_client(server_params=SERVER_PARAMS) as session:

        assert await session.send_ping()


asyncio.run(test_run_stdio_client())
