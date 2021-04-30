#-*- coding: utf-8 -*-

import math



# other functions
def check_ennemy_ants_near_allies(ant_structure):
    """Check if an ennemy ants is near a specified ally. Close means less than 5 cells away (return number)
    
    Parameter
    ----------
    ant_structure: structure containing all the ants (list)

    #Return
    #-------
    #close_e_ant: Number of ennemy ants close for each ally ant (int)

    specification: Maxime Dufrasne (v.1 18/4/21)
    """
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

    specification: Maxime Dufrasne (v.1 18/4/21)

    """
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
    defense_ants: Number of ants considered in defense (int)
    
    specification: Maxime Dufrasne (v.1 18/4/21)

    """
    pass

def compute_fight_worth(ant_structure):
    """Calculate the rentability of a particular fight.

    Parameters
    ----------
    ant_structure: structure containing the ants (list) 

    Return
    ------
    fight_valid: wether the fight is worth or not (bool) 

    Version
    -------
    specification: Martin Buchet (v.1 19/04/21)
    
    """
    pass

def generate_ants_group(ant_structure, team):
    """Genreate a list of ants close to each other. (ennemies)
    Parameters
    ----------
    ant_structure: the structure containing the ants (list)
    team : your team number (int)

    Return
    ------
    close_ant: a list which contain group of ennemies ants (list)

    Version
    -------
    specification: Liam Letot (19/04/21)
    """
    pass

def get_distance_from_base_to_closest_mud(main_structure, anthill_structure, team):
    """Get the distance from the ennemies base to the closest mud.
    
    parameters
    ----------
    main_structure: main structure of the game board (list)
    anthill_structure: list of 2 elements containing the anthills information (list)
    team: your team number (int)

    returns
    -------
    distance: the distance from ennemies base to the closest mud [x,y] (list)
    closest_mud: coordinate of the closest mud (list)
    Version
    -------
    specification: Liam Letot (19/04/21)
    implementation: Liam Letot (19/04/21)
    """
    anthill_pos = (anthill_structure[team - 1]['pos_y'], anthill_structure[team - 1]['pos_x'])
    distance = 100
    for y in main_structure:
        for x in main_structure[y]:
            if main_structure[y][x]['clod'] != None:
                clod= (y,x)
                dist = math.dist(anthill_pos, clod)
                if dist < distance:
                    distance = dist
                    closest_mud = clod
    return distance, closest_mud

def compute_muds_steal_time(ant_structure, main_structure, ant_id):
    """Compute how long it will take to steal an ennemy's mud.
    parameter
    ---------
    ant_structure : structure containing all the ants (list)
    main_structure: main structure of the game board (list)
    ant_id: the id of the ant who want to steal

    return
    ------
    steal_time: the number of turn to steal a mud (int)

    Version
    -------
    specification: Liam Letot (19/04/21)
    """
    pass

def get_closest_mud(ant_structure, main_structure):
    """Get the position of the closest mud from an ally ant.
    
    Parameters
    ----------
    ant_structure: structure containing all the ants (list)
    main_structure: main structure of the game board (list)

    specification: Maxime Dufrasne (v.1 18/4/21)
    """
    pass

def seperate_ally_and_ennemy_ants(ant_structure, player_id):
    """Creates two list with the allies and ennemies ants.

    Parameters
    ----------
    ant_structure: list of all the ants (list) 
    player_id: which team are we, 1 or 2 (int)

    Returns
    -------
    ally_ants: list of all allied ants (list) 
    enemy_ants: list of all the enemy ants (list) 

    Version
    -------
    specification: Martin Buchet (v.1 19/04/21)  
    implementation: Youlan Collard 
    """
    allies = []
    enemies = []

    for ant in ant_structure:
        if ant['team'] == player_id:
            allies.append(ant)
        else:
            enemies.append(ant)
    
    return enemies, allies

def get_closest_8_clods_from_anthill(main_structure, anthill_structure):
    """Returns the remaining closest clods from the ally anthill needed to win
    
    Parameters
    ----------
    main_structure: main_structure of the game board (list)
    anthill_structure: structure containing the anthills (list)

    Returns
    -------
    closest_clods: the remaining closest clods needed to win the game (list)
    
    Version
    -------
    specification: Liam Letot (19/04/21)
    """
    
    closest_clods = []

    for y in range(-7, 8):
        for x in range(-7, 8):
            if main_structure[y][x]['clod']:
                closest_clods.append(y, x)



    return closest_clods

def define_ants_type(ally_ants, enemy_ants, main_structure):
    """Define the type of each ally ants (attack, collect, defense).
    
    Parameters
    ----------
    ally_ants: list of all allied ants (list) 
    enemy_ants: list of all enemy ants (list)
    main_structure: main structure of the game board (list)

    Returns
    -------
    updated_aliied_ants: list of all allied ants with their defined types (list) 

    Version
    -------
    specification: Martin Buchet (v.1 19/04/21)

    """
    pass

def define_action_for_ant(ant, type):
    """Define the action a particular ant will do this turn.

    Parameters
    ----------
    ant: specified ant (dict)
    type: type of the specified ant (str)

    Returns
    -------
    order: order to execute (dict)

    Version
    -------
    specification: Youlan Collard (v.1 19/04/21)
    
    """
    pass

def generate_order():
    """Generate a valid order in the form of a string.

    Return
    ------
    valid_order: valid order (str) 

    Version
    -------
    spécification: Martin Buchet (v.1 19/04/21)
    
    """
    pass


# main function
def get_AI_orders(main_structure, ant_structure, anthill_structure, player_id):
    """Return orders of AI.
    
    Parameters
    ----------
    main_structure: main data structure of the game board (list)
    ant_structure: structure containing all ants (list)
    anthill_structure: structure containing both anthills (list)
    player_id: player id of AI (int)

    Returns
    -------
    orders: orders of AI (str)

    Version
    -------
    specification: Youlan Collard (v.1 19/04/21)
    
    """

    orders = ''
    
    ...
    ...
    ...
    
    return orders
