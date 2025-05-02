from math import sqrt
from itertools import combinations


points = [
    (2, 1),
    (2, 5),
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4),
    (1, 2),
    (4, 5),
    (7, 8),
    (9, 10),
    (11, 12),
    (13, 14),
    (15, 16),
    (17, 18),
    (19, 20),
]


def find_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def brute_force(points):
    min_dist = float("inf")
    closest = None
    for p1, p2 in combinations(points, 2):
        dist = find_distance(p1, p2)
        if dist < min_dist:
            min_dist = dist
            closest = (p1, p2)
    return closest[0], closest[1], min_dist


def closest_pair(points_sorted_by_x):
    if len(points_sorted_by_x) <= 6:
        return brute_force(points_sorted_by_x)

    mid = len(points_sorted_by_x) // 2
    midpoint = points_sorted_by_x[mid][0]

    left = points_sorted_by_x[:mid]
    right = points_sorted_by_x[mid:]

    l_p1, l_p2, l_dist = closest_pair(left)
    r_p1, r_p2, r_dist = closest_pair(right)

    if l_dist < r_dist:
        min_pair = (l_p1, l_p2)
        min_dist = l_dist
    else:
        min_pair = (r_p1, r_p2)
        min_dist = r_dist

    # Build strip: points within min_dist of the dividing line
    strip = [p for p in points_sorted_by_x if abs(p[0] - midpoint) < min_dist]
    strip.sort(key=lambda p: p[1])  # sort by y

    # Check each point in the strip with next ~6 points
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            p1, p2 = strip[i], strip[j]
            dist = find_distance(p1, p2)
            if dist < min_dist:
                min_dist = dist
                min_pair = (p1, p2)

    return min_pair[0], min_pair[1], min_dist


# Pre-sort by x before starting recursion
points_sorted = sorted(points, key=lambda p: (p[0], p[1]))
p1, p2, dist = closest_pair(points_sorted)

print("Closest points:", p1, "and", p2, "with distance:", dist)
