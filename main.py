#-*- coding: utf-8 -*-

import blessed, math, os, time
term = blessed.Terminal()

# Initialize data structure
def create_map(path):
    """Create the data structure for the map and returns it.

    Parameter
    ---------
    path: Path to the file containing the map information (str)

    Return
    ------
    main_structure: Main structure for the map (list)
    ant_structure: List of existing ants (list)
    anthill_structure: List of 2 elements containing the anthills information (list)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/2021)
    
    """

# Victory function
def check_victory(main_structure, anthill_structure):
    """Check if one of the player has win the game and returns the number of the team who has won.

    Parameter
    ---------
    main_structure: Main structure of the game, containing the map (list)
    anthill_structure: list containing the anthills information (list)

    Return
    ------
    won: Number of the team who has won, None if nobody has (int)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/2021)
    
    """

# Validation of orders
def interpret_order(main_structure, ant_structure, orders):
    """take an input, check if it's a true fonction and if it's possible, if both conditions are met, return True , if not, return False and send an error to the player

    Parameters
    ----------
    main_structure: Main structure of the game board (list)
    ant_structure: Structure containing all the ants (list)
    orders: the input of the user (str)

    Return
    ------
    order_ok: True if order is a True order, False if it isn't (Bool)
    order_list: return the orders in a list (list)
    
    Version
    -------
    Specification : Letot Liam (v.1 18/02/21)
    """

def validation_lift(main_structure, ant_structure, ant_pos):
    """Check if an ant has the force to carry clod and if there is clod where it is
    
    Parameters
    ----------
    main_structure: Main structure of the game board (list)
    ant_structure: Structure containing all the ants (list)
    ant_pos: Position of the ant executing the action (tuple)

    Return
    ------
    lift_valid: Wether the lifting action is valid or not (bool)

    Version
    -------
    specification: Youlan Collard (v.1 21/02/2021)

    
    """

def validation_attack(attacker_pos, target_pos):
    """check if target is in range of the attacker and return a boolean
    
    Parameters
    ----------
    attacker_pos: pos of attacker (list)
    target_pos: pos of target (list)
    
    Return
    ------
    is_in_range: wether the target is in range or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/2021)
    """

def validation_move(origin, destination, main_structure, ant_structure):
    """check if deplacement is valid and return a boolean
    
    Parameter
    ---------
    origin: depart position (list)
    destination: destination position (list)
    main_structure: Main structure of the game board (list)
    ant_structure: Structure containing all the ants (list)
    
    Return
    ------
    move_valid: wether move is valid or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/2021)
    """

# Execution of orders
def exec_order(order_list, main_structure, ant_structure):
    """ Execute orders and give the structures to each order fonctions

    Parameters
    ---------
    order_list: The list of orders the user imput (list)
    main_structure: Main structure of the game board (list)
    ant_structure: Structure containing all the ants (list)
    
    return
    ------
    main_structure: Modified main structure of the game board (list)
    ant_structure: Modified structure containing all the ants (list)

    Version
    -------
    specification: Maxime Dufrasne, Liam Letot (v.1 19/02/21)
    """

def lift(main_structure, ant_structure, ant_position):
    """ Lift dirt on Ants

    Parameters
    ----------
    main_structure: Library of board (list)
    ant_structure: Library of all ants (list)
    ant_position: Position of the ant that will lift dirt (tuple)

    Returns
    -------
    ant_structure: modified ant structure (list)
    main_structure: modified main structure (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21)
    """

def place(main_structure, ant_structure, ant_position):
    """ Place dirt on a case

    Parameters
    ----------
    main_structure: Library of board (list)
    ant_structure: Library of all ants (list)
    ant_position: Position of the ant that will place dirt (tuple)

    Returns
    -------
    main_structure: modified main structure (list)
    ant_structure: modified ant structure (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21)
    """

