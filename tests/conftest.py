import pathlib

import pytest


@pytest.fixture(scope='session')
def tests_dir():
    return pathlib.Path(__file__).parent.absolute()


@pytest.fixture(scope='session')
def fixtures_dir(tests_dir):
    return tests_dir.joinpath('fixtures')


@pytest.fixture(scope='session')
def fixture_hamlet_info(fixtures_dir):
    return fixtures_dir.joinpath('hamlet.info')


@pytest.fixture(scope='session')
def fixture_hamlet_txt(fixtures_dir):
    return fixtures_dir.joinpath('hamlet.txt')


@pytest.fixture(scope='session')
def fixture_empty_txt(fixtures_dir):
    return fixtures_dir.joinpath('empty.txt')
