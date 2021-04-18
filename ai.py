#-*- coding: utf-8 -*-

import math



# other functions
def check_ennemy_ants_near_allies(ant_structure):
    """Check if an ennemy ants is a specified ally. (return number)
    
    Parameter
    ----------
    ant_structure: structure containing all the ants (list)

    Return
    -------
    close_e_ant: Number of ennemy ants close for each ally ant

    """
    specification: Maxime Dufrasne v1 (18/4/21)
    pass

def compute_danger(anthill_structure, ant_structure):
    """Compute the current level of danger.
    
    Parameters
    -----------
    anthill_structure: list of 2 elements containing the anthills information (list)
    ant_structure: structure containing all the ants (list)

    Return
    ------
    danger: A number who determine the danger level (int)
    """
    specification: Maxime Dufrasne v1 (18/4/21)
    pass

#On a une fonction pour définir le danger, mais faudrait une fonction pour gérer nos strats en fonction de cette valeur danger

def compute_ally_defense_ants(anthill_structure, ant_structure):
    """Compute the number of ants in defense.
    
    Parameters
    -----------
    anthill_structure: list of 2 elements containing the anthills information (list)
    ant_structure: structure containing all the ants (list)

    Return
    ------
    defense_ants: Number of ants considered in defense
    """
    specification: Maxime Dufrasne v1 (18/4/21)
    pass

def compute_fight_worth():
    """Calculate the rentability of a particular fight.
    
    """
    pass

def generate_ants_group():
    """Genreate a list of ants close to each other. (ennemies)
    
    """
    pass

def get_distance_from_ebase_to_closest_mud():
    """Get the distance from the ennemies base to the closest mud.
    
    """
    pass

def compute_muds_steal_time():
    """Compute how long it will take to steal an ennemy's mud.
    
    """
    pass

def get_closest_mud():
    """Get the position of the closest mud from an ally ant.
    
    """
    pass

def seperate_ally_and_ennemy_ants(ant_structure):
    """Creates two list with the allies and ennemies ants.
    
    """
    pass

def get_closest_8_clods_from_anthill(main_structure, anthill_structure):
    """Returns the 8 closest clods from the ally anthill
    
    """
    pass

def define_ants_type():
    """Define the type of each ally ants (attack, collect, defense).
    
    """
    pass

def define_action_for_ant(ant, type):
    """Define the action a particular ant will do this turn.
    
    """
    pass

def generate_order():
    """Generate a valid order in the form of a string.
    
    """
    pass


# main function
def get_AI_orders(main_structure, ant_structure, anthill_structure, player_id):
    """Return orders of AI.
    
    Parameters
    ----------
    game: game data structure (dict)
    player_id: player id of AI (int)

    Returns
    -------
    orders: orders of AI (str)
    
    """

    orders = ''
    
    ...
    ...
    ...
    
    return orders