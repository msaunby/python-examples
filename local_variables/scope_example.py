def make_list(new_item):
    local_str = "I'm a local string"
    # mutable objects from the outer scope
    my_list.append(new_item)
    my_dict[new_item] = 0
    # Try uncommenting the next line
    # global_str = "Is this allowed?"
    print('make_list: local_str', local_str)
    print('make_list: global_str', global_str)
    return len(my_list)

my_list = []
my_dict = {}
global_str = "I'm a global string, you can access me anywhere"
count = make_list("hello")
count = make_list("world")

print('main:', count, my_list, my_dict)
print('main:', global_str)

