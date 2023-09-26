#!/usr/bin/python3

import os
import sys
import json

from discord_webhook import DiscordWebhook


def main() :

    webhook_url = os.getenv('WEBHOOK_URL')

    camera_id = sys.argv[1]
    camera_name = sys.argv[2]
    time_repr = sys.argv[3]

    webhook = DiscordWebhook(url=webhook_url)
    webhook.set_content(f"Motion detected at {camera_name}, {time_repr}")

    webhook.execute()


if __name__ == '__main__' :
    main()
