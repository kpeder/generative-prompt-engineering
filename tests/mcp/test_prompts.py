from generative_prompt_engineering.mcp.prompts import fibannaci_prompt


def test_prompts() -> None:

    '''
    Test system_prompt() function.
    '''

    result = fibannaci_prompt(resource='get_package_info', tool='get_fibonacci_sequence')
    assert isinstance(result, str)
    assert 'get_package_info' in result
    assert 'get_fibonacci_sequence' in result
