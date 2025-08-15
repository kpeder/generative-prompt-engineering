from generative_prompt_engineering import flush_logs

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import asynccontextmanager

import logging


logger = logging.getLogger(__name__)


@asynccontextmanager
async def run_stdio_client(server_params: StdioServerParameters):

    '''
    Run the stdio_client with StdioServerParameters and return a context-managed async session.

    Args:
        server_params (StdioServerParameters): Server command and arguments.

    Returns:
        session (async session): Ansync context managed STDIO MCP client session.

    Raises:
        e (Exception): Any unhandled exception.
    '''

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            try:
                await session.initialize()
                logger.info('Initialized STDIO client session.')

            except Exception as e:
                logger.exception('Failed to initialize client session with exception {}.'.format(e))
                flush_logs()
                raise e

            try:
                yield session

            finally:
                logger.warning('Terminated STDIO client session.')
                flush_logs()
