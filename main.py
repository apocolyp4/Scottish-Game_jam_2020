import appgamekit as agk
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
from Sprite import Sprite
import json

with agk.Application():
    status = 'server'

    #setup the editor
    text_image = agk.load_image("Images/greenCar.png")
    test_sprite = Sprite(text_image, 10, 20, 11, 25, 0, 0, False, True) #Change visiible to False for invisible

    vis_editor = VisualEditor(0)
    vis_editor.open_scene(0)
    moon_poo = vis_editor.get_entity_id("MOON POO", 0)

    # game_network = Network("Awesome Dave", "10.241.90.69", 45000)
    # game_network.client()

    if status is 'client':
        #connection as client
        game_network = Network("Awesome Rich", "10.241.90.69", 45000)
        network_id = game_network.client()
        iType = 1
        State = 1
    if status is 'server':
        #connection as server
        game_network = Network("Awesome Rich", "10.241.90.69", 45000)
        network_id = game_network.host()
        iType = 0
        State = 1

    while True:
        if agk.is_network_active(network_id) != 0:
            id = agk.get_network_first_client(network_id)
            #Get players online
            while id != 0:
                print('ID = ' + str(id))
                id = agk.get_network_next_client(network_id)

            # Replace with message build code
            # This section will be responsible
            # For the handling of incoming data
            # from the other player and the
            # manipulation of sprites on the screen
            user_detail = {"sprite_name": "fsds", "sprite_x": 0, "sprite_y": 0, "sprite_z": 0, "health": 123}
            x = test_sprite.get_centre_x()
            y = test_sprite.get_centre_y()
            cmessage = agk.create_network_message()
            agk.add_network_message_float(cmessage, x)
            agk.add_network_message_float(cmessage, y)
            agk.add_network_message_string(cmessage, json.dumps(user_detail))

            agk.send_network_message(network_id, 0, cmessage)

            game_network.update()
            cmessage = agk.get_network_message(network_id)

            while cmessage != 0:
                # Replace with message parsing code
                # This are will be responsible for
                # reading data from the queue and
                # manipulating sprites
                x = agk.get_network_message_float(cmessage)
                y = agk.get_network_message_float(cmessage)
                player_date = agk.get_network_message_string(cmessage)
                player_obj = json.loads(player_date)
                print(player_obj)
                print(player_obj["sprite_name"])
                print(player_obj["sprite_x"])
                print(player_obj["sprite_y"])
                print(player_obj["sprite_z"])
                print(player_obj["health"])
                print(str(x) + " " + str(y))
                test_sprite.set_position(player_obj["sprite_x"], player_obj["sprite_y"])
                # Replace with message parsing code

                agk.delete_network_message(cmessage)
                cmessage = agk.get_network_message(network_id)


        if agk.get_raw_key_pressed(27):
            break

        vis_editor.update()
        agk.sync()