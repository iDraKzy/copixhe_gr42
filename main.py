#-*- coding: utf-8 -*-

import blessed, math, os, time, random, sys
term = blessed.Terminal()

"""Module providing remote play features for UNamur programmation project (INFOB132).

Sockets are used to transmit orders on local or remote machines.
Firewalls or restrictive networks settings may block them.  

More details on sockets: https://docs.python.org/2/library/socket.html.

Author: Benoit Frenay (benoit.frenay@unamur.be).

"""



import socket
# import time


def create_server_socket(local_port, verbose):
    """Creates a server socket.
    
    Parameters
    ----------
    local_port: port to listen to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: server socket (socket.socket)
    
    """
    
    socket_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_in.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state

    if verbose:
        print(' binding on local port %d to accept a remote connection' % local_port)
    
    try:
        socket_in.bind(('', local_port))
    except:
        raise IOError('local port %d already in use by your group or the referee' % local_port)
    socket_in.listen(1)
    
    if verbose:
        print('   done -> can now accept a remote connection on local port %d\n' % local_port)
        
    return socket_in


def create_client_socket(remote_IP, remote_port, verbose):
    """Creates a client socket.
    
    Parameters
    ----------
    remote_IP: IP address to send to (int)
    remote_port: port to send to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_out: client socket (socket.socket)
    
    """

    socket_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_out.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state
    
    connected = False
    msg_shown = False
    
    while not connected:
        try:
            if verbose and not msg_shown:
                print(' connecting on %s:%d to send orders' % (remote_IP, remote_port))
                
            socket_out.connect((remote_IP, remote_port))
            connected = True
            
            if verbose:
                print('   done -> can now send orders to %s:%d\n' % (remote_IP, remote_port))
        except:
            if verbose and not msg_shown:
                print('   connection failed -> will try again every 100 msec...')
                
            time.sleep(.1)
            msg_shown = True
            
    return socket_out
    
    
def wait_for_connection(socket_in, verbose):
    """Waits for a connection on a server socket.
    
    Parameters
    ----------
    socket_in: server socket (socket.socket)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: accepted connection (socket.socket)
    
    """
    
    if verbose:
        print(' waiting for a remote connection to receive orders')
        
    socket_in, remote_address = socket_in.accept()
    
    if verbose:
        print('   done -> can now receive remote orders from %s:%d\n' % remote_address)
        
    return socket_in            


def create_connection(your_group, other_group=0, other_IP='127.0.0.1', verbose=False):
    """Creates a connection with a referee or another group.
    
    Parameters
    ----------
    your_group: id of your group (int)
    other_group: id of the other group, if there is no referee (int, optional)
    other_IP: IP address where the referee or the other group is (str, optional)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    Raises
    ------
    IOError: if your group fails to create a connection
    
    Notes
    -----
    Creating a connection can take a few seconds (it must be initialised on both sides).
    
    If there is a referee, leave other_group=0, otherwise other_IP is the id of the other group.
    
    If the referee or the other group is on the same computer than you, leave other_IP='127.0.0.1',
    otherwise other_IP is the IP address of the computer where the referee or the other group is.
    
    The returned connection can be used directly with other functions in this module.
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')
        
    # check whether there is a referee
    if other_group == 0:
        if verbose:
            print('** group %d connecting to referee on %s **\n' % (your_group, other_IP))
        
        # create one socket (client only)
        socket_out = create_client_socket(other_IP, 42000+your_group, verbose)
        
        connection = {'in':socket_out, 'out':socket_out}
        
        if verbose:
            print('** group %d successfully connected to referee on %s **\n' % (your_group, other_IP))
    else:
        if verbose:
            print('** group %d connecting to group %d on %s **\n' % (your_group, other_group, other_IP))

        # create two sockets (server and client)
        socket_in = create_server_socket(42000+your_group, verbose)
        socket_out = create_client_socket(other_IP, 42000+other_group, verbose)
        
        socket_in = wait_for_connection(socket_in, verbose)
        
        connection = {'in':socket_in, 'out':socket_out}

        if verbose:
            print('** group %d successfully connected to group %d on %s **\n' % (your_group, other_group, other_IP))
        
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return connection
        
        
def bind_referee(group_1, group_2, verbose=False):
    """Put a referee between two groups.
    
    Parameters
    ----------
    group_1: id of the first group (int)
    group_2: id of the second group (int)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connections: sockets to receive/send orders from both players (dict)
    
    Raises
    ------
    IOError: if the referee fails to create a connection
    
    Notes
    -----
    Putting the referee in place can take a few seconds (it must be connect to both groups).
        
    connections contains two connections (dict of socket.socket) which can be used directly
    with other functions in this module.  connection of first (second) player has key 1 (2).
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')

    # create a server socket (first group)
    if verbose:
        print('** referee connecting to first group %d **\n' % group_1)        

    socket_in_1 = create_server_socket(42000+group_1, verbose)
    socket_in_1 = wait_for_connection(socket_in_1, verbose)

    if verbose:
        print('** referee succcessfully connected to first group %d **\n' % group_1)        
        
    # create a server socket (second group)
    if verbose:
        print('** referee connecting to second group %d **\n' % group_2)        

    socket_in_2 = create_server_socket(42000+group_2, verbose)
    socket_in_2 = wait_for_connection(socket_in_2, verbose)

    if verbose:
        print('** referee succcessfully connected to second group %d **\n' % group_2)        
    
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return {1:{'in':socket_in_1, 'out':socket_in_1},
            2:{'in':socket_in_2, 'out':socket_in_2}}


def close_connection(connection):
    """Closes a connection with a referee or another group.
    
    Parameters
    ----------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    """
    
    # get sockets
    socket_in = connection['in']
    socket_out = connection['out']
    
    # shutdown sockets
    socket_in.shutdown(socket.SHUT_RDWR)    
    socket_out.shutdown(socket.SHUT_RDWR)
    
    # close sockets
    socket_in.close()
    socket_out.close()
    
    
