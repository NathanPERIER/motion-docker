#!/usr/bin/python3

import os
import sys
import json

from discord_webhook import DiscordWebhook


def main() :

    webhook_url = os.getenv('WEBHOOK_URL')

    webhook = DiscordWebhook(url=webhook_url)
    webhook.set_content(f"Picture save\n`{json.dumps(sys.argv)}`")

    webhook.execute()


if __name__ == '__main__' :
    main()
