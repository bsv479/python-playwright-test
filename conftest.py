import pytest

from utils.config_reader import read_config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default="PROD",
        action="store",
        choices=("LOCAL", "PROD"),
        help="Choose env param"
    )
    parser.addoption(
        "--run-browser",
        default="CHROMIUM",
        action="store",
        choices=("CHROMIUM", "FIREFOX", "WEBKIT"),
        help="Choose browser param"
    )


@pytest.fixture(scope="session")
def current_env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def run_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['en_US', 'ro_RO', 'it_IT']


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return 12345


@pytest.fixture(scope="session")
def base_url(current_env) -> str:
    return read_config(current_env, "BASE_URL")


@pytest.fixture(scope="session")
def register_url(current_env) -> str:
    return read_config(current_env, "REGISTER_URL")