def notify_remote_orders(connection, orders):
    """Notifies orders to a remote player.
    
    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
    orders: orders to notify (str)
        
    Raises
    ------
    IOError: if remote player cannot be reached
    
    """

    # deal with null orders (empty string)
    if orders == '':
        orders = 'null'
    
    # send orders
    try:
        connection['out'].sendall(orders.encode())
    except:
        raise IOError('remote player cannot be reached')


def get_remote_orders(connection):
    """Returns orders from a remote player.

    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
        
    Returns
    ----------
    player_orders: orders given by remote player (str)

    Raises
    ------
    IOError: if remote player cannot be reached
            
    """
   
    # receive orders    
    try:
        orders = connection['in'].recv(65536).decode()
    except:
        raise IOError('remote player cannot be reached')
        
    # deal with null orders
    if orders == 'null':
        orders = ''
        
    return orders


# Initialize data structure
def parse_map_file(path):
    """Parse the information from the cpx file.

    Parameters
    ----------
    path: path to the cpx file containing the map information (str)

    Returns
    -------
    board_size: Size of the board (list)
    antthills: Anthills's positions (list)
    clods: clods's positions (list)

    Version
    -------
    specification: Youlan Collard (v.1 26/02/21) (v.2 12/03/21)
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
        clod_info[2] = int(clod_info[2])
        clods_info.append(clod_info)

    return board_size, anthills_pos, clods_info

def create_map(board_size, anthills, clods):
    """Create the data structure for the map and returns it.

    Parameters
    ----------
    board_size: Size of the game board (list)
    anthills: Anthills's positions (list)
    clods: clods's informations (list)

    Returns
    -------
    main_structure: main structure for the map (list)
    ant_structure: list of existing ants (list)
    anthill_structure: list of 2 elements containing the anthills information (list)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21) (v.2 26/02/21) (v.3 12/03/21)
    implementation: Youlan Collard (v.1 26/02/21)
    """
    main_structure = []
    for y in range(int(board_size[0])):
        row = []
        for x in range(int(board_size[1])):
            cell = {
                'ant': None,
                'clod': None
            }
            row.append(cell)
        main_structure.append(row)
    
    for clod in clods:
        main_structure[clod[0]][clod[1]]['clod'] = clod[2]

    anthill_structure = [
        {
            'team': 1,
            'pos_x': anthills[0][1],
            'pos_y': anthills[0][0]
        },
        {
            'team': 2,
            'pos_x': anthills[1][1],
            'pos_y': anthills[1][0]
        }
    ]

    ant_structure = []

    return main_structure, ant_structure, anthill_structure

# Victory function
def check_victory(main_structure, anthill_structure, number_of_turn):
    """Check if one of the player has win the game and returns the number of the team who has won.

    Parameters
    ----------
    main_structure: main structure of the game, containing the map (list)
    anthill_structure: list of 2 elements containing the anthills information (list)
    number_of_turn: The number of turn for this game (int)

    Returns
    -------
    won: number of the team who has won, None if nobody has (int)
    

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21). Maxime Dufrasne (v.2 05/03/21)
    implementation: Maxime Dufrasne (v.1 09/03/21)
    
    """
    if number_of_turn > 200:
        return 3

    nbr_clod_pl_1, nbr_clod_pl_2 = check_clod(main_structure, anthill_structure)

    if nbr_clod_pl_1 == 8 and nbr_clod_pl_2 < 8:
        return 1
    elif nbr_clod_pl_1 < 8 and nbr_clod_pl_2 == 8:
        return 2
    else:
        return None

def check_clod(main_structure, anthill_structure):
    """Check the number of clod around anthill

    Parameters
    ----------
    main_structure: main structure of the game, containing the map (list)
    anthill_structure: list of 2 elements containing the anthills information (list)

    Returns
    -------
    nbr_clod_pl_1: Number of clod player 1 has around his anthill (int)
    nbr_clod_pl_2: Number of clod player 2 has around his anthill (int)


    Version
    --------
    specification: Maxime Dufrasne (v.1 05/02/21)
    implemmentation: Maxime Dufrasne (v.1 09/02/21)
    """

    clod_numbers = [0, 0]

    around = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    for pos in around:
        for anthill in anthill_structure:
            pos_y = pos[0] + anthill['pos_y']
            pos_x = pos[1] + anthill['pos_x']
            if main_structure[pos_y][pos_x]['clod']:
                clod_numbers[anthill['team'] - 1] += 1
    
    return clod_numbers[0], clod_numbers[1]

def sort_orders(orders):
    """Sort the orders by priority given by game rules

    Parameters
    ----------
    orders: list of unsorted orders (list)

    Returns
    -------
    sorted_orders: the sorted list of orders
    
    Version
    -------
    specification: Youlan Collard (v.1 25/03/21)
    implementation: Youlan Collard (v.1 25/03/21)
    """
    
    sorted_orders = []

    clods_orders = []
    attack_orders = []
    move_orders = []

    for order in orders:
        if order['type'] == 'lift' or order['type'] == 'drop':
            clods_orders.append(order)
        elif order['type'] == 'attack':
            attack_orders.append(order)
        elif order['type'] == 'move':
            move_orders.append(order)

    # ? Pas très joli si vous avez une meilleure idée je suis preneur xD
    team_1_clod, team_2_clod = seperate_team_orders(clods_orders)

    sorted_orders += team_1_clod
    sorted_orders += team_2_clod

    team_1_attack, team_2_attack = seperate_team_orders(attack_orders)

    sorted_orders += team_1_attack
    sorted_orders += team_2_attack

    team_1_move, team_2_move = seperate_team_orders(move_orders)

    sorted_orders += team_1_move
    sorted_orders += team_2_move

    return sorted_orders
        

# Util function for sort_orders
def seperate_team_orders(orders):
    """Seperate a list of orders into two list for each teams

    Parameters
    ----------
    orders: list of orders to be seperated

    Returns
    -------
    orders_team_1: the orders specific to team 1
    orders_team_2: the orders specific to team 2

    Version
    -------
    specification: Youlan Collard (v.1 25/03/21)
    implementaion: Youlan Collard (v.1 25/03/21)
    """
    team_1, team_2 = [], []

    for order in orders:
        if order['team'] == 1:
            team_1.append(order)
        else:
            team_2.append(order)
    
    return team_1, team_2

# Validation of orders
def interpret_order(main_structure, ant_structure, anthill_structure, orders):
    """Take an input, check if it's a true fonction and if it's possible, if both conditions are met, return True , if not, return False and send an error to the player.

    Parameters
    ----------
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    anthill_structure: list of 2 elements containing the anthills information (list)
    orders: the input of the user (str)

    Returns
    -------
    order_list: the orders in a list (list)

    Notes
    -----
    All orders should be sent in a single string with the first and second team's orders seperated by a ;
    
    Version
    -------
    Specification : Letot Liam/Youlan Collard (v.1 18/02/21) (v.2 11/03/21)
    implementation: Youlan Collard (v.1 11/03/21)
    """


    orders_list = orders.split(';')
    seems_valid = [] 
    team_number = 0 # initialize the number team to 0

    for team in orders_list:
        team_number += 1 # increment it at the beginning of the loop (so it's 1 for the first iteration and 2 for the second)
        for order in team.split(' '):
            order_dict = {}
            order_dict['team'] = team_number
            if ':' in order:
                order_seperated = order.split(':') # Seperate the first part of the order from the second
                if '-' in order_seperated[0]:
                    ant_pos = order_seperated[0].split('-')
                    if (len(ant_pos) == 2) and (ant_pos[0].isdigit() and ant_pos[1].isdigit()):
                        order_dict['origin'] = (int(ant_pos[0]) - 1, int(ant_pos[1]) - 1) # -1 to both because our game board is 0 indexed and the game is 1 indexed
                        if order_seperated[1] == 'lift':
                            order_dict['type'] = 'lift'
                            order_dict['target'] = None
                            seems_valid.append(order_dict)
                        elif order_seperated[1] == 'drop':
                            order_dict['type'] = 'drop'
                            order_dict['target'] = None
                            seems_valid.append(order_dict)
                        elif "-" in order_seperated[1]:
                            action_pos = order_seperated[1][1:].split('-')
                            if (len(action_pos) == 2) and (action_pos[0].isdigit() and action_pos[1].isdigit()):
                                order_dict['target'] = (int(action_pos[0]) - 1, int(action_pos[1]) - 1)
                                if order_seperated[1][0] == '@':
                                    order_dict['type'] = 'move'
                                    seems_valid.append(order_dict)
                                elif order_seperated[1][0] == '*':
                                    order_dict['type'] = 'attack'
                                    seems_valid.append(order_dict)


    seems_valid = sort_orders(seems_valid) # Sorting the orders before the final verification because moves actions are always sensitive to the order

    valid_orders = []

    for seems_valid_order in seems_valid:
        origin = seems_valid_order['origin']
        ant_id = main_structure[origin[0]][origin[1]]['ant']
        ant = return_ant_by_id(ant_structure, ant_id)
        if ant != None:
            if not ant['played']:
                ant['played'] = True
                if seems_valid_order['type'] == 'move':
                    if validation_move(seems_valid_order['team'], seems_valid_order['origin'], seems_valid_order['target'], main_structure, ant_structure, anthill_structure):
                        already_used_square = []
                        for order in valid_orders:
                            if order['type'] == 'move':
                                already_used_square.append(order['target'])

                        if not seems_valid_order['target'] in already_used_square:
                            valid_orders.append(seems_valid_order)
                elif seems_valid_order['type'] == 'attack':
                    if validation_attack(seems_valid_order['team'], main_structure, ant_structure, seems_valid_order['origin'], seems_valid_order['target']):
                        valid_orders.append(seems_valid_order)
                elif seems_valid_order['type'] == 'lift':
                    if validation_lift(seems_valid_order['team'], seems_valid_order['origin'], main_structure, ant_structure):
                        valid_orders.append(seems_valid_order)
                elif seems_valid_order['type'] == 'drop':
                    if validation_drop(main_structure, ant_structure, seems_valid_order['team'], seems_valid_order['origin']):
                        valid_orders.append(seems_valid_order)

    return valid_orders

def validation_drop(main_structure, ant_structure, team, ant_pos):
    """Check if a drop action is valid
    
    Parameters
    ----------
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    team: number of the team who made the order (int)
    ant_pos: position of the ant executing the action (tuple)

    Returns
    -------
    drop_valid: wether the drop action is valid (bool)

    Versions
    --------
    specification: Youlan Collard (v.1 19/03/21)
    implementation: Youlan Collard (v.1 23/03/21)
    
    """
    ant_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']
    if ant_id is None:
        return False
    ant = return_ant_by_id(ant_structure, ant_id)

    if ant['health'] <= 0:
        return False

    if ant['team'] == team and ant['carrying']:
        return True
    
    return False

def validation_lift(team, ant_pos, main_structure, ant_structure):
    """Check if an ant has the force to carry clod and if there is clod where it is.
    
    Parameters
    ----------
    team: number of the team who made the order (int)
    ant_pos: position of the ant executing the action (tuple)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)

    Returns
    -------
    lift_valid: wether the lifting action is valid or not (bool)

    Version
    -------
    specification: Youlan Collard (v.1 21/02/21) (v.2 11/03/21)(v.3 12/03/21)
    implementation: Martin Buchet (v.1 18/03/21)
    
    """
    #TODO: For All Validation: check if the ant has already done an action this turn
    lift_valid = False
    ant_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']
    if ant_id is None:
        return False
    ant = return_ant_by_id(ant_structure, ant_id)

    if ant['health'] <= 0:
        return False

    if main_structure[ant_pos[0]][ant_pos[1]]['ant'] is not None:

        # get ant_id from ant_pos then get the ant dict

        # check team and if ant is strong enough and if there is a clod
        if team == ant['team']:
            if main_structure[ant_pos[0]][ant_pos[1]]['clod']:
                if ant['level'] >= main_structure[ant_pos[0]][ant_pos[1]]['clod']:

                    lift_valid = True
        
    return lift_valid

def validation_attack(team, main_structure, ant_structure, attacker_pos, target_pos):
    """Check if target is in range of the attacker and return a boolean.
    
    Parameters
    ----------
    team: number of the team who made the order (int)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    attacker_pos: position of attacker (tuple)
    target_pos: position of target (tuple)
    
    Return
    ------
    is_in_range: wether the target is in range or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/21) (v.2 11/03/21) (v.3 12/03/21)
    implementation: Martin Buchet (v.1 18/03/21)
    """

    is_in_range = False

    # get ant_id from ant_pos then get the ant dict
    ant_id = main_structure[attacker_pos[0]][attacker_pos[1]]['ant']
    if ant_id is None:
        return False

    ant = return_ant_by_id(ant_structure, ant_id)

    if ant['health'] <= 0:
        return False

    ant_targeted = main_structure[target_pos[0]][target_pos[1]]['ant']

    if main_structure[attacker_pos[0]][attacker_pos[1]]['ant'] and ant_targeted:

        # compute distance between ants
        range_x = target_pos[0] - attacker_pos[0]
        range_y = target_pos[1] - attacker_pos[1]

        # check if the attacker ant belong to the team giving the order then check range
        if team == ant['team']:
            if (range_x <= 3 and range_x >= -3) and (range_y <= 3 and range_y >= -3):
                is_in_range = True

    return is_in_range

def validation_move(team, origin, destination, main_structure, ant_structure, anthill_structure):
    """Check if deplacement is valid and return a boolean.
    
    Parameters
    ----------
    team: number of the team who made the order (int)
    origin: depart position (tuple)
    destination: destination position (tuple)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    anthill_structure: list of 2 elements containing the anthills information (list)
    
    Returns
    -------
    move_valid: wether move is valid or not (bool)
    
    Version
    -------
    specification: Martin Buchet (v.1 21/02/21) (v.2 11/03/21)
    implementation: Youlan Collard, Martin Buchet (v.1 12/03/21)
    """

    if (destination[0] >= len(main_structure) or destination[0] < 0) or (destination[1] >= len(main_structure[0]) or destination[1] < 0): # < 0 because the order has already been converted to 0 index
        return False

    origin_tile = main_structure[origin[0]][origin[1]]
    ant_id = origin_tile['ant']
    ant = return_ant_by_id(ant_structure, ant_id)

    if ant_id is None or ant['health'] <= 0:
        return False
    
    if ant['carrying'] and main_structure[destination[0]][destination[1]]['clod']:
        for anthill in anthill_structure:
            if destination[0] == anthill['pos_y'] and destination[1] == anthill['pos_x']:
                return False 
        return False

    if ant['team'] == team:
        offset_origin_x = origin[0] - destination[0]
        offset_origin_y = origin[1] - destination[1] 
        if (offset_origin_x in (-1, 0, 1)) and (offset_origin_y in (-1, 0, 1)) and not (offset_origin_x == 0 and offset_origin_y == 0):
            return True
    elif main_structure[destination[0]][destination[1]]['ant'] != None:
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
    order_list has been parsed by interpret_order and is now a list of dictionnary (containing the attributes:
    origin, target and type)

    Version
    -------
    specification: Maxime Dufrasne, Liam Letot, Youlan Collard (v.1 19/02/21) (v.2 26/02/21) (v.3 11/03/21)
    implementation: Youlan Collard (v.1 12/03/21)
    """

    #TODO: Order the list (lift, drop, attack, move)
    all_dead_ants = []

    for order in order_list:
        antid = main_structure[order['origin'][0]][order['origin'][1]]['ant']
        ant = return_ant_by_id(ant_structure, antid)

        
        if order['type'] == 'move':
            move(main_structure, ant_structure, order['team'], order['origin'], order['target'])
        elif order['type'] == 'attack':
            dead = attack(ant_structure, main_structure, order['origin'], order['target'])
            if dead != None:
                all_dead_ants.append(dead)
        elif order['type'] == 'lift':
            lift(main_structure, ant_structure, order['origin'])
        elif order['type'] == 'drop':
            place(main_structure, ant_structure, order['origin'])

    for dead_ant in all_dead_ants:
        death((dead_ant['pos_y'], dead_ant['pos_x']), main_structure, ant_structure, dead_ant['carrying'])

