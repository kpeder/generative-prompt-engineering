from generative_prompt_engineering import initialize_package, PACKAGE_NAME


def test_initialize_package(caplog,
                            package_version) -> None:

    '''
    Test package init and entrypoint.
    '''

    initialize_package()

    ''' Two logs are generated.'''
    assert len(caplog.records) == 2

    ''' The logs use the package name.'''
    for log in caplog.records:
        assert log.name == PACKAGE_NAME.replace('-', '_')

    ''' The first is a warning log that records the package's default loglevel.'''
    assert caplog.records[0].levelname == 'WARNING'
    assert 'loglevel' in caplog.records[0].message

    ''' The second is an info log that records the package's name and version.'''
    assert caplog.records[1].levelname == 'INFO'
    assert package_version in caplog.records[1].message
