#-*- coding: utf-8 -*-

import math
import main

ants_type = {}

# other functions
def check_ennemy_ants_near_allies(ant_structure, main_structure, team):
    """Check if an ennemy ants is near a specified ally. Close means less than 5 cells away (return number)
    
    Parameter
    ----------
    ant_structure: structure containing all the ants (list)
    main_structure: main structure of the game board (list)
    team: ally team number (int)

    Return
    -------
    close_e_ant: List of ant id close to each ally ant (dict)

    specification: Maxime Dufrasne (v.1 18/4/21)
    implementation: Maxime Dufrasne, Youlan Collard (v.1 29/4/21)
    """
    close_e_ant = {}

    for ant in ant_structure:
        close_e_ant[ant['id']] = []
        ant_pos = (ant['pos_y'], ant['pos_x'])
        for y in range(-5, 6):
            for x in range(-5, 6):
                potential_ant_id = main_structure[ant_pos[0] + y][ant_pos[1] + x]
                if potential_ant_id != None:
                    ant_dict = main.return_ant_by_id(ant_structure, potential_ant_id)
                    if ant_dict['team'] != team:
                        close_e_ant[ant['id']].append(potential_ant_id)

    return close_e_ant

def compute_danger(anthill_structure, ant_structure, team):
    """Compute the current level of danger.
    
    Parameters
    -----------
    anthill_structure: list of 2 elements containing the anthills information (list)
    ant_structure: structure containing all the ants (list)

    Return
    ------
    danger: A number who determine the danger level (int)

    specification: Maxime Dufrasne (v.1 18/4/21)
    implementation: Martin Buchet Maxime Dufrasne (v.1 28/4/21 )

    """
    #Need correct values
    danger = 0
    e_average_dist = e_average_dist_from_a_base(ant_structure, anthill_structure, team)

    if e_average_dist <= 5:
        danger += 10 
    elif e_average_dist > 5 and e_average_dist <= 10:
        danger += 7.5
    else:
        danger += 5

    a_average_dist = a_average_dist_from_a_base(ant_structure, anthill_structure, team)

    if a_average_dist <= 5:
        danger -= 2.5
    elif a_average_dist > 5 and a_average_dist <= 10:
        danger += 3.5
    else:
        danger += 7.5

    ennemies, allies = seperate_ally_and_ennemy_ants(ant_structure, team)

    ally_average_level = compute_average_level_ant(allies)
    ennemy_average_level = compute_average_level_ant(ennemies)

    difference_average_level = ennemy_average_level - ally_average_level

    if difference_average_level > 1:
        danger += 15
    elif difference_average_level > 0 and difference_average_level < 1:
        danger += 7.5
    elif difference_average_level < 0 and difference_average_level > -1:
        danger -= 7.5
    elif difference_average_level < -1:
        danger -= 15

    difference_number_ants = len(ennemies) - len(allies)

    if difference_number_ants > 3:
        danger += 15
    elif difference_number_ants > 0:
        danger += 7.5
    elif difference_number_ants < 0 and difference_number_ants > -3:
        danger -= 7.5
    elif difference_number_ants < -3:
        danger -= 15

    return danger 

def compute_average_level_ant(ant_list):
    """Compute the average level of a list of ant.

    Parameters
    ----------
    ant_list: the list to compute (list)

    Returns
    -------
    average_level: The average level of the list (float)

    Version
    -------
    specification: Youlan Collard (v.1)
    implementation: Youlan Collard (v.1)
    
    """
    average_level = 0

    for ant in ant_list:
        average_level += ant['level']

    average_level = average_level / len(ant_list)

    return average_level

def e_average_dist_from_a_base(ant_structure, anthill_structure, team):
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

    ants = seperate_ally_and_ennemy_ants(ant_structure, team)

    enemies = ants[0] 
    #list of all the distances between ennemies and our base
    e_dist_list = []
    total = 0

    for ant in enemies:
        ally_anthill = anthill_structure[team - 1]
        dist = compute_distance((ally_anthill['pos_y'], ally_anthill['pos_x']), (ant['pos_y'], ant['pos_x']))
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
    ants = seperate_ally_and_ennemy_ants(ant_structure, team)

    a_dist_list = []
    total = 0

    allies = ants[1]

    for ant in allies:
        ally_anthill = anthill_structure[team - 1]
        dist = compute_distance((ally_anthill['pos_y'], ally_anthill['pos_x']), (ant['pos_y'], ant['pos_x']))
        a_dist_list.append(dist)

    for each in range(0, len(a_dist_list)):
        total += a_dist_list[each] 

    a_average_dist = total / len(a_dist_list)

    return a_average_dist

