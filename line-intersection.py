def line_intersection(line1, line2):
    x1, x2, x3, x4 = line1[0][0], line1[1][0], line2[0][0], line2[1][0]
    y1, y2, y3, y4 = line1[0][1], line1[1][1], line2[0][1], line2[1][1]

    dx1 = x2 - x1
    dx2 = x4 - x3
    dy1 = y2 - y1
    dy2 = y4 - y3
    dx3 = x1 - x3
    dy3 = y1 - y3

    det = dx1 * dy2 - dx2 * dy1
    det1 = dx1 * dy3 - dx3 * dy1
    det2 = dx2 * dy3 - dx3 * dy2

    if det == 0.0:  # lines are parallel
        if det1 != 0.0 or det2 != 0.0:  # lines are not co-linear
            return None  # so no solution

        if dx1:
            if x1 < x3 < x2 or x1 > x3 > x2:
                raise Exception  # infinitely many solutions
        else:
            if y1 < y3 < y2 or y1 > y3 > y2:
                raise Exception  # infinitely many solutions

        if line1[0] == line2[0] or line1[1] == line2[0]:
            return line2[0]
        elif line1[0] == line2[1] or line1[1] == line2[1]:
            return line2[1]

        return None  # no intersection

    s = det1 / det
    t = det2 / det

    if 0.0 < s < 1.0 and 0.0 < t < 1.0:
        return x1 + t * dx1, y1 + t * dy1


def points_on_line(p1, p2):
    fx, fy = p1
    sx, sy = p2
    if fx == sx and fy == sy:
        return []
    elif fx == sx:
        return [(fx, y) for y in range(fy + 1, sy)]
    elif fy == sy:
        return [(x, fy) for x in range(fx + 1, sx)]
    elif fx > sx and fy > sy:
        p1, p2 = p2, p1

    slope = (p2[1] - p1[1]) / float(p2[0] - p1[0])
    return [(x, int(x * slope)) for x in range(p1[0], p2[0]) if
            int(x * slope) == x * slope and (x, int(x * slope)) != p1]


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


if __name__ == '__main__':
    try:
        p1 = [-4, 2]
        p2 = [4, 2]

        p3 = [0, 2]
        p4 = [0, 2]
        result = line_intersection([p1, p2], [p3, p4])

        print("Lines intersects at:", result)
    except Exception:
        line1 = [tuple(p1)]
        line1.extend(points_on_line(p1, p2))
        line1.append(tuple(p2))

        line2 = [tuple(p3)]
        line2.extend(points_on_line(p3, p4))
        line2.append(tuple(p4))

        commonPoints = intersection(line1, line2)

        if (len(commonPoints) == 0):
            print("No intersection points. Lines are parallel")
            exit(0)

        commonPoints = sorted(commonPoints, key=lambda tup: (tup[0], tup[1]))
        commonSegmentStart = commonPoints[0]
        commonSegmentEnd = commonPoints[-1]

        print("Common segment is between:", commonSegmentStart, commonSegmentEnd)