#-*- coding: utf-8 -*-

import math



# other functions
def check_ennemy_ants_near_allies(ant_structure, main_structure):
    """Check if an ennemy ants is near a specified ally. Close means less than 5 cells away (return number)
    
    Parameter
    ----------
    ant_structure: structure containing all the ants (list)
    main_structure: main structure of the game board (list)

    Return
    -------
    close_e_ant: Number of ennemy ants close for each ally ant (list)

    specification: Maxime Dufrasne (v.1 18/4/21)
    implementation: Maxime Dufrasne (v.1 29/4/21)
    """
    close_e_ant = []

    ant_pos = (ant_structure[ant_id]['pos_y'],ant_structure[ant_id]['pos_x'])
    for y in range (-5,5):
        for x in range (-5,5):
            if main_structure[y][x]['ant'] != None:
                close_e_ant.append((y,x))
    return close_e_ant


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
    implémentation: Martin Buchet (v.1 )

    """
    danger = 0
    e_average_dist = e_average_dist_from_a_base(ant_structure, anthill_structure)

    if e_average_dist <= 5:
        danger += 10 
    elif e_average_dist > 5 and e_average_dist <= 10:
        danger += 7.5
    else:
        danger += 5

    a_average_dist = a_average_dist_from_a_base(ant_structure, anthill_structure)

    if a_average_dist <= 5:
        danger -= 2.5
    elif a_average_dist > 5 and a_average_dist <= 10:
        danger += 3.5
    else:
        danger += 7.5

    return danger 

def e_average_dist_from_a_base(ant_structure, anthill_structure, team,):
    """Compute average distance of ennemies ants from allie base

    Parameters
    ----------
    ant_structure: structure containing all the ants (list)
    anthill_structure: list of 2 elements containing the anthills information (list)
    team: the digit of the team we're in (int)

    Return
    ------
    e_average_dist: Ennemies ants average distance from allie base

    Version
    -------
    specification: Maxime Dufrasne (v.1 22/4/21)
    implementation: Martin Buchet (v.1  24/4/21)
    """

    #player_id == team ???
    ants = seperate_ally_and_ennemy_ants(ant_structure, player_id)

    if team == 1:
        team = 0
    else:
        team = 1

    enemies = ants[0] 
    #list of all the distances between ennemies and our base
    e_dist_list = []
    total = 0

    for ants in enemies:
        dist = max(abs(anthill_structure['team']['pos_x'] - ant_structure['pos_x']), abs(anthill_structure['team']['pos_y'] - ant_structure['pos_y']))
        e_dist_list.append(dist)

    for each in range(0, len(e_dist_list)):
        total += e_dist_list[each]

    e_average_dist = total / len(e_dist_list)

    return e_average_dist

def a_average_dist_from_a_base(ant_structure, anthill_structure, team):
    """Compute average distance of allies ants from allie base

    Parameters
    ----------
    ant_structure: structure containing all the ants (list)
    anthill_structure: list of 2 elements containing the anthills information (list)

    Return
    ------
    a_average_dist: Allies ants average distance from allie base

    Version
    -------
    specification: Maxime Dufrasne (v.1 22/4/21 )
    implementation: Maxime Dufrasne (v.1 24/4/21)
    """
    ants = seperate_ally_and_ennemy_ants(ant_structure, player_id)

    if team == 1:
        team = 0
    else:
        team = 1

    a_dist_list = []
    total = 0

    allies = ants[1]

    for ants in allies:
        dist = max(abs(anthill_structure['team']['pos_x'] - ant_structure['pos_x']), abs(anthill_structure['team']['pos_y'] - ant_structure['pos_y']))
        a_dist_list.append(dist)

    for each in range(0, len(a_dist_list)):
        total += a_dist_list[each] 

    a_average_dist = total / len(a_dist_list)

    return a_average_dist

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

def compute_fight_worth(ant_structure, ally_ant):
    """Calculate the rentability of a particular fight.

    Parameters
    ----------
    ennemy_ants: list of all ennemy ants (list)
    ally_ants: list of all ally ants (list)
    ally_ant_id: id of our ant who participates in this fight (int)

    Return
    ------
    fight_point: worth point of the combat (int) 

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
    specification: Liam Letot (v.1 19/04/21)
    """
    pass

def get_distance_from_base_to_closest_clod(main_structure, anthill_structure, team):
    """Get the distance from the ennemies base to the closest mud.
    
    parameters
    ----------
    main_structure: main structure of the game board (list)
    anthill_structure: list of 2 elements containing the anthills information (list)
    team: your team number (int)

    returns
    -------
    distance: the distance from ennemies base to the closest mud [x,y] (list)
    closest_clod: coordinate of the closest mud (list)

    Version
    -------
    specification: Liam Letot (v.1 19/04/21)
    implementation: Liam Letot (v.1 19/04/21)
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
                    closest_clod = clod
    return distance, closest_clod

