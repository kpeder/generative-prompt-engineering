from generative_prompt_engineering import flush_logs, get_package_version, PACKAGE_NAME

import json
import logging


logger = logging.getLogger(__name__)


def package_info() -> str:

    '''
    Return the package name and version in JSON format.

    Args:
        None

    Returns:
        package (dict): A json string containing keys "package" and "version".

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        package = json.dumps({"package": PACKAGE_NAME,
                              "version": get_package_version(PACKAGE_NAME)})

        return package

    except Exception as e:
        logger.exception('Failed to dump package info with exception {}.'.format(e))
        flush_logs()
