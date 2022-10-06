from prefect.blocks.notifications import AppriseNotificationBlock
from pydantic import Field, SecretStr


class WebexTeamsWebhook(AppriseNotificationBlock):
    """
    Enables sending notifications via a provided Webex Teams webhook.
    Args:
        url: Teams webhook URL which can be used to send messages
    Examples:
        Load a saved Teams webhook and send a message:
        ```python
        from prefect.blocks.notifications import WebexTeamsWebhook
        teams_webhook_block = WebexTeamsWebhook.load("BLOCK_NAME")
        teams_webhook_block.notify("Hello from Prefect!")
        ```
    """

    _block_type_name = "Webex Teams Webhook"
    _block_type_slug = "webex-teams-webhook"
    _logo_url = "https://i.imgur.com/fOAw8Rp.png"

    url: SecretStr = Field(
        ...,
        title="Webhook URL",
        description="The Teams incoming webhook URL used to send notifications.",
        example="https://webexapis.com/v1/webhooks/incoming/your-token",
    )