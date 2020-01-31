import appgamekit as agk
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from networking import Network
from Text import Text

with agk.Application():
    status = 'client'

    #setup the editor

    vis_editor = VisualEditor(0)
    #vis_editor.open_scene(0)
    #sprite = vis_editor.get_entity_id("sprite 8", 0)
    #kind = vis_editor.get_entity_kind("sprite 8", 0)

    agk.set_clear_color(255, 255, 255)
    agk.set_print_color(0, 0, 0)

    search_tree = SearchTree()

    #create_node(Node Name (String), X co-oridinate (Integer), Y co-oridinate (Integer), Accessible (Bool))
    node1 = search_tree.new_node("Node 1", 50, 0, True)
    node2 = search_tree.new_node("Node 2", 10, 30, True)
    node3 = search_tree.new_node("Node 3", 70, 30, True)
    node4 = search_tree.new_node("Node 4", 40, 200, True)
    node5 = search_tree.new_node("Node 5", 200, 160, True)
    node6 = search_tree.new_node("Node 6", 300, 430, True)

    node1.add_child(node2)
    node1.add_child(node3)
    node2.add_child(node1)
    node2.add_child(node4)
    node3.add_child(node4)
    node3.add_child(node5)
    node4.add_child(node2)
    node4.add_child(node6)
    node5.add_child(node3)
    node5.add_child(node6)
    node6.add_child(node4)
    node6.add_child(node5)

    #prints tree
    for node in search_tree.nodes:
        node_text = node.id
        node_text += " Child Nodes = "
        for child in node.child_nodes:
            node_text += child.id + " "
        print(node_text)

    print("")
    print("Path")

    path = search_tree.get_path("Node 1", "Node 6")

    node_text = ""
    for node in path:
        node_text += node.id + " "

    print(node_text)

    # test_button = ImageButton("", "SHITE")
    # test_button.set_position(0, 0)
    # text_color = Color(255, 0, 0, 255)


    test_text = Text("cunty baws", Color(0, 0, 0, 255), 45, 100, 100, 0, True, True)
    test_text.set_string("mubs")

    if status is 'client':
        #connection as client
        game_network = Network("Awesome Rich", "10.241.90.69", 45000)
        game_network.client()
        iType = 1
        State = 1
    if status is 'server':
        #connection as server
        network_id = agk.host_network("AGK Test Game", "Player 1", 45000)
        iType = 0
        State = 1

    while True:
        agk.sync()

        if iType is 0:
            x = 11
            y = 12
            cmessage = agk.create_network_message()
            agk.add_network_message_float(cmessage, x)
            agk.add_network_message_float(cmessage, y)
            agk.send_network_message(network_id, 0, cmessage)

        if iType is 1:
            game_network.update()
            cmessage = agk.get_network_message(100001)
            while cmessage != 0:
                x = agk.get_network_message_float(cmessage)
                y = agk.get_network_message_float(cmessage)

                #add update code here
                print(x)
                print(y)

                agk.delete_network_message(cmessage)
                cmessage = agk.get_network_message(100001)

        if agk.get_raw_key_pressed(27):
            break