def compute_clods_steal_time(ant_structure, main_structure, ant_id, anthill_structure, team):
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
    specification: Liam Letot (v.1 19/04/21)
    implementation: Martin Buchet (v.1 23/04/21)
    """
    

def get_closest_clod(ant_structure, main_structure, ant_id):
    """Get the position of the closest mud from an ally ant.
    
    Parameters
    ----------
    ant_structure: structure containing all the ants (list)
    main_structure: main structure of the game board (list)

    specification: Maxime Dufrasne (v.1 18/4/21)
    implementation: Liam Letot (v.1 20/04/21)
    """
    ant_pos = (ant_structure[ant_id]['pos_y'],ant_structure[ant_id]['pos_x'])
    distance =100
    for y in main_structure:
        for x in main_structure[y]:
            if main_structure[y][x]['clod'] != None:
                clod= (y,x)
                dist = math.dist(ant_pos, clod)
                if dist < distance:
                    distance = dist
                    closest_clod = clod
    return closest_clod


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

def get_closest_8_clods_from_anthill(main_structure, anthill_structure, team):
    """Returns the remaining closest clods from the ally anthill needed to win
    
    Parameters
    ----------
    main_structure: main_structure of the game board (list)
    anthill_structure: structure containing the anthills (list)
    team: the team we are in 1 or 2 (int)

    Returns
    -------
    closest_clods: the remaining closest clods needed to win the game (list)
    
    Version
    -------
    specification: Liam Letot (v.1 19/04/21)
    """

    closest_clods = []

    if team == 1:
        team = 0
    else:
        team = 1

    #anthill_pos = (anthill_structure[team]['pos_y'], anthill_structure[team]['pos_x'])

    while len(closest_clods) < 8:
        for y in range(-1, 2):
            for x in range(-1, 2):
                if main_structure[y][x]['clod']:
                    closest_clods.append((y, x))
        
    return closest_clods

def get_distance_between_anthills(anthill_structure):
    """Returns the distance between both anthills

    Parameters
    ----------
    anthill_structure: structure containing both anthills (dict)

    Returns
    -------
    distance: distance in cells (int)

    Version
    -------
    specification: Youlan Collard (v.1 30/04/21)
    implementation: Youlan Collard
    
    """
    pos = []
    for anthill in anthill_structure:
        pos.append((anthill['pos_y'], anthill['pos_x']))
    return int(math.dist(pos[0], pos[1]))

def define_ants_type(ally_ants, enemy_ants, main_structure, danger):
    """Define the type of each ally ants (attack, collect, stealer, defense).
    
    Parameters
    ----------
    ally_ants: list of all allied ants (list) 
    enemy_ants: list of all enemy ants (list)
    main_structure: main structure of the game board (list)
    danger: current danger value of the game (int)

    Returns
    -------
    updated_aliied_ants: list of all allied ants with their defined types (list) 

    Version
    -------
    specification: Martin Buchet (v.1 19/04/21)

    """
    pass

def define_action_for_ant(ant, type, danger):
    """Define the action a particular ant will do this turn.

    Parameters
    ----------
    ant: specified ant (dict)
    type: type of the specified ant (str)
    danger: current danger value of the game

    Returns
    -------
    order: order to execute (dict)

    Version
    -------
    specification: Youlan Collard (v.1 19/04/21)
    
    """
    pass

def generate_order(order):
    """Generate a valid order in the form of a string.

    Parameters
    ----------
    order: dict order generated by previous function (dict)

    Returns
    -------
    orders: valid order (str) 

    Version
    -------
    spécification: Martin Buchet (v.1 19/04/21)
    implementation: Liam Letot (v.1 21/04/21)
    
    """
    ant_pos_y = order[0][0]
    ant_pos_x = order[0][1]
    order_type = order[1]
    if order_type == ('attack' or 'move'):
        target_pos_y = order[2][0]
        target_pos_x = order[2][1]

    orders = str(ant_pos_y + 1) + '-' + str(ant_pos_x +1)
    if order_type == 'drop':
        orders += ':drop '
    elif order_type == 'lift':
        orders += ':lift '
    elif order_type == 'move':
        orders += ':@' + str(target_pos_y + 1) + '-' + str(target_pos_x + 1) + ' '
    elif order_type == 'attack':
        orders += ':*' + str(target_pos_y + 1) + '-' + str(target_pos_x + 1) + ' '

    return orders

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