def attack(target_pos, target_health, ant_pos, ant_strengh):
    """compute damage done 

    Parameter
    ---------
    target_health: health of the target (int)
    ant_strengh: strengh of the ant (int)
    target_pos: pos of target (list)
    ant_structure: Structure containing the ants (list)

    Return
    ------
    ant_structure: Modified ant structure (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/2021)
    """
    
def move(main_structure, origin, destination):
    """if move valid return the new position of the ant

    Parameter
    ---------
    main_structure: main structure containing the game board (list)
    origin: depart position (list)
    destination: destination position (list)

    Return
    ------
    main_structure: modified main structure (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/2021)
    """

# New ants functions
def check_level(main_structure, anthill):
    """Check the level of an anthill and returns it.

    Parameter
    ---------
    main_structure: Main structure of the game, containing the map (list)
    anthill: The anthill to be checked, from the anthill structure (dict)

    Returns
    -------
    level: The level of the anthill (int)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/2021)
        
    """

def spawn(number_of_turn,ant_structure,main_structure):
    """ Spawn ant 

    Parameter
    ---------
    number_of_turn: The number of turn passed (int)
    main_structure: Library of board (list)
    ant_structure: Library of all ants (list)

    Returns
    -------
    main_structure: modified main structure (list)
    ant_structure: modified ant structure (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 18/02/21)
    """

# Removal of dead ant function
def death(ant_pos, main_structure, ant_structure):
    """if function called remove the dead ant

    Parameters
    ----------
    ant_pos: pos of the dead ant (tupple)
    main_structure: main structure of the board (list)
    ant_structure: structure containing the ants (list)

    Return
    ------
    main_structure: the modified main structure (list)
    ant_structure: the modified ant structure (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/2021)
    """

# UI Function
def init_dispay(main_structure, ant_structure, anthills_structure):
    """Initialize the display of the UI, create the initial game board from scratch

    Parameters
    ----------
    main_structure: Main structure of the game board (list)
    ant_structure: Structure containing all the ants (list)
    anthills_structure: Structure containing the anthills (list)

    Version
    -------
    specification: Youlan Collard (v.1 19/02/21)
    """

def move_ant_on_display(old_position, new_position):
    """Change the position of an ant on the dispay

    Paremeters
    ----------
    old_position: The old position of an ant (tuple)
    new_position: The new position of an ant (tuple)

    Version
    -------
    spécification: Maxime Dufrasne (v.1 22/02/21)
    
    """

def remove_ant_on_display(ant_position,carrying):
    """Remove ant on dispay when she died

    Parameters
    ----------
    ant_position: Position of an ant (tuple)
    carrying: If the ant was carrying something (bool)
    
    Version
    -------
    spécification: Maxime Dufrasne  (v.1 22/02/21)
    """

def update_lifepoint_on_display(ant_id, ant_structure,):
    """Update the health bar of an ant on display
    Parameter
    ---------
    ant_structure: Structure containing all the ants (list)
    ant_id: Id of the desired ant (int)
    
    Version
    -------
    specification: Martin Buchet (v.1 22/02/2021)
    """

def lift_dirt_on_display(ant_position):
    """
    make the dirt disappear and switch the ant to an ant with dirt on display
    
    parameter
    ---------
    ant_position: the position of the ant who lift the dirt (tupple)

    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    """

def place_dirt_on_display(ant_position):
    """
    make the dirt appear and switch the ant with a dirt to an ant on display

    parameter:
    ----------
    ant_position: the position of the ant who lift the dirt (tupple)

    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    """

def add_ant_on_display(ant_structure, ant_id):
    """
    Add an ant on display (game board and health bar)
    
    parameter:
    ----------
    ant_structure: the list with all informations on ants (list)
    ant_id: the id of the new ant (int)
    
    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    """

# Util function
def return_ant_by_id(ant_structure, ant_id):
    """Find an ant by its id inside the ant structure

    Parameters
    ----------
    ant_structure: The structure containing all the ants (list)
    ant_id: Id of the desired ant (int)

    Return
    ------
    ant: The desired ant (dict)

    Version
    -------
    specification: Youlan Collard (v.1 21/02/2021)    
    """

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
    
    """