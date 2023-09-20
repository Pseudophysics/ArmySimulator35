
__all__ = ['TroopStates']

from pydantic import BaseModel
from pathlib import Path
from typing import List
import pandas as pd
# todo create file to represent map data

# todo ensure grid locations

# todo define troop things

class Unit(BaseModel):
    x: int
    y: int
    z: int
    name: str
    unit_type: str
    controller: str
    condition: List[str] = ['Fine']
    queued_command: str


class TroopStates:
    def __init__(self):
        self.state = pd.DataFrame()

    def load_state(self,
                   inputpath: str
                   ):

        if not self.state.empty:
            # todo I know the state is empty dunno what to do with that yet.
            print('ALL PREVIOUS DATA LOST')

        path = Path(__file__).parent / 'save_states' / inputpath
        print('reading from the following path')

        thang = pd.read_csv(path)
        if thang['name'].duplicated().any():
            raise Exception("There are Duplicate unit troop names")

        thang['condition'] = thang['condition'].str.split('|')

        self.state = thang


    def save_state(self, save_path: str):

        save_location = str(Path(__file__).parent / 'save_states' / save_path)
        self.state['condition'] = self.state['condition'].apply('|'.join)
        self.state.to_csv(save_location, index=False)
        return "```GAME SAVED... DM YOU BETTER NOT HAVE SAVED YOUR DRIVE INFO INTO CHAT```"


#t = TroopStates()
#
#t.load_state(Path(__file__).parent / 'save_states' / 'starting_state.csv')
#
#t.save_state(Path(__file__).parent / 'save_states' / 'babaganoosh_state.csv')
