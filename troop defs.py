from pydantic import BaseModel
from typing import Tuple, Optional
import re
import math
import pandas as pd


class TroopChar(BaseModel):
    troop_name: str
    total_hp: int
    defense: int
    dice: str
    spdef: int
    speed: int
    static_ability_1: Optional[str] = None
    static_ability_2: Optional[str] = None
    movement: str = 'walk'
    heal: Optional[str] = None
    charge1: Optional[str] = None
    charge2: Optional[str] = None
    pilotable: Optional[str] = None
    roll1: Optional[str] = None
    roll2: Optional[str] = None
    creaturetype: Optional[str] = None
    multiplier: Optional[str] = None




def calc_damage_dealt(
    defense: int,
    damage: int
):

    dif = damage - defense
    if dif > 0:
        return dif
    else:
        return 0


def disect_dice(dice: str) -> (int, int):
    """

    :param dice: dice to roll in format adc where a and c are integer values
    :return: tuple(# dice, dice size
    """
    return re.split('d', dice)


def mkunitdict():

    t = pd.read_csv('base_stats.csv')

    t.set_index('Stats', inplace=True)

    troops = {}
    for i in t:

        troops[i] = TroopChar(troop_name=i, **t[i].dropna())
    return troops


g = mkunitdict()


def unit_output():
    required_output = {'troop_name',
                       }

class butter():
print(g)

class Gish():



def read_commands(frame:pd.DataFrame()):
    '''

    :param frame:
    :return:
    '''
    keys = [
        'unit name',
        'unit type',
        'current hp',
        'status',
        'location',
        'order',
        'target',
        'value rolled'
    ]




