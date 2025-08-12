from generative_prompt_engineering import PACKAGE_NAME

from google import genai

import importlib
import pytest


def pytest_addoption(parser) -> None:

    '''
    Collect pytest arguments.
    '''

    parser.addoption('--location', action='store', dest='location')
    parser.addoption('--project-id', action='store', dest='project_id')


@pytest.fixture()
def location(request) -> str:

    '''
    Return GCP location string.
    '''

    val = request.config.getoption('location')

    return val


@pytest.fixture()
def project_id(request) -> str:

    '''
    Return GCP project-id string.
    '''

    val = request.config.getoption('project_id')

    return val


@pytest.fixture()
def genai_client(location,
                 project_id) -> genai.Client:

    '''
    Return a genai.Client initialized for Vertex AI.
    '''

    try:
        client = genai.Client(location=location,
                              project=project_id,
                              vertexai=True)

    except Exception as e:
        raise e

    return client


@pytest.fixture()
def package_version():
    return importlib.metadata.version(PACKAGE_NAME)
