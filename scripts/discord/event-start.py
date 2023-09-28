#!/usr/bin/python3

import os
import sys

from discord_webhook import DiscordWebhook, DiscordEmbed

from common import get_urls

EMBED_COLOUR = 'C41010'


def main() :

    camera_id = sys.argv[1]
    camera_name = sys.argv[2]
    event_id = sys.argv[3]

    webhook_urls = get_urls()

    wh_embeds: list[DiscordEmbed] = []
    message = os.getenv('MOTION_INSTRUCTION_MESSAGE')
    if message is not None :
        wh_embeds.append(DiscordEmbed(title='Notice', description=message, color=EMBED_COLOUR))

    wh_content = f"Motion detected at camera {camera_name} (camera_id={camera_id}, event_id={event_id})"

    webhooks = DiscordWebhook.create_batch(urls=webhook_urls, content=wh_content, embeds=wh_embeds)

    for webhook in webhooks :
        webhook.execute()


if __name__ == '__main__' :
    main()
