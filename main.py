#-*- coding: utf-8 -*-

import blessed, math, os, time
term = blessed.Terminal()

# Initialize data structure
def parse_map_file(path):
    """Parse the information from the cpx file.

    Parameter
    ---------
    path: path to the cpx file containing the map information (str)

    Returns
    -------
    board_size: Size of the board (tuple)
    antthills: Anthills's positions (list)
    clods: clods's positions (list)

    Version
    -------
    specification: Youlan Collard (v.1 26/02/21)
    
    """

def create_map(path):
    """Create the data structure for the map and returns it.

    Parameters
    ----------
    board_size: Size of the game board (tuple)
    anthills: Anthills's positions (list)
    clods: clods's positions (list)

    Returns
    -------
    main_structure: main structure for the map (list)
    ant_structure: list of existing ants (list)
    anthill_structure: list of 2 elements containing the anthills information (list)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21) (v.2 26/02/21)
    
    """
    

# Victory function
def check_victory(main_structure, anthill_structure):
    """Check if one of the player has win the game and returns the number of the team who has won.

    Parameters
    ----------
    main_structure: main structure of the game, containing the map (list)
    anthill_structure: list containing the anthills information (list)

    Return
    ------
    won: number of the team who has won, None if nobody has (int)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21)
    
    """

# Validation of orders
def interpret_order(main_structure, ant_structure, orders):
    """Take an input, check if it's a true fonction and if it's possible, if both conditions are met, return True , if not, return False and send an error to the player.

    Parameters
    ----------
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    orders: the input of the user (str)

    Returns
    -------
    order_ok: true if order is a True order, False if it isn't (Bool)
    order_list: the orders in a list (list)
    
    Version
    -------
    Specification : Letot Liam (v.1 18/02/21)
    """
    pass

def validation_lift(main_structure, ant_structure, ant_pos):
    """Check if an ant has the force to carry clod and if there is clod where it is.
    
    Parameters
    ----------
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    ant_pos: position of the ant executing the action (tuple)

    Return
    ------
    lift_valid: wether the lifting action is valid or not (bool)

    Version
    -------
    specification: Youlan Collard (v.1 21/02/21)

    
    """
    pass

def validation_attack(attacker_pos, target_pos):
    """Check if target is in range of the attacker and return a boolean.
    
    Parameters
    ----------
    attacker_pos: position of attacker (list)
    target_pos: position of target (list)
    
    Return
    ------
    is_in_range: wether the target is in range or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/21)
    """
    pass

def validation_move(origin, destination, main_structure, ant_structure):
    """Check if deplacement is valid and return a boolean.
    
    Parameters
    ----------
    origin: depart position (list)
    destination: destination position (list)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    
    Return
    ------
    move_valid: wether move is valid or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/21)
    """

# Execution of orders
def exec_order(order_list, main_structure, ant_structure):
    """Execute orders and give the structures to each order fonctions.

    Parameters
    ---------
    order_list: the list of orders the user imput (list)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)

    Version
    -------
    specification: Maxime Dufrasne, Liam Letot (v.1 19/02/21) (v.2 26/02/21)
    """
    pass

def lift(main_structure, ant_structure, ant_position):
    """Lift dirt on ants.

    Parameters
    ----------
    main_structure: library of board (list)
    ant_structure: library of all ants (list)
    ant_position: position of the ant that will lift dirt (tuple)

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21) (v.2 26/02/21)
    """
    pass

def place(main_structure, ant_structure, ant_position):
    """Place dirt on a case.

    Parameters
    ----------
    main_structure: library of board (list)
    ant_structure: library of all ants (list)
    ant_position: position of the ant that will place dirt (tuple)

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21) (v.2 26/02/21)
    """
    pass

def attack(target_pos, target_health, ant_pos, ant_strengh):
    """Compute damage done.

    Parameters
    ----------
    target_health: health of the target (int)
    ant_strengh: strengh of the ant (int)
    target_pos: position of target (list)
    ant_structure: structure containing the ants (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/21) (v.2 26/02/21)
    """
    pass
    
def move(main_structure, origin, destination):
    """if move valid return the new position of the ant.

    Parameters
    ----------
    main_structure: main structure containing the game board (list)
    origin: depart position (list)
    destination: destination position (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/21) (v.2 26/02/21)
    """
    pass

