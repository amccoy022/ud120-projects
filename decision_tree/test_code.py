import math

entropy_parent = 1.0

entropy_child_1 = -(.666)*math.log(.666, 2)-(.333)*math.log(.333, 2)
print entropy_child_1

entropy_child_2 = 0

inf_gain = entropy_parent - (((3/4)(entropy_child_1))+((1/4)(entropy_child_2)))
print inf_gain