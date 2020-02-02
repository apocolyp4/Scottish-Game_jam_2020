import appgamekit as agk
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
from Game import Game
import json

with agk.Application():
    status = 'client'

    #setup the editor

    vis_editor = VisualEditor(0)
    game = Game(vis_editor)

    boy_button = vis_editor.get_entity_id("IB:Boy", 0)
    girl_button = vis_editor.get_entity_id("IB:Girl", 0)
    dungeon_master_button = vis_editor.get_entity_id("IB:DungeonMaster", 0)
    boy_button.text.set_active(False)
    girl_button.text.set_active(False)
    dungeon_master_button.text.set_active(False)

    while True:
        if agk.get_raw_key_pressed(27):
            agk.end()

        if boy_button.pressed:
            game.start("boy")
        elif girl_button.pressed:
            game.start("girl")
        elif dungeon_master_button.pressed:
             game.start("dungeon master")

        vis_editor.update()
        agk.sync()


    # game_network = Network("Awesome Dave", "10.241.90.69", 45000)
    # game_network.client()

    # Networking Code
    if status is 'server':
        # connection as server
        game_network = Network("Game Deally", "10.241.90.69", 45000)
        network_id = game_network.host()
        iType = 0
    if status is 'client':
        # connection as client
        game_network = Network("Game Deally", "10.241.90.69", 45000)
        network_id = game_network.client()
        iType = 1

    while True:
        #Networking Code
        user_data_list = []
        if iType is 0: #host
            #Modify for more realistic use depending on number npcs
            for x in range(6):
                user_detail = {"sprite_name": str(x), "sprite_x": 700, "sprite_y": 400, "sprite_z": 0, "health": 123}
                user_data_list.append(user_detail)
        if iType is 1: #client
            #create user dictionary for each user
            #use data from each of the npc characters
            #add them to a list of users
            user_detail = {"sprite_name": "client", "sprite_x": 600, "sprite_y": 500, "sprite_z": 0, "health": 123}
            user_data_list.append(user_detail)

        if agk.is_network_active(network_id) != 0:
            id = agk.get_network_first_client(network_id)
            #Get players online
            while id != 0:
                print('ID = ' + str(id))
                id = agk.get_network_next_client(network_id)

            for user_detail in user_data_list:
                cmessage = agk.create_network_message()
                agk.add_network_message_string(cmessage, json.dumps(user_detail))
                agk.send_network_message(network_id, 0, cmessage)

            game_network.update()
            cmessage = agk.get_network_message(network_id)
            while cmessage != 0:
                player_data = None
                # Replace with message parsing code
                # This are will be responsible for
                # reading data from the queue and
                # manipulating sprites
                player_data = agk.get_network_message_string(cmessage)
                player_obj = json.loads(player_data)
                test_sprite.set_position(player_obj["sprite_x"], player_obj["sprite_y"])
                # Replace with message parsing code
                agk.delete_network_message(cmessage)
                cmessage = agk.get_network_message(network_id)

        if agk.get_raw_key_pressed(27):
            break

        vis_editor.update()
        agk.sync()