import appgamekit as agk
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from networking import Network
from Text import Text
from Sprite import Sprite

with agk.Application():
    status = 'server'

    #setup the editor
    text_image = agk.load_image("Images/greenCar.png")
    test_sprite = Sprite(text_image, 10, 20, 11, 25, 0, 0, False, True) #Change visiible to False for invisible

    vis_editor = VisualEditor(0)
    #vis_editor.open_scene(0)
    #sprite = vis_editor.get_entity_id("sprite 8", 0)
    #kind = vis_editor.get_entity_kind("sprite 8", 0)

    agk.set_clear_color(255, 255, 255)
    agk.set_print_color(0, 0, 0)

    # test_button = ImageButton("", "SHITE")
    # test_button.set_position(0, 0)
    # text_color = Color(255, 0, 0, 255)


    test_text = Text("cunty baws", Color(0, 0, 0, 255), 45, 100, 100, 0, True, True)
    test_text.set_string("mubs")

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
        agk.sync()

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
            x = test_sprite.get_centre_x()
            y = test_sprite.get_centre_y()
            cmessage = agk.create_network_message()
            agk.add_network_message_float(cmessage, x)
            agk.add_network_message_float(cmessage, y)

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
                print(str(x) + " " + str(y))
                test_sprite.set_position(x, y)
                # Replace with message parsing code

                agk.delete_network_message(cmessage)
                cmessage = agk.get_network_message(network_id)

        if agk.get_raw_key_pressed(27):
            break