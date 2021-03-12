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
    implementation: Youlan Collard (v.1 26/02/21)
    
    """

    fh = open(path, 'r')
    lines = fh.readlines()
    fh.close()

    board_size = lines[1].split(' ')

    anthills_pos = []

    for line_index in range(3, 5):
        anthill_pos = lines[line_index].split(' ')
        for index in range(len(anthill_pos)):
            anthill_pos[index] = int(anthill_pos[index]) - 1
        anthills_pos.append(anthill_pos)
    
    clods_info = []

    for line_index_clods in range(6, len(lines)):
        clod_info = lines[line_index_clods].split(' ')
        for index in range(2):
            clod_info[index] = int(clod_info[index]) - 1
        clod_info[2] = int(clod_info[index])
        clods_info.append(clod_info)

    return board_size, anthills_pos, clods_info

def create_map(board_size, anthills, clods):
    """Create the data structure for the map and returns it.

    Parameters
    ----------
    board_size: Size of the game board (tuple)
    anthills: Anthills's positions (list)
    clods: clods's informations (list)

    Returns
    -------
    main_structure: main structure for the map (list)
    ant_structure: list of existing ants (list)
    anthill_structure: list of 2 elements containing the anthills information (list)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21) (v.2 26/02/21) 
    implementation: Youlan Collard
    """
    main_structure = []
    for x in range(int(board_size[0])):
        row = []
        for y in range(int(board_size[1])):
            cell = {
                'ant': None,
                'dirt': None
            }
            row.append(cell)
        main_structure.append(row)
    
    for clod in clods:
        main_structure[clod[0]][clod[1]]['dirt'] = clod[2]

    # TODO: anthill structure
    # TODO: Add 2 first ants to ant structure

    anthill_structure = [
        {
            'team': 1,
            'pos_x': anthills[0][0],
            'pos_y': anthills[0][1]
        },
        {
            'team': 2,
            'pos_x': anthills[1][0],
            'pos_y': anthills[1][1]
        }
    ]

    # Maybe replace that with spawn func
    ant_structure = [
        {
            'id': 0,
            'team': 1,
            'health': 3,
            'level': 1,
            'carrying': False,
            'dirt_force': None
        },
        {
            'id': 1,
            'team': 2,
            'health': 3,
            'level': 1,
            'carrying': False,
            'dirt_force': None
        }
    ]

    main_structure[anthill_structure[0]['pos_x']][anthill_structure[0]['pos_y']]['ant'] = 0
    main_structure[anthill_structure[1]['pos_x']][anthill_structure[1]['pos_y']]['ant'] = 1

    return main_structure, ant_structure, anthill_structure
        

    
    

# Victory function
def check_victory(main_structure, anthill_structure, number_of_turn):
    """Check if one of the player has win the game and returns the number of the team who has won.

    Parameters
    ----------
    main_structure: main structure of the game, containing the map (list)
    anthill_structure: 
    number_of_turn: The number of turn for this game (int)

    Return
    ------
    won: number of the team who has won, None if nobody has (int)
    

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21). Maxime Dufrasne (v.2 05/03/21)
    implementation: Maxime Dufrasne (v.1 09/03/21)
    
    """
    if number_of_turn > 200:
        return None

    nbr_dirt_pl_1, nbr_dirt_pl_2 = check_dirt(main_structure)

    if nbr_dirt_pl_1 == 8 and nbr_dirt_pl_2 < 8:
        return 1
    elif nbr_dirt_pl_1 < 8 and nbr_dirt_pl_2 == 8:
        return 2
    else:
        return None

def check_dirt(main_structure):
    """Check the number of dirt around anthill

    Parameter
    ----------
    main_structure: main structure of the game, containing the map (list)
    anthill_structure: (list)

    Return
    -------
    nbr_dirt_pl_1: Number of dirt player 1 has around his anthill (int)
    nbr_dirt_pl_2: Number of dirt player 2 has around his anthill (int)


    Version
    --------
    specification: Maxime Dufrasne (v.1 05/02/21)
    implemmentation: Maxime Dufrasne (v.1 09/02/21)
    """
    # TODO: Faudrait la position des deux anthills je pense

    # dirt_1, dirt_2 = 0, 0
    # anthill_1, anthill_2 = recup les deux positions
    around = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    # for all pos in around:
    #        if anthill_1 + pos est une dirt:
    #            dirt_1 += 1
    #        if anthill_2 + pos est une dirt:
    #            dirt_2 += 2
    #
    # return dirt_1, dirt_2

    pass

# Validation of orders
def interpret_order(team, main_structure, ant_structure, orders):
    """Take an input, check if it's a true fonction and if it's possible, if both conditions are met, return True , if not, return False and send an error to the player.

    Parameters
    ----------
    team: number of the team who sent the order (int)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    orders: the input of the user (str)

    Returns
    -------
    order_list: the orders in a list (list)
    
    Version
    -------
    Specification : Letot Liam/Youlan Collard (v.1 18/02/21) (v.2 11/03/21)
    implementation: Youlan Collard (v.1 11/03/21)
    """

    #TODO: Créer un dictionnaire pour les ordres pour ne devoir décoder l'ordre qu'une fois

    orders_list = orders.split(" ")

    seems_valid = [] # Items are [order, type] (type is one of lift, drop, move or attack)

    for order in orders_list:
        if ":" in order:
            order_seperated = order.split(":") # Seperate the first part of the order from the second
            if "-" in order_seperated[0]:
                ant_pos = order_seperated[0].split("-")
                if (len(ant_pos) == 2) and (ant_pos[0].isdigit() and ant_pos[1].isdigit()):
                    if order_seperated[1] == "lift":
                        seems_valid.append([order, "lift"])
                    elif order_seperated[1] == "drop":
                        seems_valid.append([order, "drop"])
                    elif "-" in order_seperated[1]:
                        action_pos = order_seperated[1][1:].split("-")
                        if (len(action_pos) == 2) and (action_pos[0].isdigit() and action_pos[1].isdigit()):
                            if order_seperated[1][0] == "@":
                                seems_valid.append([order, "move"])
                            elif order_seperated[1][0] == "*":
                                seems_valid.append([order, "attack"])

    valid_orders = []

    for seems_valid_order in seems_valid:
        order_seperated = seems_valid_order.split(":")
        ant_pos = order_seperated[0].split("-")
        if seems_valid_order[1] == "move":
            move_to = order_seperated[1][1:].split("-")
            if validation_move(team, ant_pos, move_to, main_structure, ant_structure):
                valid_orders.append(seems_valid_order)
        elif seems_valid_order[1] == "attack":
            attack_to = order_seperated[1][1:].split("-")
            if validation_attack(team, ant_pos, attack_to):
                valid_orders.append(seems_valid_order)
        elif seems_valid_order[1] == "lift":
            if validation_lift(team, ant_pos, main_structure, ant_structure):
                valid_orders.append(seems_valid_order)
        elif seems_valid_order[1] == "drop":
            valid_orders.append(seems_valid_order)

    return valid_orders


def validation_lift(team, ant_pos, main_structure, ant_structure):
    """Check if an ant has the force to carry clod and if there is clod where it is.
    
    Parameters
    ----------
    team: number of the team who made the order (int)
    ant_pos: position of the ant executing the action (tuple)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)

    Return
    ------
    lift_valid: wether the lifting action is valid or not (bool)

    Version
    -------
    specification: Youlan Collard (v.1 21/02/21) (v.2 11/03/21)

    
    """
    pass

def validation_attack(team, attacker_pos, target_pos):
    """Check if target is in range of the attacker and return a boolean.
    
    Parameters
    ----------
    team: number of the team who made the order (int)
    attacker_pos: position of attacker (list)
    target_pos: position of target (list)
    
    Return
    ------
    is_in_range: wether the target is in range or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/21) (v.2 11/03/21)
    """
    pass

def validation_move(team, origin, destination, main_structure, ant_structure):
    """Check if deplacement is valid and return a boolean.
    
    Parameters
    ----------
    team: number of the team who made the order (int)
    origin: depart position (list)
    destination: destination position (list)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    
    Return
    ------
    move_valid: wether move is valid or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/21) (v.2 11/03/21)
    implementation: Youlan Collard (v.1 12/03/21)
    """
    #TODO: Check if ant doesn't leave board

    origin_tile = main_structure[origin[0] - 1][origin[1] - 1] # -1 because our structure is 0 indexed and the game is 1 indexed
    ant_id = origin_tile['ant']
    ant = return_ant_by_id(ant_structure, ant_id)
    if ant['team'] == team:
        around = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for relative in around:
            if origin[0] + relative[0] == destination[0] and origin[1] + relative[1] == destination[1]:
                return True

    return False


# Execution of orders
def exec_order(order_list, main_structure, ant_structure):
    """Execute orders and give the structures to each order fonctions.

    Parameters
    ---------
    order_list: the list of orders the user imput (list)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)

    Notes
    -----
    order_list has been parsed by interpret order already when it reaches this function
    the format of the order_list's item is [order, type] 

    Version
    -------
    specification: Maxime Dufrasne, Liam Letot, Youlan Collard (v.1 19/02/21) (v.2 26/02/21) (v.3 11/03/21)
    implementation: Youlan Collard (v.1 12/03/21)
    """

    #TODO: Order the list (lift, drop, attack, move)

    for order in order_list:
        if order[1] == "move":
            order_seperated = order[0].split(":")
            origin = order_seperated[0].split("-")
            destination = order_seperated[1][1:].split("-")
            move(main_structure, origin, destination)
        elif order[1] == "attack":
            order_seperated = order[0].split(":")
            attacker = order_seperated[0].split("-")
            attacked = order_seperated[1][1:].split("-")
            attack(ant_structure, main_structure, attacker, attacked)
        elif order[1] == "lift":
            order_seperated = order[0].split(":")
            ant_pos = order_seperated[0].split("-")
            lift(main_structure, ant_structure, ant_pos)
        elif order[1] == "drop":
            order_seperated = order[0].split(":")
            ant_pos = order_seperated[0].split("-")
            place(main_structure, ant_structure, ant_pos)

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

def attack(ant_structure, main_structure, ant_pos, target_pos):
    """Compute damage done.

    Parameters
    ----------
    ant_structure: structure containing the ants (list)
    main_structure: main structure of the game board (list)
    ant_pos: position of the attacking ant (list)
    target_pos: position of target (list)

    Version
    -------
    specification: Martin Buchet/Youlan Collard (v.1 18/02/21) (v.2 26/02/21) (v.3 12/03/21)
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
    # Description should be changed
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

    nbr_dirt_pl_1, nbr_dirt_pl_2 = check_dirt(main_structure)
        
    #check the level for team 1
    if anthill['team']== 1:
        if nbr_dirt_pl_1 <= 2:
            level = 1
        elif nbr_dirt_pl_1 <= 5:
            level = 2
        elif nbr_dirt_pl_1 <= 8:
            level = 3
        
    #check the level for team 2
    elif anthill['team']== 2:
        if nbr_dirt_pl_2 <= 2:
            level = 1
        elif nbr_dirt_pl_2 <= 5:
            level = 2
        elif nbr_dirt_pl_2 <= 8:
            level = 3

    return level


