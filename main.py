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
    
def deplacement(origin, destination,):
    """if move valid return the new position of the ant
    Parameter
    ---------
    origin: depart position (list)
    destination: destination position (list)

    Return
    ------
    new_position: destination (list)

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
    ant_pos: pos of attacker (list)

    Return:
    ------
    target_lifepoints: number of health remaining on the target (int)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/2021)
    """

def mourance(ant_pos):
    """if function called remove the dead ant
    Parameter
    ---------
    ant_pos: pos of the dead ant (list)

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


def interpréter_commande(order):
    """take an input, check if it's a true fonction and if it is, call the right fonction, if it's not, send an error

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
    
    def spawn(number_of_turn)
''' Will spawn ant

Parameters
-----------
number_of_turn: 

Version
--------
specification: Maxime Dufrasne (v.1 18/02/21)

def raise

def throw


def dispay()
