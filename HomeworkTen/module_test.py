"""Test of importing modules"""
# from Task_Three import find_file
# from Task_One_and_Two import get_most_common_symbol
#
# if __name__ == '__main__':
#     for a in find_file('test_file'):
#         print(a[1])
#         print(get_most_common_symbol(a[1]))

"""Test of imported package with blank init file"""
# from my_packet import file_search, common_symbol
#
# if __name__ == '__main__':
#     for a in file_search.find_file('test_file'):
#         print(a[1])
#         print(common_symbol.get_most_common_symbol(a[1]))

"""Test of imported package with imports in init file"""
# import my_packet
#
# for a in my_packet.find_file('test_file'):
#     print(a[1])
#     print(my_packet.get_most_common_symbol(a[1]))

"""Test of imported package after adding __all__ to init"""
# from my_packet import *
#
# for a in find_file('test_file'):
#     print(a[1])
#     print(get_most_common_symbol(a[1]))
