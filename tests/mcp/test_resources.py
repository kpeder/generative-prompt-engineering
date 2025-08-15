from generative_prompt_engineering import get_package_version, PACKAGE_NAME
from generative_prompt_engineering.mcp.resources import package_info

import json


def test_resources() -> None:

    '''
    Test package_info() function.
    '''

    result = json.loads(package_info())
    assert isinstance(result, dict)
    assert result["package"] == PACKAGE_NAME
    assert result["version"] == get_package_version(PACKAGE_NAME)
