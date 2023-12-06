import logging

logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send(channel, token, text):
    try:
        response = WebClient(token=token).chat_postMessage(
            channel=channel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": text
                    }
                }
            ]
        )
        assert response.status_code == 200
    except SlackApiError as e:
        assert e.response["error"]
