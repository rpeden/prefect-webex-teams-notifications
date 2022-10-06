from prefect import flow

from prefect_webex_teams.tasks import (
    goodbye_prefect_webex_teams,
    hello_prefect_webex_teams,
)


def test_hello_prefect_webex_teams():
    @flow
    def test_flow():
        return hello_prefect_webex_teams()

    result = test_flow()
    assert result == "Hello, prefect-webex-teams-notifications!"


def goodbye_hello_prefect_webex_teams():
    @flow
    def test_flow():
        return goodbye_prefect_webex_teams()

    result = test_flow()
    assert result == "Goodbye, prefect-webex-teams-notifications!"