def compute_defense_ants(anthill_structure, ant_structure, team):
    """Compute the number of ants in defense for each team.
    
    Parameters
    -----------
    anthill_structure: list of 2 elements containing the anthills information (list)
    ant_structure: structure containing all the ants (list)
    team: team number of our ai (int)

    Return
    ------
    defense_ants: List of ants considered in defense for each team (dict)
    
    specification: Maxime Dufrasne (v.1 18/4/21)
    implementation: Youlan Collard (v.1)
    """

    ennemies, allies = seperate_ally_and_ennemy_ants(ant_structure, team)

    for anthill in anthill_structure:
        if anthill['team'] == team:
            ally_group = generate_defense_group(anthill, allies)
        else:
            ennemy_group = generate_defense_group(anthill, ennemies)

    other_team = get_ennemy_team(team)
    
    return {team: ally_group, other_team: ennemy_group}
        

def generate_defense_group(anthill, ant_list):
    """Generate a list of ants close to the specified anthill given the anthill and the ants posessed by this anthill

    Parameters
    ----------
    anthill: anthill to check (dict)
    ant_list: ants list possessed by this anthill

    Returns
    -------
    ant_group: group of ants considered in defense (list)

    Version
    -------
    specification: Youlan Collard (v.1)
    implementation: Youlan Collard (v.1)
    

    """
    group = []
    anthill_pos = (anthill['pos_y'], anthill['pos_x'])

    for ant in ant_list:
        ant_pos = (ant['pos_y'], ant['pos_x'])
        if compute_distance(anthill_pos, ant_pos) < 6:
            group.append(ant)

    return group


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
    a
    compute_average_level_ant(ant_list)

def generate_ants_e_group(ant_structure, team):
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
    implementation: Youlan Collard (v.1)
    """
    ennemies, allies = seperate_ally_and_ennemy_ants(ant_structure, team)

    groups = []

    for ant in ennemies:
        current_group = []
        for ant_to_check in ennemies:
            if ant['id'] != ant_to_check['id']:
                ant_pos = (ant['pos_y'], ant['pos_x'])
                ant_to_check_pos = (ant_to_check['pos_y'], ant_to_check['pos_x'])
                if compute_distance(ant_pos, ant_to_check_pos) <= 5:
                    current_group.append(ant['id'])

        groups.append(current_group)

    already_seen = []
    groups_not_duplicated = []
    for group in groups:
        duplicates_in_this_group = False
        index = 0
        while not duplicates_in_this_group and len(group) < index:
            ant_id = group[index]
            if not ant_id in already_seen:
                already_seen.append(ant)
            else:
                duplicates_in_this_group = True
            index += 1

        if not duplicates_in_this_group:
            group.append(groups_not_duplicated)

    return groups_not_duplicated


def generate_ants_a_group(ant_structure, team):
    """Genreate a list of ants close to each other. (ally)

    Parameters
    ----------
    ant_structure: the structure containing the ants (list)
    team : your team number (int)

    Return
    ------
    close_ant: a list which contain group of ally ants (list)

    Version
    -------
    specification: Liam Letot (v.1 19/04/21)
    implementation: Liam Letot (v.1 03/05/21b)
    """
    ennemies, allies = seperate_ally_and_ennemy_ants(ant_structure, team)

    groups = []

    for ant in allies:
        current_group = []
        for ant_to_check in allies:
            if ant['id'] != ant_to_check['id']:
                ant_pos = (ant['pos_y'], ant['pos_x'])
                ant_to_check_pos = (ant_to_check['pos_y'], ant_to_check['pos_x'])
                if compute_distance(ant_pos, ant_to_check_pos) <= 5:
                    current_group.append(ant['id'])

        groups.append(current_group)

    already_seen = []
    groups_not_duplicated = []
    for group in groups:
        duplicates_in_this_group = False
        index = 0
        while not duplicates_in_this_group and len(group) < index:
            ant_id = group[index]
            if not ant_id in already_seen:
                already_seen.append(ant)
            else:
                duplicates_in_this_group = True
            index += 1

        if not duplicates_in_this_group:
            group.append(groups_not_duplicated)

    return groups_not_duplicated

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
    for y in range(main_structure):
        for x in range(main_structure[0]):
            if main_structure[y][x]['clod'] != None:
                clod = (y,x)
                dist = compute_distance(anthill_pos, clod)
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
    anthill_structure: list of 2 elements containing the anthills information (list) 
    team: team : your team number (int)

    return
    ------
    steal_time: the number of turn to steal a mud (int)

    Version
    -------
    specification: Liam Letot (v.1 19/04/21)
    implementation: Martin Buchet (v.1 23/04/21)
    """

    ant = main.return_ant_by_id(ant_structure, ant_id)
    ennemy_team = get_ennemy_team(team)

    ennemy_anthill = anthill_structure[ennemy_team - 1]
    return compute_distance((ant['pos_y'], ant['pos_x']), (ennemy_anthill['pos_y'], ennemy_anthill['pos_x'])) 

