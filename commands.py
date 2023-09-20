__all__ = ['commands']
from troop_defs import g

NEW_LINE = "\n"


def base_stats(troop_name: str):
    return f"```{NEW_LINE.join([str(i) for i in g[troop_name] if i[1] is not None])}```"


commands = {
    'base_stats': base_stats
}

print()
