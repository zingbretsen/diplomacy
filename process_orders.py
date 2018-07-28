# from dependencies import *
from objects import *
from instances import *
from order_text_processor import get_orders_from_txt
from write_to_log import clear_log

from territories import territories

# Resolve Challenges ==================================================================================

def resolve_challenges():
    write_to_log("\n")
    for move in Move.all_moves:
        move.create_bounces()
                
    write_to_log("\n")
    for move in Move.all_moves:
        move.resolve_bounce()
                
    write_to_log("\n")
    for piece in Piece.all_pieces:
        for other_piece in Piece.all_pieces:
            if piece.challenging == other_piece.challenging and id(piece) != id(other_piece):
                write_to_log("recursing the function because piece at {} is challenging {} the same territory as {}".format(piece.territory.name, piece.challenging.name, other_piece.territory.name))
                resolve_challenges()
    return True

# Process Orders ==================================================================================

def process_orders(turn):
    
    write_to_log("\n")
    get_orders_from_txt(turn)
    
    for piece in Piece.all_pieces:
        piece.assign_piece_to_order()
    
    for order in Order.all_orders:
    # convoy orders have to be carried out before other orders
        if isinstance(order, Convoy):
            order.process_order()
            
    for order in Order.all_orders:
        if not isinstance(order, Convoy):
            order.process_order()
        
    if isinstance(game_properties.phase, Order_Phase):
        resolve_challenges()
        
        for move in Move.all_orders:
            move.piece.change_territory()
        
    # change phase
    game_properties.end_phase()
        
    Move.all_moves =[]
    Order.all_orders =[]


# END TURN ========================================================================================

# def save_orders_to_history():
#     order_history = mongo.db.order_history
#     for order in get_orders():
#         order_history.insert(order)

def end_turn(orders):
    

    # unfinalise_users()

    process_orders(orders)
    
    # save_orders_to_history()
    
clear_log()
end_turn("game_histories/game_1/01_spring_1901.txt")
end_turn("game_histories/game_1/02_fall_1901.txt")
end_turn("game_histories/game_1/03_fall_build_1901.txt")