def get_closest_clod(ant_structure, main_structure, ant_id):
    """Get the position of the closest mud from an ally ant.
    
    Parameters
    ----------
    ant_structure: structure containing all the ants (list)
    main_structure: main structure of the game board (list)
    ant_id: allied ant close to a mud (int)

    Returns
    -------
    closest_clod: position of the closest clod (tupple)

    Version
    -------
    specification: Maxime Dufrasne (v.1 18/4/21)
    implementation: Liam Letot (v.1 20/04/21)
    """
    ant_pos = (ant_structure[ant_id]['pos_y'],ant_structure[ant_id]['pos_x'])
    distance =100
    for y in main_structure:
        for x in main_structure[y]:
            if main_structure[y][x]['clod'] != None:
                clod= (y,x)
                dist = compute_distance(ant_pos, clod)
                if dist < distance:
                    distance = dist
                    closest_clod = clod
    return closest_clod

def seperate_ally_and_ennemy_ants(ant_structure, team):
    """Creates two list with the allies and ennemies ants.

    Parameters
    ----------
    ant_structure: list of all the ants (list) 
    team: which team are we, 1 or 2 (int)

    Returns
    -------
    enemy_ants: list of all the enemy ants (list) 
    ally_ants: list of all allied ants (list) 

    Version
    -------
    specification: Martin Buchet (v.1 19/04/21)  
    implementation: Youlan Collard 
    """
    allies = []
    enemies = []

    for ant in ant_structure:
        if ant['team'] == team:
            allies.append(ant)
        else:
            enemies.append(ant)
    
    return enemies, allies

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

def compute_ennemies_ants_near_anthill(anthill_structure, team, ant_structure):
    """Compute the number of ennemies near anthills

    Parameters
    ----------
    anthill_structure: structure containing both anthills (list)
    team: team number of our ai (int)
    ant_structure: structure containing all the ants (list)

    Returns
    -------
    ennemy_number: number of ennemies close to anthills (int)

    Version
    -------
    specification: Youlan Collard (v.1)
    implementation: Youlan Collard (v.1)
    
    """

    ally_anthill = anthill_structure[team - 1]
    ally_anthill_pos = (ally_anthill['pos_y'], ally_anthill['pos_x'])

    ennemies, allies = seperate_ally_and_ennemy_ants(ant_structure, team)

    ennemy_number = 0

    for ant in ennemies:
        ant_pos = (ant['pos_y'], ant['pos_x'])
        if compute_distance(ally_anthill_pos, ant_pos) <= 8:
            ennemy_number += 1

    return ennemy_number

def define_ants_type(allies, enemies, main_structure, danger, anthill_structure, ant_structure, team, ant_id):
    """Define the type of each ally ants (attack, collect, stealer, defense).
    
    Parameters
    ----------
    allies: list of all allied ants (list) 
    enemies: list of all enemy ants (list)
    main_structure: main structure of the game board (list)
    danger: current danger value of the game (int)
    anthill_structure: list of 2 elements containing the anthills information (list) 
    ant_structure: structure containing all the ants (list) 
    team: team number of our ai (int)
    ant_id: id of the ant who wants to steal (int)

    Returns
    -------
    updated_allied_ants: list of all allied ants with their defined types (dict) 

    Version
    -------
    specification: Martin Buchet (v.1 19/04/21)
    implementation: Martin Buchet (v.1 27/04/21)

    """
    updated_allied_ants = []

    defense_ants = compute_defense_ants(anthill_structure, ant_structure, team)

    steal_time = compute_clods_steal_time(ant_structure, main_structure, ant_id, anthill_structure, team)

    fight_point = compute_fight_worth(ant_structure, allies)

    if len(defense_ants['other_team']) >= len(defense_ants['team']) and steal_time >= 10:
        for ants in defense_ants:
            updated_allied_ants[ant_id] = 'defense'
    elif danger >= 30:  
        for ants in defense_ants:
            updated_allied_ants[ant_id] = 'defense'
    elif len(defense_ants['other_team']) < len(defense_ants['team']) and steal_time < 10:
        for ants in defense_ants:
            updated_allied_ants[ant_id] = 'stealer'

    if fight_point >= 20:
        updated_allied_ants[]

        

