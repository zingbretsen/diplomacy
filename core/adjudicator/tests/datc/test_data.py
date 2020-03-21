from collections import namedtuple

from core.utils.data import get_fixture_data
from core.adjudicator.territory import CoastalTerritory, InlandTerritory, \
    SeaTerritory

nation_data = get_fixture_data('nations.json')
piece_data = get_fixture_data('pieces.json')
territory_data = get_fixture_data('territories.json')
supply_center_data = get_fixture_data('supply_centers.json')

nations = dict()
territories = dict()


class Territories:
    def __init__(self, **entries):
        self.__dict__.update(entries)


for territory in territory_data:
    fields = territory['fields']
    pk = territory['pk']
    type = fields['type']
    nationality = fields['controlled_by_initial']
    coastal = fields['coastal']
    name = fields['name']
    neighbours = fields['neighbours']
    shared_coasts = fields['shared_coasts']

    if type == 'sea':
        result = SeaTerritory(pk, name, neighbours)
    else:
        if coastal:
            result = CoastalTerritory(pk, name, nationality, neighbours, shared_coasts)
        else:
            result = InlandTerritory(pk, name, nationality, neighbours)
    territories[name] = result

