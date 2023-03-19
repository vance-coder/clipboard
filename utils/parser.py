import struct
from typing import Optional, Union
from datetime import datetime
from dateutil.parser import parse as dateutil_parse

from urllib.parse import urlparse, unquote, parse_qs, unquote_plus


def parse_url(stg: str) -> dict:
    ret = {}
    potential = urlparse(stg)
    if potential.query:
        ret = parse_qs(unquote_plus(potential.query))
        # {'A': [1], 'B': [1, 2]} -> {'A': 1, 'B': [1, 2]}
        ret = {k: v[0] if len(v) == 1 else v for k, v in ret.items()}

    return ret


def date_parse(stg: str) -> Optional[datetime]:
    try:
        return dateutil_parse(stg)
    except Exception as e:
        return


def to_list(stg: str) -> Optional[list]:
    if '\n' in stg:
        return list(map(str.strip, stg.split('\n')))

    return
