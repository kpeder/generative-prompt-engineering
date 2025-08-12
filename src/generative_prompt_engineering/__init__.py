from google.cloud import logging_v2
from typing import TextIO

import importlib
import logging
import sys


PACKAGE_NAME = __name__


def _get_root_logger(handlers: list[logging.Handler] | None = None,
                     loglevel: int = logging.WARN) -> logging.Logger:

    '''
    Get a root logger for the package, and add provided handlers.

    Args:
        handlers (logging.Handler): A list of configured handlers to add to the logger.
        level (int): The loglevel to configure the logger with. Must be a defined constant.

    Returns:
        logger (logging.Logger): A logger object configured with the specified handlers.

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        logger = logging.getLogger(__name__)

        if handlers:
            for handler in handlers:
                logger.addHandler(handler)

        logger.setLevel(loglevel)
        logger.warning('Package loglevel has been set to {}.'.format(logger.getEffectiveLevel()))

        return logger

    except Exception as e:
        raise e


def get_cloud_logging_handler(formatter: logging.Formatter = logging.Formatter(fmt='%(name)s: %(levelname)s: %(message)s', datefmt='%(asctime)s'),
                              log_name: str = 'prompt_engineering_experiments') -> logging.Handler:

    '''
    Get a cloud logging handler and set the format and name.

    Args:
        formatter (logging.Formatter): A formatter object to add to the handler.
        log_name (str): The name of the handler's Cloud Logging API log.

    Returns:
        handler (logging.Handler): A log handler configured for the Cloud Logging API.

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        client = logging_v2.Client()
        handler = client.get_default_handler(name=log_name)
        handler.setFormatter(formatter)

        return handler

    except Exception as e:
        raise e


def get_console_logging_handler(formatter: logging.Formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s'),
                                out_stream: TextIO = sys.stdout) -> logging.Handler:

    '''
    Get a console logging handler and set the format and output stream.

    Args:
        formatter (logging.Formatter): A formatter object to add to the handler.
        out_stream (typing.TextIO): The output stream that the handler should log to.

    Returns:
        handler (logging.Handler): A log handler configured for the specified output stream.

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        handler = logging.StreamHandler()
        handler.setStream(out_stream)
        handler.setFormatter(formatter)

        return handler

    except Exception as e:
        raise e


def get_package_version(package_name: str) -> str:

    '''
    Display the package version found in the package metadata.

    Args:
        package_name (str): The name of the package.

    Returns:
        version (str): The version of the named package.

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        version = importlib.metadata.version(package_name)
        return version

    except Exception as e:
        raise e


def initialize_package(handlers: list[logging.Handler] = []) -> None:

    '''
    Initialize the package with a root logger. Defaults to Cloud Logging and Console handlers.

    Args:
        handlers (list[logging.Handler]): Non-default logging handlers to configure. Overrides defaults.

    Returns:
        None

    Raises:
        e (Exception): Any unhandled exception.
    '''

    try:
        if not handlers:
            handlers.append(get_cloud_logging_handler())
            handlers.append(get_console_logging_handler())

        logger = _get_root_logger(handlers=handlers, loglevel=logging.INFO)

    except Exception as e:
        raise e

    try:
        version = get_package_version(package_name=PACKAGE_NAME)

        logger.info('Package {} version {}.'.format(PACKAGE_NAME, version))
        for handler in logger.handlers:
            handler.flush()

    except Exception as e:
        logger.exception(e)
        raise e


initialize_package()
