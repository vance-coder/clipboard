
def remove_blank_line(stg: str) -> str:
    return "".join([s for s in stg.splitlines(True) if s.strip()])

