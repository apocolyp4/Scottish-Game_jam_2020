import appgamekit as agk
from SearchTree import SearchTree

with agk.Application():
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

    path = search_tree.get_path("node 1", "node 6")

    node_text = ""
    for node in path:
        node_text += node.id + " "

    print(node_text)



    while True:

        agk.sync()
        if agk.get_raw_key_pressed(27):
            break