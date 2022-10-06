# prefect-webex-teams-notifications

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-webex-teams-notifications/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-webex-teams-notifications?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/rpeden/prefect-webex-teams-notifications/" alt="Stars">
        <img src="https://img.shields.io/github/stars/rpeden/prefect-webex-teams-notifications?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-webex-teams-notifications/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-webex-teams-notifications?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/rpeden/prefect-webex-teams-notifications/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/rpeden/prefect-webex-teams-notifications?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

A Prefect collection for working with WebEx Teams.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-webex-teams-notifications` with `pip`:

```bash
pip install prefect-webex-teams-notifications
```

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_webex_teams.notifications
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).


## Resources

If you encounter any bugs while using `prefect-webex-teams-notifications`, feel free to open an issue in the [prefect-webex-teams-notifications](https://github.com/rpeden/prefect-webex-teams-notifications) repository.

If you have any questions or issues while using `prefect-webex-teams-notifications`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-webex-teams-notifications`](https://github.com/rpeden/prefect-webex-teams-notifications) for updates too!

## Development

If you'd like to install a version of `prefect-webex-teams-notifications` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/rpeden/prefect-webex-teams-notifications.git

cd prefect-webex-teams-notifications/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
