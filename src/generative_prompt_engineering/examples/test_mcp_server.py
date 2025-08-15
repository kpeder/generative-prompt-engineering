from generative_prompt_engineering import flush_logs
from generative_prompt_engineering.mcp.servers import get_mcp_server, start_mcp_server

import logging


logger = logging.getLogger('generative_prompt_engineering.examples.test_mcp_server')

SERVER_NAME = 'mcp_test'

''' Get a local MCP server and register a tool, a resource and a prompt.'''
try:
    mcp = get_mcp_server(name=SERVER_NAME)

except Exception as e:
    logger.exception('Failed to create MCP server with exception {}.'.format(e))
    flush_logs()

''' Start the local MCP server with STDIO transport.'''
try:
    start_mcp_server(mcp=mcp, transport="stdio")

except Exception as e:
    logger.exception('Failed to start MCP server with exception {}.'.format(e))
    flush_logs()