def spawn(main_structure, ant_structure, anthill_structure):
    """Spawn ant.

    Parameters
    ----------
    main_structure: library of board (list)
    ant_structure: library of all ants (list)
    anthill_structure: library of all anthills (list)

    Returns
    -------
    main_structure: modified main structure (list)
    ant_structure: modified ant structure (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 18/02/21) (v.2 10/03/21)
    implementation: Liam Letot (v.1 10/03/21)
    """
    for anthill in anthill_structure:
        #check the level the next ant will have
        ant_level = check_level(main_structure, anthill),
        
        #with the level, take the health of the ant
        if ant_level == 1:
            health = 3
        elif ant_level == 2:
            health = 5
        elif ant_level == 3:
            health = 7
    
        #add the nex ant in ant_structure
        ant_structure.append({
            'id': len(ant_structure),
            'team': anthill['team'],
            'health': health,
            'level':  ant_level,
            'carrying': False,
            'dirt_force': None
            })

        #add the new ant in the board (main_structure) 
        main_structure[anthill['pos_x']][anthill['pos_y']]['ant'] = len(ant_structure)-1
    #return the structures
    return main_structure, ant_structure

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
    implementation: Martin Buchet, Youlan Collard (v.1 04/03/21)
    """
    llcorner = "└"
    ulcorner = "┌"
    lrcorner = "┘"
    urcorner = "┐"
    hline = "─"
    bigplus = "┼"
    vline = "│"
    ttee = "┬"
    btee = "┴"
    ltee = "├"
    rtee = "┤"
    space = " "
    row = len(main_structure)
    col = len(main_structure[0])

    print(term.home + term.clear + term.hide_cursor)
    # print grid
    print(term.move(0,0) + ulcorner + (3*hline + ttee)*(col - 1) + 3*hline + urcorner)
    for x in range(row - 1):
        print((vline + 3*space)*col + vline)
        print(ltee + (3*hline + bigplus)*(col - 1) + 3*hline + rtee)
    print((vline + 3*space)*col + vline)
    print(llcorner + (3*hline + btee)*(col - 1) + 3*hline + lrcorner)

def move_ant_on_display(old_position, new_position):
    """Change the position of an ant on the dispay.

    Paremeters
    ----------
    old_position: the old position of an ant (tuple)
    new_position: the new position of an ant (tuple)

    Version
    -------
    specification: Maxime Dufrasne (v.1 22/02/21)
    
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
    specification: Maxime Dufrasne  (v.1 22/02/21)
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

