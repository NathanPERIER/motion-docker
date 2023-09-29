
import os
import re
from datetime import datetime, timedelta

from typing import Sequence


timedelta_reg = re.compile(r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?')

def get_start_time() -> datetime :
    start_time = datetime.strptime(os.getenv('MOTION_START_TIME'), '%Y%m%d%H%M%S')
    m = timedelta_reg.fullmatch(os.getenv('MOTION_STARTUP_DELAY'))
    delta_hours   = m.group(1)
    delta_minutes = m.group(2)
    delta_seconds = m.group(3)
    if delta_hours is not None :
        start_time += timedelta(hours=int(delta_hours))
    if delta_minutes is not None :
        start_time += timedelta(minutes=int(delta_minutes))
    if delta_seconds is not None :
        start_time += timedelta(seconds=int(delta_seconds))
    return start_time


def get_urls() -> Sequence[str] :
    return [
        val
        for var, val in os.environ.items()
        if var.upper().startswith('DISCORD_WEBHOOK')
    ]
