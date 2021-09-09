#5-function Написати функцію для знаходження відстані між двома точками в просторі:
# (x1, y1, z1) і (x2, y2, z2).


def distance_in_space(x1, y1, z1, x2, y2, z2):
    """Calculating the distance between two points in space with coordinates (x1,y1,z1) and (x2,y2,z2)"""
    distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
    return distance


#test
assert (distance_in_space(1, 1, 1, 4, 4, 4) == 5.196152422706632)
