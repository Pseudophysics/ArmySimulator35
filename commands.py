__all__ = ['commands']

import pandas as pd
import os
from troop_defs import g
from state_manager import TroopStates
NEW_LINE = "\n"


def base_stats(troop_name: str,
               user: str,
               state: TroopStates,
               **kwargs):
    return f"```{NEW_LINE.join([str(i) for i in g[troop_name] if i[1] is not None])}```"



def save_states(
        body: str,
        user: str,
        state: TroopStates,
        **kwargs):
    return state.save_state(save_path=body)



print()


def load_states(
        body: str,
        user: str,
        state: TroopStates,
        **kwargs):
    return state.load_state(inputpath=body)


commands = {
    'base_stats': base_stats,
    'save_states': save_states,
    "load_states": load_states,
}