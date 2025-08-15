import logging


logger = logging.getLogger(__name__)


def fibannaci_prompt(resource: str = 'get_package_info', tool: str = 'get_fibonacci_sequence') -> str:

    '''
    Return the package name and version and the fibonacci sequence in JSON format.

    Args:
        data (AnyUrl[str])

    Returns:
        prompt (str): A prompt string containing instructions for a language model.

    Raises:
        e (Exception): Any unhandled exception.
    '''

    prompt: str = f'''
Display a json document containing the data found at the resource {resource} with an additional key appended containing the fibonacci sequence returned by the tool {tool}.
'''

    return prompt
