import json
from typing import Optional, Union


def beautify_json(dct_like: Union[str, dict]) -> str:
    if isinstance(dct_like, str):
        dct_like = json.loads(dct_like)

    return json.dumps(dct_like, ensure_ascii=False, indent=4)
