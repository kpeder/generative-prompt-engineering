from generative_prompt_engineering import flush_logs
from generative_prompt_engineering.mcp.prompts import fibannaci_prompt
from generative_prompt_engineering.mcp.resources import package_info
from generative_prompt_engineering.mcp.servers import get_mcp_server, start_mcp_server
from generative_prompt_engineering.mcp.tools import fibonacci_sequence

import json
import logging


logging.getLogger('generative_prompt_engineering').propagate = False  # the buck stops at package root; MCP does dumb stuff to the root logger

logger = logging.getLogger('generative_prompt_engineering.examples.local_mcp_server')

SERVER_NAME = 'mcp_local'

''' Get a local MCP server and register a prompt, a resource, and a tool.'''
try:
    mcp = get_mcp_server(name=SERVER_NAME)

except Exception as e:
    logger.exception('Failed to create MCP server with exception {}.'.format(e))
    flush_logs()

try:
    @mcp.prompt(description='Returns the package information and fibonacci sequence in JSON format.')
    def get_fibonacci_prompt():
        '''
        Wrapped resource for MCP server registration.
        '''
        return fibannaci_prompt()

    logger.info('Registered prompt {} with MCP server instance {}.'.format(list(mcp._prompt_manager._prompts.values())[0].name, mcp.name))

except Exception as e:
    logger.exception('Failed to register resource with MCP server with exception {}.'.format(e))
    flush_logs()

try:
    @mcp.resource(description='Returns the package information in JSON format.',
                  uri='data://package-info')
    def get_package_info():
        '''
        Wrapped resource for MCP server registration.
        '''
        return json.loads(package_info())

    logger.info('Registered resource {} with MCP server instance {}.'.format(list(mcp._resource_manager._resources.values())[0].name, mcp.name))

except Exception as e:
    logger.exception('Failed to register resource with MCP server with exception {}.'.format(e))
    flush_logs()

try:
    @mcp.tool(description='Returns the fibonacci sequence as a list of integers.')
    def get_fibonnaci_sequence(n: int = 13):
        '''
        Wrapped tool function for MCP server registration.
        '''
        return fibonacci_sequence(n=n)

    logger.info('Registered tool {} with MCP server instance {}.'.format(list(mcp._tool_manager._tools.values())[0].name, mcp.name))

except Exception as e:
    logger.exception('Failed to register tool with MCP server with exception {}.'.format(e))
    flush_logs()

''' Start the local MCP server with STDIO transport.'''
try:
    start_mcp_server(mcp=mcp, transport="stdio")

except Exception as e:
    logger.exception('Failed to start MCP server with exception {}.'.format(e))
    flush_logs()
