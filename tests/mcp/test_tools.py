from generative_prompt_engineering.mcp.tools import fibonacci_sequence


def test_tools() -> None:

    '''
    Test get_models() function.
    '''

    result = fibonacci_sequence(n=0)
    assert result == []

    result = fibonacci_sequence(n=2)
    assert len(result) == 2
    assert result == [0, 1]

    result = fibonacci_sequence(n=7)
    assert len(result) == 7
    assert result == [0, 1, 1, 2, 3, 5, 8]

    result = fibonacci_sequence()
    assert len(result) == 13
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