def define_action_for_ant(ants, danger):
    """Define the action a particular ant will do this turn.

    Parameters
    ----------
    ant: specified ant (dict)
    danger: current danger value of the game

    Returns
    -------
    order: order to execute (dict)

    Version
    -------
    specification: Youlan Collard (v.1 19/04/21)
    
    """

    collectors = []
    attackers = []
    defensers = []
    stealers = []

    for ant in ants:
        ant_type = ants_type[ant['id']]
        if ant_type == 'collect':
            collectors.append(ant)
        elif ant_type == 'attack':
            attackers.append(ant)
        elif ant_type == 'defensers':
            defensers.append(ant)
        elif ant_type == 'stealers':
            stealers.append(ant)


    collectors_order_list = define_collect_order(collectors, danger)
    attackers_order_list = define_attack_order(attackers, danger)
    defensers_order_list = define_defense_order(defensers, danger)
    stealers_order_list = define_stealer_order(stealers, danger)

    return collectors_order_list + attackers_order_list + defensers_order_list + stealers_order_list
    
def define_collect_order(main_structure, ants):
    """Define the order to give to a collector ant

    Parameters
    ----------
    ants: ants to which give the order (list)
    danger: danger value (int)

    Returns
    -------
    order_list: dictionnary describing the order (list)

    Version
    -------
    specification: Youlan Collard
    
    """
    already_taken_clods = []

    for ant in ants:



def define_defense_order(ants):
    """Define the order to give to a defense ant

    Parameters
    ----------
    ants: ants to which give the order (list)
    danger: danger value (int)

    Returns
    -------
    order_list: dictionnary describing the order (list)

    Version
    -------
    specification: Youlan Collard
    """
    pass

def define_attack_order(ants):
    """Define the order to give to a defense ant

    Parameters
    ----------
    ants: ants to which give the order (list)
    danger: danger value (int)

    Returns
    -------
    order_list: dictionnary describing the order (list)

    Version
    -------
    specification: Youlan Collard
    """
    pass

def define_stealer_order(ants):
    """Define the order to give to a stealer ant

    Parameters
    ----------
    ants: ants to which give the order (list)
    danger: danger value (int)

    Returns
    -------
    order_list: dictionnary describing the order (list)

    Version
    -------
    specification: Youlan Collard
    
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
    ant_pos_y = order['origin'][0]
    ant_pos_x = order['origin'][1]

    if order['type'] == ('attack' or 'move'):
        target_pos_y = order['target'][0]
        target_pos_x = order['target'][1]

    orders = str(ant_pos_y + 1) + '-' + str(ant_pos_x +1)
    if order['type'] == 'drop':
        orders += ':drop '
    elif order['type'] == 'lift':
        orders += ':lift '
    elif order['type'] == 'move':
        orders += ':@' + str(target_pos_y + 1) + '-' + str(target_pos_x + 1) + ' '
    elif order['type'] == 'attack':
        orders += ':*' + str(target_pos_y + 1) + '-' + str(target_pos_x + 1) + ' '

    return orders

# Util function
def compute_distance(origin, destination):
    """compute distance between an ant and an anthill

    Parameters
    ----------
    origin: point of origin (tupple)
    destination: destination (tupple)

    Return
    ------
    distance: distance in number of moves between the ant and the anthill (int)

    Version
    -------
    specification: Martin Buchet, Youlan Collard (v.1 01/05/21)
    implementation: Martin Buchet, Youlan Collard (v.1 01/05/21)
    """
    return max(abs(origin[0] - destination[0]), abs(origin[1] - destination[1]))

def get_ennemy_team(team):
    """Return the number of the ennemy team

    Parameters
    ----------
    team: number of the team of our ai (int)

    Returns
    -------
    ennemy_team_number: number of the ennemy team
    
    Version
    -------
    """
    if team == 1:
        return 2
    else:
        return 1

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
    danger = compute_danger(anthill_structure, ant_structure, player_id)
    ennemies, allies = seperate_ally_and_ennemy_ants(ant_structure, player_id)

    ants_type = define_ants_type(allies, ennemies, main_structure, danger)

    orders = ''

    for ant in allies:
        ant_type = ants_type[ant['id']]
        order_dict = define_action_for_ant(ant, ant_type, danger)
        orders += generate_order(order_dict)
    
    return orders
