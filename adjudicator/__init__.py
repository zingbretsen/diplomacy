from adjudicator.processor import process
from adjudicator.state import data_to_state, state_to_data


def process_game_state(data):
    state = data_to_state(data)
    state.post_register_updates()
    process(state)
    return state_to_data(state)
