import logging


logger = logging.getLogger(__name__)


def fibonacci_sequence(n: int = 13) -> list[int]:

    '''
    Return the fibonacci sequence.

    Args:
        iterations (int): The number of digits in the sequence to return.

    Returns:
        sequence (list[int]): A list of the first n integers in the fibonacci sequence.

    Raises:
        None
    '''

    sequence: list = [0, 1]

    if n < 0:
        return []

    if n < 2:
        return sequence[:n]

    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence
