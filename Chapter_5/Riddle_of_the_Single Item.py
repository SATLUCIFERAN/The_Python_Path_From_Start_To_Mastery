
# This is NOT a tuple, it's a string
single_item_tuple_fail = ("R2-D2")
print(type(single_item_tuple_fail))
# Output: <class 'str'>


# This IS a tuple - notice the trailing comma!
single_item_tuple_success = ("R2-D2",)
print(type(single_item_tuple_success))
# Output: <class 'tuple'>