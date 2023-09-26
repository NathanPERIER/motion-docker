#!/usr/bin/python3

import os
import sys
import json

from discord_webhook import DiscordWebhook


def main() :

    webhook_url = os.getenv('WEBHOOK_URL')

    camera_id = sys.argv[1]
    camera_name = sys.argv[2]
    event_id = sys.argv[3]

    print(f"Motion detected at camera {camera_name} (camera_id={camera_id}, event_id={event_id})")

    webhook = DiscordWebhook(url=webhook_url)
    webhook.set_content(f"Motion detected at {camera_name}")

    webhook.execute()


if __name__ == '__main__' :
    main()
