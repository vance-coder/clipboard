from typing import Optional
from urllib.parse import urlparse, unquote, parse_qs, unquote_plus


def parse_url(stg: str) -> dict:
    ret = {}
    potential = urlparse(stg)
    if potential.query:
        ret = parse_qs(unquote_plus(potential.query))
        # {'A': [1], 'B': [1, 2]} -> {'A': 1, 'B': [1, 2]}
        ret = {k: v[0] if len(v) == 1 else v for k, v in ret.items()}

    return ret

