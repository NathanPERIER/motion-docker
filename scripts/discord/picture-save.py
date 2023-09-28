#!/usr/bin/python3

import os
import sys

from discord_webhook import DiscordWebhook

from common import get_urls


def main() :

    camera_id = sys.argv[1]
    camera_name = sys.argv[2]
    filepath = sys.argv[3]

    webhook_urls = get_urls()

    wh_content = f"Picture saved at {camera_name}"

    wh_files: dict[str,bytes] = {}
    with open(filepath, 'rb') as f:
        wh_files[os.path.basename(filepath)] = f.read()

    webhooks = DiscordWebhook.create_batch(urls=webhook_urls, content=wh_content, files=wh_files)

    for webhook in webhooks :
        webhook.execute()


if __name__ == '__main__' :
    main()
