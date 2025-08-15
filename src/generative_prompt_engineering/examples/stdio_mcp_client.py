from generative_prompt_engineering.mcp.clients import run_stdio_client

from mcp import StdioServerParameters

import asyncio
import logging


logging.getLogger('generative_prompt_engineering').propagate = False  # the buck stops at package root; MCP does dumb stuff to the root logger

logger = logging.getLogger('generative_prompt_engineering.examples.stdio_mcp_client')

server_params = StdioServerParameters(
    command='uv',
    args=['run', '-m', 'generative_prompt_engineering.examples.local_mcp_server'],
    env=None
)


async def list_server_resources(prompts: bool = True, resources: bool = True, tools: bool = True):

    '''
    An async def wrapper for listing local MCP server resources via STDIO client session.
    '''

    async with run_stdio_client(server_params=server_params) as session:

        result: list = []

        if prompts:
            result.append(await session.list_prompts())
        if resources:
            result.append(await session.list_resources())
        if tools:
            result.append(await session.list_tools())

        print(result)

asyncio.run(list_server_resources())
