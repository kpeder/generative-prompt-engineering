from generative_prompt_engineering.models import get_models


def test_get_models(genai_client) -> None:

    '''
    Test get_models() function.
    '''

    models = get_models(client=genai_client,
                        query_base=True)

    assert models
