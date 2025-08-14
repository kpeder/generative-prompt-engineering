from generative_prompt_engineering import flush_logs

from google.genai import Client

import logging


logger = logging.getLogger(__name__)


def get_models(client: Client,
               query_base: bool = True) -> list:

    '''
    Get a list of available Generative AI models.

    Args:
        client (genai.Client): An initialized Vertex AI or Gemini API platform client.
        page_size (int): How many models to return per page in the response.
        query_base (bool): Whether to return a list of base models or tuned models.

    Returns:
        models (list): A list of model names matching the configured criteria.

    Raises:
        e (Exception): Any unhandled exception, as necessary.
    '''

    config = {'query_base': query_base}

    models: list = []

    try:
        for model in client.models.list(config=config):
            models.append(model.name)

    except Exception as e:
        logger.exception(e)
        flush_logs()

    return models
