from generative_prompt_engineering import flush_logs

from mcp.server.fastmcp import FastMCP
from typing import Literal

import logging


logger = logging.getLogger(__name__)


def get_mcp_server(name: str) -> FastMCP:

    '''
    Get a default MCP server.

    Args:
        name (str): The name of the MCP server.

    Returns:
        mcp (FastMCP): A default instance of the FastMCP server.

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        mcp = FastMCP(name)
        logger.info('Created FastMCP server instance "{}".'.format(name))

        return mcp

    except Exception as e:
        logger.exception(e)
        flush_logs(logger=logger)


def start_mcp_server(mcp: FastMCP, transport: Literal['stdio', 'sse', 'streamable-http'] = "stdio") -> None:

    '''
    Starts an MCP server instance.

    Args:
        mcp (FastMCP): The MCP server instance to start.

    Returns:
        None

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        logger.info('Starting MCP server instance "{}".'.format(mcp.name))
        mcp.run(transport=transport)

    except Exception as e:
        logger.exception(e)
        flush_logs(logger=logger)
