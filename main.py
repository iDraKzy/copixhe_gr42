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
    specification: Youlan Collard (v.1 18/02/2021 )
    
    """

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
    
def deplacement(main_structure, origin, destination):
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

def mourance(ant_pos):
    """if function called remove the dead ant

    Parameters
    ----------
    ant_pos: pos of the dead ant (tupple)
    main_structure: main structure of the board (list)
    ant_structure: structure containing the ants (list)

    Returns
    -------
    main_structure: the modified main structure (list)
    ant_structure: the modified ant structure (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/2021)
    """
    
def main_fonction():
    """
    call the others fonctions and count the turns
    
    parameters
    ----------
    path : the path to the file used to start the game (str)
    
    Version
    --------
    Specification : Letot Liam (v.1 18/02/21)
    """


def interpret_order(order):
    """take an input, check if it's a true fonction and if it is, return True , if it's not, return False and send an error to the player

    parameters
    ----------
    order : the input of the user (str)

    return
    ------
    order_ok : True if order is a True order, False if it isn't (Bool)
    order_list: return the orders in a list (list)
    
    
    Version
    -------
    Specification : Letot Liam (v.1 18/02/21)
    """

    
def spawn(number_of_turn):
    """ Spawn ant 

    Parameter
    ---------
    number_of_turn: The number of turn passed

    Version
    -------
    specification: Maxime Dufrasne (v.1 18/02/21)
    """


def lift(main_structure, ant_structure, ant_position):
    """ Lift dirt on Ants

    Parameters
    ----------
    main_structure: Library of board
    ant_structure: Library of all ants
    ant_position: Position of the ant that will lift dirt

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21)
    """


def place(main_structure, ant_structure, ant_position):
    """ Place dirt on a case

    Parameters
    ----------
    main_structure: Library of board
    ant_structure: Library of all ants
    ant_position: Position of the ant that will place dirt

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21)
    """


def exec_order(order):
    """ Execute order

    Parameter
    ---------
    order: The order the user imput

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21)
    """

    
    

def dispay(main_structure, ant_structure, anthills_structure):
    """Display the UI in the terminal

    Parameters
    ----------
    main_structure: Main structure of the game board (list)
    ant_structure: Structure containing all the ants (list)
    anthills_structure: Structure containing the anthills (list)

    Version
    -------
    specification: Youlan Collard (v.1 19/02/21)
    """

    
def validation_deplacement(origin, destination, destination_state):
    """check if deplacement is valid and return a boolean
    
    Parameter
    ---------
    origin: depart position (list)
    destination: destination position (list)
    destination_state: potential object on the position blocking the move (list)
    
    Return
    ------
    move_valid: wether move is valid or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/2021)
    """
def range_attack(attacker_pos, target_pos):
    """check if target is in range of the attacker and return a boolean
    
    Parameter
    ---------
    attacker_pos: pos of attacker (list)
    target_pos: pos of target (list)
    
    Return
    ------
    is_in_range: wether the target is in range or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/2021)
    """