def lift(main_structure, ant_structure, ant_pos):
    """Lift clod on ants.

    Parameters
    ----------
    main_structure: library of board (list)
    ant_structure: library of all ants (list)
    ant_pos: position of the ant that will lift clod (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21) (v.2 26/02/21)
    implementation: Liam Letot (v.1 12/03/21)
    """
    #search the id of ants in the board
    ant_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']
    #take the ant in the ant_structure
    ant = return_ant_by_id(ant_structure, ant_id)
    #place the clod on the ant
    ant['clod_force'] = main_structure[ant_pos[0]][ant_pos[1]]['clod']
    ant['carrying'] = True
    #remove the clod from the board
    main_structure[ant_pos[0]][ant_pos[1]]['clod'] = None
    #remove the clod on the display 
    lift_clod_on_display(ant_pos, ant_structure, main_structure)

def place(main_structure, ant_structure, ant_pos):
    """Place clod on a case.

    Parameters
    ----------
    main_structure: library of board (list)
    ant_structure: library of all ants (list)
    ant_pos: position of the ant that will place clod (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 19/02/21) (v.2 26/02/21)
    implementation: Liam Letot (v.1 12/03/21)
    """
    #search the id of ants in the board
    ant_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']
    #take the ant in the ant_structure
    ant = return_ant_by_id(ant_structure, ant_id)
    #place the clod on the ground
    clod_force = ant['clod_force']
    main_structure[ant_pos[0]][ant_pos[1]]['clod'] = ant['clod_force']
    ant['carrying'] = False
    #remove the clod from the ant
    ant['clod_force']= None
    #place the clod on the display
    place_clod_on_display(ant_pos, clod_force, main_structure, ant_structure)

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
    implementation: Liam Letot (v.1 12/03/21)
    """
    #search the id of ants in the board
    ant_1_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']
    ant_2_id = main_structure[target_pos[0]][target_pos[1]]['ant']
    #take each ant in the ant_structure
    ant_1 = return_ant_by_id(ant_structure, ant_1_id)
    ant_2 = return_ant_by_id(ant_structure, ant_2_id)

    if ant_2 == None:
        return
    #do the attack
    ant_2["health"] -= ant_1['level']

    update_lifepoint_on_display(ant_2, ant_structure)
    if ant_2['health'] <= 0:
        return ant_2
    
def move(main_structure, ant_structure, team, origin, destination):
    """if move valid return the new position of the ant.

    Parameters
    ----------
    main_structure: main structure containing the game board (list)
    ant_structure: structure containing the ants (list)
    team: number of the team who sent the order (int)
    origin: depart position (list)
    destination: destination position (list)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/21) (v.2 26/02/21)
    implementation: Youlan Collard, Liam Letot (v.1 12/03/21)
    """
    # Description should be changed

    ant_id = main_structure[origin[0]][origin[1]]['ant']
    ant = return_ant_by_id(ant_structure, ant_id)
    main_structure[origin[0]][origin[1]]['ant'] = None
    main_structure[destination[0]][destination[1]]['ant'] = ant_id

    if ant == None:
        return

    ant['pos_y'] = destination[0]
    ant['pos_x'] = destination[1]
    move_ant_on_display(main_structure, ant_id, team, ant['level'],  ant['carrying'], origin, destination)

# New ants functions
def check_level(main_structure, anthill_structure, anthill):
    """Check the level of an anthill and returns it.

    Parameters
    ----------
    main_structure: main structure of the game, containing the map (list)
    anthill_structure: list of 2 elements containing the anthills information (list)
    anthill: the anthill to be checked, from the anthill structure (dict)

    Returns
    -------
    level: the level of the anthill (int)

    Version
    -------
    specification: Youlan Collard (v.1 18/02/21) (v.2 26/02/21)
    implementation: Liam Letot (v.1 12/03/2021)
    """

    nbr_clod_pl = check_clod(main_structure, anthill_structure)
        
    #check the level
    if nbr_clod_pl[anthill['team'] - 1] <= 2:
        level = 1
    elif nbr_clod_pl[anthill['team'] - 1] <= 5:
        level = 2
    elif nbr_clod_pl[anthill['team'] - 1] <= 8:
        level = 3

    return level

def spawn(main_structure, ant_structure, anthill_structure):
    """Spawn ant.

    Parameters
    ----------
    main_structure: library of board (list)
    ant_structure: library of all ants (list)
    anthill_structure: library of all anthills (list)

    Version
    -------
    specification: Maxime Dufrasne (v.1 18/02/21) (v.2 10/03/21)
    implementation: Liam Letot (v.1 10/03/21)
    """
    for anthill in anthill_structure:
        #check the level the next ant will have
        if main_structure[anthill['pos_y']][anthill['pos_x']]['ant'] is None:
            ant_level = check_level(main_structure, anthill_structure, anthill)
            
            #with the level, take the health and color of the ant
            if ant_level == 1:
                health = 3
            elif ant_level == 2:
                health = 5
            elif ant_level == 3:
                health = 7

            ant_id = len(ant_structure)

            #add the next ant in ant_structure
            ant_structure.append({
                'id': ant_id,
                'team': anthill['team'],
                'health': health,
                'level': ant_level,
                'pos_y': anthill['pos_y'],
                'pos_x': anthill['pos_x'],
                'carrying': False,
                'clod_force': None,
                'played': False
                })

            #add the new ant in the board (main_structure) 
            main_structure[anthill['pos_y']][anthill['pos_x']]['ant'] = ant_id
            #take parameters for add_ant on display
            ant_pos = (anthill['pos_y'],anthill['pos_x'])
            team = anthill['team']
            add_ant_on_display(main_structure, ant_id, ant_pos, ant_level, team) 

# Removal of dead ant function
def death(ant_pos, main_structure, ant_structure, carrying):
    """Remove the specified ant.

    Parameters
    ----------
    ant_pos: position of the dead ant (list)
    main_structure: main structure of the board (list)
    ant_structure: structure containing the ants (list)
    carrying: if the ant was carrying something (bool)

    Version
    -------
    specification: Martin Buchet (v.1 18/02/21) (v.2 26/02/21)
    implementation: Martin Buchet (v.1 18/03/21)
    """
    #TODO: ne pas remove de ant_structure et passer l'attribut ant de main_structure à None
    ant_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']

    remove_ant_on_display(ant_id, ant_pos, carrying, main_structure, ant_structure)

    if carrying:
        place(main_structure, ant_structure, ant_pos)


    main_structure[ant_pos[0]][ant_pos[1]]['ant'] = None

    # remove dead ant from grid


# UI Function
def init_display(main_structure, ant_structure, anthills_structure):
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
    llcorner = '└'
    ulcorner = '┌'
    lrcorner = '┘'
    urcorner = '┐'
    hline = '─'
    bigplus = '┼'
    vline = '│'
    ttee = '┬'
    btee = '┴'
    ltee = '├'
    rtee = '┤'
    space = ' '
    row = len(main_structure)
    col = len(main_structure[0])

    print(term.home + term.clear + term.hide_cursor)
    # print grid
    for n in range(len(main_structure[0])):
        # numerotation of the columns
        nbr_col = ''
        if n + 1 < 10:
            nbr_col = ' ' + str(n + 1)
        else:
            nbr_col = str(n + 1)
        print(term.move_yx(0, n * 4 + 3) + nbr_col)
    print('  ' + ulcorner + (3 * hline + ttee) * (col - 1) + 3 * hline + urcorner)
    for x in range(row - 1):
        # numerotation of the rows
        if x + 1 < 10:
            nbr_row = str(x + 1) + ' '
        else:
            nbr_row = str(x + 1)
        print(nbr_row + (vline + 3 * space) * col + vline)
        print('  ' + ltee + (3 * hline + bigplus) * (col - 1) + 3 * hline + rtee)
    
    print(str(row) + (vline + 3 * space) * col + vline)
    print('  ' + llcorner + (3 * hline + btee) * (col - 1) + 3 * hline + lrcorner)

    print(term.on_blue + term.move_yx(anthills_structure[0]['pos_y'] * 2 + 2, anthills_structure[0]['pos_x'] * 4 + 5) + '⤊' + term.normal)
    print(term.on_red + term.move_yx(anthills_structure[1]['pos_y'] * 2 + 2, anthills_structure[1]['pos_x'] * 4 + 5) + '⤊' + term.normal)

    for y in range(len(main_structure)):
        for x in range(len(main_structure[0])):
            if main_structure[y][x]['clod']:
                color = get_color(main_structure[y][x]['clod'])
                print(term.move_yx((y * 2 + 2), (x * 4 + 5)) + '∆' + color + term.normal)

    spawn(main_structure, ant_structure, anthills_structure)

def move_ant_on_display(main_structure, ant_id, team, ant_level, ant_is_carrying, old_position, new_position):
    """Change the position of an ant on the dispay.

    Paremeters
    ----------
    main_structure: main structure of the game board (list)
    ant_id: id of the ant to move (int)
    team: number of the team owning the ant (int)
    ant_level: level of the ant being moved (int)
    ant_is_carrying: wether the ant is carrying a clods (bool)
    old_position: the old position of an ant (tuple)
    new_position: the new position of an ant (tuple)

    Version
    -------
    specification: Maxime Dufrasne (v.1 22/02/21) (v.2 28/03/21)
    implementation: Youlan Collard (v.1 12/03/21)
    """
    if team == 1:
        bg_color = term.on_blue
    elif team == 2:
        bg_color = term.on_red

    color = get_color(ant_level)

    if ant_is_carrying:
        possible_underline = term.underline
    else:
        possible_underline = ''

    print(term.move_yx(old_position[0] * 2 + 2, old_position[1] * 4 + 3) + ' ') # remove previous ant
    print(term.move_yx(new_position[0] * 2 + 2, new_position[1] * 4 + 3) + bg_color + color + possible_underline + '⚇' + term.normal) # add it back

    # Update the lifepoints pos
    life_point_col, life_point_row = define_col_and_row_for_lifepoint(len(main_structure), ant_id)

    ant_pos_for_lifepoint = ''

    for new_pos in new_position:
        if new_pos + 1 < 10:
            ant_pos_for_lifepoint += ' '

    ant_pos_for_lifepoint += str(new_position[0] + 1) + '-' + str(new_position[1] + 1)

    print(term.move_yx(life_point_row * 2 + 2, (len(main_structure[0]) * 4 + 3) + (life_point_col * 24)) + ' ' + ant_pos_for_lifepoint)

def remove_ant_on_display(ant_id, ant_pos, carrying, main_structure, ant_structure):
    """Remove ant on dispay when she died.

    Parameters
    ----------
    ant_id: id of the dead ant (int)
    ant_pos: position of an ant (list)
    carrying: if the ant was carrying something (bool)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    
    Version
    -------
    specification: Maxime Dufrasne  (v.1 22/02/21)
    implementation: Martin Buchet (v.1 18/03/21)
    """
    print(term.move_yx(ant_pos[0] * 2 + 2, ant_pos[1] * 4 + 3) + ' ')
    
    if carrying:
        # get ant_id from ant_pos then get the ant dict
        dead_ant = return_ant_by_id(ant_structure, ant_id)

        color = get_color(dead_ant['clod_force'])
        print(term.move_yx((ant_pos[0] * 2 + 2), (ant_pos[1] * 4 + 5)) + color + '∆' + term.normal)

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

def lift_clod_on_display(ant_pos, ant_structure, main_structure):
    """Make the clod disappear and switch the ant to an ant with clod on display.
    
    Parameters
    ----------
    ant_pos: the position of the ant who lift the clod (list)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)

    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    implementation: Martin Buchet, Maxime Dufrasne (v.1 21/03/21)
    """
    # get ant_id from ant_pos then get the ant dict
    ant_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']
    ant = return_ant_by_id(ant_structure, ant_id)

    color = get_color(ant['level'])

    if ant['team'] == 1:
        bg_color = term.on_blue
    elif ant['team'] == 2:
        bg_color = term.on_red
    
    print(term.move_yx((ant_pos[0] * 2 + 2), (ant_pos[1] * 4 + 5)) + ' ')
    print(term.move_yx((ant_pos[0] * 2 + 2), (ant_pos[1] * 4 + 3)) + bg_color + color + term.underline + '⚇' + term.normal)

def place_clod_on_display(ant_pos, clod_force, main_structure, ant_structure):
    """Make the clod appear and switch the ant with a clod to an ant on display.

    Parameters
    ----------
    ant_pos: the position of the ant who lift the clod (list)
    clod_force: the force needed to lift the clod the ant just dropped (int)
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)

    Version
    -------
    specification: Liam Letot (v.1 22/02/21)
    implementation: Martin Buchet, Maxime Dufrasne (v.1 21/03/21)
    """
    # get ant_id from ant_pos then get the ant dict

    # TODO: Add background color (Youlan)

    ant_id = main_structure[ant_pos[0]][ant_pos[1]]['ant']
    ant = return_ant_by_id(ant_structure, ant_id)
    team = ant['team']
    if team == 1:
        bg_color = term.on_blue
    elif team == 2:
        bg_color = term.on_red

    color = get_color(clod_force)

    print(term.move_yx((ant_pos[0] * 2 + 2), (ant_pos[1] * 4 + 5)) + color + '∆' + term.normal)

    color = get_color(ant['level'])

    print(term.move_yx((ant_pos[0] * 2 + 2), (ant_pos[1] * 4 + 3)) + bg_color + color + '⚇' + term.normal)

def define_col_and_row_for_lifepoint(max_row, ant_id, current_col=0):
    """Returns the row and columns where the health bar should be printed

    Parameters
    ----------
    max_row: the max number of rows per column (int)
    ant_id: the id of the ant (int)
    current_col: current column that should be returned (int, optional)

    Returns
    -------
    col: the column where the health bar should be displayed
    row: the row where the health bar should be displayed

    Notes
    -----
    Never set current_col to anything else than 0 when you call it yourself, this variable is updated by the function itself

    Version
    -------
    specification: Youlan Collard (v.1 28/03/21)
    implementation: Youlan Collard (v.1 28/03/21)
    """
    max_row_indexed = max_row - 1
    if ant_id <= max_row_indexed:
        return current_col, ant_id
    else:
        return define_col_and_row_for_lifepoint(max_row, ant_id - max_row, current_col + 1)

def add_ant_on_display(main_structure, ant_id, ant_pos, ant_level, team) :
    """Add an ant on display (game board and health bar).
    
    Parameters
    ----------
    main_structure: main structure of the game board (list)
    ant_id: id of the added ant (int)
    ant_pos: Position of the ant to add (list)
    ant_level: the level of the ant (int)
    team: the team of the ant (int)
    Version
    -------
    specification: Liam Letot (v.1 22/02/21) (v.2 05/03/21) (v.3 12/03/21)
    implementation: Liam Letot, Youlan Collard (v.1 12/03/21)
    """
    #TODO: Ajouter barre de vie à droite de la grille
    life_point_col, life_point_row = define_col_and_row_for_lifepoint(len(main_structure), ant_id)

    if ant_level == 1:
        health = 3
    elif ant_level == 2:
        health = 5
    elif ant_level == 3:
        health = 7


    if team == 1:
        bg_color = term.on_blue
    elif team == 2:
        bg_color = term.on_red

    term_color = get_color(ant_level)

    ant_pos_for_lifepoint = ''

    for pos in ant_pos:
        if pos < 10:
            ant_pos_for_lifepoint += ' '
    
    ant_pos_for_lifepoint = ant_pos_for_lifepoint + str(ant_pos[0] + 1) + '-' + str(ant_pos[1] + 1)
    health_display = ' %d/%d' % (health, health)

    print(term.move_yx(life_point_row * 2 + 2, (len(main_structure[0]) * 4 + 3) + (life_point_col * 24)) + ' ' + ant_pos_for_lifepoint + ' ' + term_color + bg_color + '⚇' + term.normal + ' ' + term.on_green + '          ' + term.normal + health_display )
    print(term.move_yx(ant_pos[0] * 2 + 2, ant_pos[1] * 4 + 3) + bg_color + term_color + '⚇' + term.normal)

# Util function
def return_ant_by_id(ant_structure, ant_id):
    """Find an ant by its id inside the ant structure.

    Parameters
    ----------
    ant_structure: the structure containing all the ants (list)
    ant_id: id of the desired ant (int)

    Returns
    -------
    ant: The desired ant (dict)

    Version
    -------
    specification: Youlan Collard (v.1 21/02/21)   
    implementation: Youlan Collard (v.1 12/03/21) 
    """
    for ant in ant_structure:
        if ant['id'] == ant_id:
            return ant

def get_color(level):
    """Send the color string for the specified level using blessed

    Parameters
    ----------
    level: the level to check [1-3] (int)

    Returns
    -------
    color: term color escape character or an empty str if level is 1 (str)

    Version
    -------
    specificaiton: Youlan Collard (v.1 18/03/21)
    implementation: Youlan Collard (v.1 18/03/21)
    """
    if level == 1:
        return ''
    elif level == 2:
        return term.yellow
    elif level == 3:
        return term.green

def reset_play_all_ants(ant_structure):
    for ant in ant_structure:
        ant['played'] = False

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
    global ant_structure
    #init the main parameters
    number_of_turn = 1
    board_size, anthills, clods = parse_map_file(CPX_file)

    main_structure, ant_structure, anthill_structure = create_map(board_size, anthills, clods)
    init_display(main_structure, ant_structure, anthill_structure)
    
    #if the game is played with AI, take the AI path to execute them
    #if type_1 == 'AI':
        #AI1_code = input("path to the ia code file")
    #if type_2 == 'AI':
        #AI2_code = input("path to the ia code file")

        
    #run the game
    is_won = check_victory(main_structure, anthill_structure, number_of_turn)
    while is_won is None or is_won == 3:

        #take the orders
        if type_1 == 'human' or type_2 == 'human':
            print(term.move_yx(len(main_structure) * 2 + 2, 0) + term.clear_eos)
        if type_1 == 'human':
            orders_1 = input("team_1 input : ")
        elif type_1 == 'AI':
            team = 1
            orders_1 = First_IA(main_structure, ant_structure, team)
        if type_2 == 'human':
            orders_2 = input("team_2 input : ")
        elif type_2 == 'AI':
            team = 2
            orders_2 = First_IA(main_structure, ant_structure, team)
        
        #check and execute the orders
        orders = orders_1 + ';' + orders_2 
        orders_list = interpret_order(main_structure, ant_structure, anthill_structure, orders)
        # orders_list = interpret_order( 1 ,main_structure, ant_structure, anthill_structure, orders_1)
        # orders_list += interpret_order(2, main_structure, ant_structure, anthill_structure, orders_2)
        exec_order(orders_list, main_structure, ant_structure)
        reset_play_all_ants(ant_structure)
        #check and spawn new ant if it's needed
        if number_of_turn % 5 == 0 and is_won != 3:
            spawn(main_structure, ant_structure, anthill_structure)
        number_of_turn += 1
        time.sleep(0.1)
        is_won = check_victory(main_structure, anthill_structure, number_of_turn)
    #print the end message
    if is_won == 1:
        print('Team 1 win')
    elif is_won == 2:
        print('Team 2 win')
    elif is_won == 3:
        print('Tied')


def First_IA(main_structure, ant_structure, team):
    """a First AI which make an order for each ant on the board

    Parameter
    ---------
    main_structure: main structure of the game board (list)
    ant_structure: structure containing all the ants (list)
    team: the team which want orders (int)
    return
    ------
    orders: orders for each ant on the board (str)
    
    Version
    -------
    specification: Liam Letot (v.1 26/03/21)   
    implementation: Liam Letot (v.1 26/03/21) 
    """
    
    around2 = [(-3, -3),(-2, -3),(-1, -3),(0, -3),(1, -3),(2, -3),(3, -3),
    (-3, -2),(-2, -2),(-1, -2),(0, -2),(1, -2),(2, -2),(3, -2),
    (-3, -1),(-2, -1),(-1, -1),(0, -1),(1, -1),(2, -1),(3, -1),
    (-3,  0),(-2,  0),(-1,  0),(1,  0),(2,  0),(3,  0),
    (-3,  1),(-2,  1),(-1,  1),(0,  1),(1,  1),(2,  1),(3,  1),
    (-3,  2),(-2,  2),(-1,  2),(0,  2),(1,  2),(2,  2),(3,  2),
    (-3,  3),(-2,  3),(-1,  3),(0,  3),(1,  3),(2,  3),(3,  3)]
    orders = ''
    
    for ant in ant_structure:
        #check if the ant is on the good team
        if ant['team'] == team:
            #check which order is possible for each ant
            target = False
            dice_roll = [1]
            for pos in around2:
                pos_y = pos[0] + ant['pos_y']
                pos_x = pos[1] + ant['pos_x']
                if pos_y >=0 and pos_y < len(main_structure):
                    if pos_x >=0 and pos_x < len(main_structure[0]):
                        if main_structure[pos_y][pos_x]['ant']:
                            if ant_structure[main_structure[pos_y][pos_x]['ant']]['team'] != ant['team']:
                                target = True
                                target_pos_y = pos_y +1
                                target_pos_x = pos_x +1
            if main_structure[ant['pos_y']][ant['pos_x']]['clod'] != None and ant['carrying'] == False:
                dice_roll.append(3)
            if main_structure[ant['pos_y']][ant['pos_x']]['clod'] == None and ant['carrying'] != False:
                dice_roll.append(4)
            if target:
                dice_roll.append(2)
            
            
            #randomly take one of the possible order
            choice = random.randint(0,len(dice_roll) - 1)

            if dice_roll[choice] == 1:
                #randomly take a direction for moving
                direction = random.randint(1,8)
                orders += str(ant['pos_y']+ 1) + '-' + str(ant['pos_x']+1) + ':@'
                if direction == 1:
                    orders += str(ant['pos_y']) + '-' + str(ant['pos_x']) + ' '
                if direction == 2:
                    orders += str(ant['pos_y']) + '-' + str(ant['pos_x']+1) + ' '
                if direction == 3:
                    orders += str(ant['pos_y']) + '-' + str(ant['pos_x']+2) + ' '
                if direction == 4:
                    orders += str(ant['pos_y']+1) + '-' + str(ant['pos_x']+2) + ' '
                if direction == 5:
                    orders += str(ant['pos_y']+2) + '-' + str(ant['pos_x']+2) + ' '
                if direction == 6:
                    orders += str(ant['pos_y']+2) + '-' + str(ant['pos_x']+1) + ' '
                if direction == 7:
                    orders += str(ant['pos_y']+2) + '-' + str(ant['pos_x']) + ' '
                if direction == 8:
                    orders += str(ant['pos_y']+1) + '-' + str(ant['pos_x']) + ' '
                
            if dice_roll[choice] == 2:
                orders += str(ant['pos_y']+1) + '-' + str(ant['pos_x']+1) + ':*' + str(target_pos_y) + '-' + str(target_pos_x) + ' '

            if dice_roll[choice] == 3:
                orders += str(ant['pos_y']+1) + '-' + str(ant['pos_x']+1) + ':lift '

            if dice_roll[choice] == 4:
                orders += str(ant['pos_y']+1) + '-' + str(ant['pos_x']+1) + ':drop '
    

    return orders


play_game('./small.cpx', '1', 'AI', '2', 'AI')

    