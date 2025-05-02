import math


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def brute_force(points):
    min_dist = float("inf")
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist


def closest_pair_recursive(px, py):
    if len(px) <= 3:
        return brute_force(px)

    mid = len(px) // 2
    mid_x = px[mid][0]

    Qx = px[:mid]
    Rx = px[mid:]
    midpoint = px[mid][0]
    Qy = list(filter(lambda p: p[0] <= midpoint, py))
    Ry = list(filter(lambda p: p[0] > midpoint, py))

    (p1, d1) = closest_pair_recursive(Qx, Qy)
    (p2, d2) = closest_pair_recursive(Rx, Ry)

    d = min(d1, d2)
    min_pair = p1 if d1 <= d2 else p2

    strip = [p for p in py if abs(p[0] - mid_x) < d]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):  # Only need to check next 6 points
            dst = distance(strip[i], strip[j])
            if dst < d:
                d = dst
                min_pair = (strip[i], strip[j])

    return min_pair, d


def closest_pair(points):
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair_recursive(px, py)


if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    pair, dist = closest_pair(points)
    print(f"Closest pair: {pair} with distance {dist:.2f}")
