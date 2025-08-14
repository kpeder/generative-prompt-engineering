from generative_prompt_engineering import flush_logs
from generative_prompt_engineering.mcp.servers import get_mcp_server, start_mcp_server
from generative_prompt_engineering.mcp.tools import fibonacci_sequence

import logging


logger = logging.getLogger('generative_prompt_engineering.examples.local_mcp_server')

SERVER_NAME = 'mcp_tools'

''' Get a local MCP server and register a tool.'''
try:
    mcp = get_mcp_server(name=SERVER_NAME)

except Exception as e:
    logger.exception('Failed to create MCP server with exception {}.'.format(e))
    flush_logs()

try:
    @mcp.tool(description='Returns the fibonacci sequence as a list of integers.')
    def get_fibonnaci_sequence(n: int = 13):
        '''
        Wrapped tool function for MCP server registration.
        '''
        return fibonacci_sequence(n=n)
except Exception as e:
    logger.exception('Failed to register tool with MCP server with exception {}.'.format(e))
    flush_logs()

''' Start the local MCP server with STDIO transport.'''
try:
    start_mcp_server(mcp=mcp, transport="stdio")

except Exception as e:
    logger.exception('Failed to start MCP server with exception {}.'.format(e))
    flush_logs()