# New ants functions
def check_level(main_structure, anthill):
    """Check the level of an anthill and returns it.

    Parameters
    ----------
    main_structure: main structure of the game, containing the map (list)
    anthill: the anthill to be checked, from the anthill structure (dict)

    Returns
    -------
    level: the level of the anthill (int)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21) (v.2 26/02/21)
        
    """
    pass

def spawn(number_of_turn,ant_structure,main_structure):
    """Spawn ant.

    Parameters
    ----------
    number_of_turn: the number of turn passed (int)
    main_structure: library of board (list)
    ant_structure: library of all ants (list)

    Returns
    -------
    main_structure: modified main structure (list)
    ant_structure: modified ant structure (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 18/02/21)
    """
    pass

# Removal of dead ant function
def death(ant_pos, main_structure, ant_structure):
    """Remove the specified ant.

    Parameters
    ----------
    ant_pos: position of the dead ant (tupple)
    main_structure: main structure of the board (list)
    ant_structure: structure containing the ants (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/21) (v.2 26/02/21)
    """
    pass

# UI Function
def init_dispay(main_structure, ant_structure, anthills_structure):
    """Initialize the display of the UI, create the initial game board from scratch.

    Parameters
    ----------
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    anthills_structure: structure containing the anthills (list)

    Version
    -------
    specification: Youlan Collard (v.1 19/02/21)
    """

def move_ant_on_display(old_position, new_position):
    """Change the position of an ant on the dispay.

    Paremeters
    ----------
    old_position: the old position of an ant (tuple)
    new_position: the new position of an ant (tuple)

    Version
    -------
    spécification: Maxime Dufrasne (v.1 22/02/21)
    
    """
    pass

def remove_ant_on_display(ant_position,carrying):
    """Remove ant on dispay when she died.

    Parameters
    ----------
    ant_position: position of an ant (tuple)
    carrying: if the ant was carrying something (bool)
    
    Version
    -------
    spécification: Maxime Dufrasne  (v.1 22/02/21)
    """
    pass

def update_lifepoint_on_display(ant_id, ant_structure):
    """Update the health bar of an ant on display.

    Parameters
    ----------
    ant_structure: structure containing all the ants (list)
    ant_id: id of the desired ant (int)
    
    Version
    -------
    specification: Martin Buchet (v.1 22/02/21)
    """
    pass

def lift_dirt_on_display(ant_position):
    """Make the dirt disappear and switch the ant to an ant with dirt on display.
    
    Parameter
    ---------
    ant_position: the position of the ant who lift the dirt (tupple)

    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    """
    pass

def place_dirt_on_display(ant_position):
    """Make the dirt appear and switch the ant with a dirt to an ant on display.

    Parameter
    ---------
    ant_position: the position of the ant who lift the dirt (tupple)

    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    """
    pass

def add_ant_on_display(ant_structure, ant_id):
    """Add an ant on display (game board and health bar).
    
    Parameters
    ----------
    ant_structure: the list with all informations on ants (list)
    ant_id: the id of the new ant (int)
    
    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    """
    pass

# Util function
def return_ant_by_id(ant_structure, ant_id):
    """Find an ant by its id inside the ant structure.

    Parameters
    ----------
    ant_structure: the structure containing all the ants (list)
    ant_id: id of the desired ant (int)

    Return
    ------
    ant: The desired ant (dict)

    Version
    -------
    specification: Youlan Collard (v.1 21/02/21)    
    """
    pass

# main function
def play_game(CPX_file, group_1, type_1, group_2, type_2):
    """Play a Copixhe game.
    
    Parameters
    ----------
    CPX_file: name of CPX file (str)
    group_1: group of player 1 (str)
    type_1: type of player 1 (str)
    group_2: group of player 2 (str)
    type_2: type of player 2 (str)
    
    Notes
    -----
    Player type is either human, AI or remote.
    
    If there is an external referee, set group id to 0 for remote player.
    
      Version
    -------
    implementation : Liam Letot (v.1 26/02/21)
    
    """

    number_of_turn = 0

    main_structure, ant_structure, anthill_structure = create_map(CPX_file)
    init_dispay(main_structure, ant_structure)

    while not check_victory:
        orders = input('what do you want to do?')
        orders_list = interpret_order(main_structure, ant_structure, orders)
        exec_order(orders_list, main_structure, ant_structure)
        spawn(number_of_turn, ant_structure, main_structure)
        number_of_turn += 1