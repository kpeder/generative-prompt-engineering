from generative_prompt_engineering import initialize_package, PACKAGE_NAME


def test_initialize_package(caplog,
                            package_version) -> None:

    '''
    Test package init and entrypoint.
    '''

    initialize_package()

    assert len(caplog.records) == 2

    for log in caplog.records:
        assert log.name == PACKAGE_NAME.replace('-', '_')

    assert caplog.records[0].levelname == 'WARNING'
    assert 'loglevel' in caplog.records[0].message

    assert caplog.records[1].levelname == 'INFO'
    assert package_version in caplog.records[1].message
