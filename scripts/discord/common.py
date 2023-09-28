
import os

from typing import Sequence


def get_urls() -> Sequence[str] :
    return [
        val
        for var, val in os.environ.items()
        if var.upper().startswith('DISCORD_WEBHOOK')
    ]
