#!/usr/bin/python3

import os
import sys
from datetime import datetime

from discord_webhook import DiscordWebhook, DiscordEmbed

from common import get_start_time, get_urls

EMBED_COLOUR = 'C41010'


def main() :

    camera_id = sys.argv[1]
    camera_name = sys.argv[2]
    event_id = sys.argv[3]

    event_time = datetime.strptime(event_id[5:], '%Y%m%d%H%M%S')
    if event_time <= get_start_time() :
        print(f"Skip event {event_id}")
        return

    webhook_urls = get_urls()

    wh_embeds: list[DiscordEmbed] = []
    message = "An image and a video should soon be uploaded, please review those in order to check if something abnormal is indeed happening. If so, please take the necessary actions, such as calling the local authorities."
    address = os.getenv('LOCATION_ADDRESS')
    if address is not None :
        message += f"\n\n*The facilities being monitored by this camera are located at the following address : ||{address}||.*"
    wh_embeds: list[DiscordEmbed] = [
        DiscordEmbed(title='Notice', description=message, color=EMBED_COLOUR, footer={'text': f"Camera {camera_id}"}, timestamp=int(event_time.timestamp()))
    ]

    wh_content = f"Motion detected at camera {camera_name}"

    webhooks = DiscordWebhook.create_batch(urls=webhook_urls, content=wh_content, embeds=wh_embeds)

    for webhook in webhooks :
        webhook.execute()


if __name__ == '__main__' :
    main()
