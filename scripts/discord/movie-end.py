#!/usr/bin/python3

import os
import sys
import json

from discord_webhook import DiscordWebhook


def main() :

    webhook_url = os.getenv('WEBHOOK_URL')

    camera_id = sys.argv[1]
    camera_name = sys.argv[2]
    filepath = sys.argv[3]

    webhook = DiscordWebhook(url=webhook_url)
    webhook.set_content(f"Video recording saved at {camera_name}")

    with open(filepath, 'rb') as f:
        webhook.add_file(file=f.read(), filename=os.path.basename(filepath))

    webhook.execute()


if __name__ == '__main__' :
    main()
