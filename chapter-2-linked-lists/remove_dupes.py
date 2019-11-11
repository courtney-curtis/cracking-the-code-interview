from LinkedList import LinkedNode, LinkedList

def remove_dupes(linked_list):
    check_dict = {}
    this_node = linked_list.first_node
    prev_node = None

    while this_node:
        if this_node.data in check_dict:
            prev_node.link = this_node.link
        else:
            check_dict[this_node.data] = True
        prev_node = this_node
        this_node = this_node.link

    print_node = linked_list.first_node
    while print_node:
        print(print_node.data)
        print_node = print_node.link
        
    return linked_list

if __name__ == '__main__':
    node_4 = LinkedNode(3)
    node_3 = LinkedNode(3, node_4)
    node_2 = LinkedNode(2, node_3)
    node_1 = LinkedNode(1, node_2)

    linked_list = LinkedList(node_1)
    remove_dupes(linked_list)