def add_ant_on_display(ant_structure, ant_id, ant_pos):
    """Add an ant on display (game board and health bar).
    
    Parameters
    ----------
    ant_structure: the list with all informations on ants (list)
    ant_id: the id of the new ant (int)
    ant_pos: Position of the ant to add (tuple)
    
    Version
    -------
    specification: Liam Letot (v.1 22/02/21) (v.2 05/03/21)
    """
    

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
    implementation: Youlan Collard (v.1 12/03/21) 
    """
    for ant in ant_structure:
        if ant['id'] == ant_id:
            return ant

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

    
    #init the main parameters
    number_of_turn = 0
    board_size, anthills, clods = parse_map_file(CPX_file)

    init_dispay(main_structure, ant_structure)
    main_structure, ant_structure, anthill_structure = create_map(board_size, anthills, clods)
    
    #if the game is played with AI, take the AI path to execute them
    if type_1 == 'AI':
        AI1_code = input("path to the ia code file")
    if type_2 == 'AI':
        AI2_code = input("path to the ia code file")

        
    #run the game
    
    while check_victory(number_of_turn, main_structure, anthill_structure) == None:
        
        #take the orders
        if type_1 == 'human':
            orders_1 = input("team_1 input")
        #elif type_1 == 'AI':
            #orders = execfile(AI1_code)
        if type_2 == 'human':
            orders_2 = input("team_2 input")
        #elif type_2 == 'AI':
            #orders += execfile(AI2_code)
        
        #check and execute the orders
        orders_list = interpret_order( 1 ,main_structure, ant_structure, orders_1)
        orders_list += interpret_order(2, main_structure, ant_structure, orders_2)
        exec_order(orders_list, main_structure, ant_structure)
        #check and spawn new ant if it's needed
        if number_of_turn % 5 == 0:
            spawn( ant_structure, main_structure, anthill_structure)
        number_of_turn += 1
    #print the end message
    if check_victory == 1:
        print('Team 1 win')
    else:
        print('Team 2 win')

def test():

    board_size, anthills, clods = parse_map_file("./basic.cpx")
    main_structure, ant_structure, anthills_structure = create_map(board_size, anthills, clods)
    init_dispay(main_structure, ant_structure, anthills_structure)
    print(len(main_structure))

    print(term.move(1, 3) + "⚇")
test()
