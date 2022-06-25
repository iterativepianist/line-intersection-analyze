import numpy
import shapely
from shapely.geometry import LineString, Point
from matplotlib import pyplot as plt


def line_intersection_shapely(p1, p2, p3, p4):
    line1 = LineString([p1, p2])
    line2 = LineString([p3, p4])

    int_pt = line1.intersection(line2)
    return int_pt.x, int_pt.y


def line_intersection_own_impl(line1, line2):
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
            print("Lines are co linear")
            return None  # so no solution

        if dx1:
            if x1 < x3 < x2 or x1 > x3 > x2:
                print("Many solutions")
                raise Exception  # infinitely many solutions
        else:
            if y1 < y3 < y2 or y1 > y3 > y2:
                print("Many solutions")
                raise Exception  # infinitely many solutions

        if line1[0] == line2[0] or line1[1] == line2[0]:
            raise Exception
        elif line1[0] == line2[1] or line1[1] == line2[1]:
            raise Exception

        print("No intersection")
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


def draw_2_lines(p1, p2, p3, p4, result):
    print("Draw 2 lines")
    # plt.rcParams["figure.figsize"] = [5, 5]
    plt.rcParams["figure.autolayout"] = True

    x_values1 = [p1[0], p2[0]]
    y_values2 = [p1[1], p2[1]]
    plt.plot(x_values1, y_values2, 'go', linestyle="-")
    plt.text(p1[0], p1[1], "")
    plt.text(p2[0], p2[1], "")

    x_values3 = [p3[0], p4[0]]
    y_values4 = [p3[1], p4[1]]
    plt.plot(x_values3, y_values4, 'bo', linestyle="-")
    plt.text(p3[0] - 0.01, p3[1] + 0.01, "")
    plt.text(p4[0] - 0.01, p4[1] - 0.01, "")

    if result is not None:
        plt.scatter(result[0], result[1], c="red")

    plt.savefig('project/static/image.jpg')
    plt.clf()


def draw_3_lines(p1, p2, p3, p4, p5, p6):
    print("Draw 3 lines")
    # plt.rcParams["figure.figsize"] = [5, 5]
    plt.rcParams["figure.autolayout"] = True

    x_values1 = [p1[0], p2[0]]
    y_values2 = [p1[1], p2[1]]
    plt.plot(x_values1, y_values2, 'go', linestyle="-")
    plt.text(p1[0] - 0.01, p1[1] + 0.25, "")
    plt.text(p2[0] - 0.01, p2[1] - 0.25, "")

    x_values3 = [p3[0], p4[0]]
    y_values4 = [p3[1], p4[1]]
    plt.plot(x_values3, y_values4, 'bo', linestyle="-")
    plt.text(p3[0] - 0.01, p3[1] + 0.01, "")
    plt.text(p4[0] - 0.01, p4[1] - 0.01, "")

    x_values5 = [p5[0], p6[0]]
    y_values6 = [p5[1], p6[1]]

    plt.plot(x_values5, y_values6, 'r', linestyle="-", linewidth=7.0)
    plt.text(p5[0] - 0.01, p5[1] + 0.01, "")
    plt.text(p6[0] - 0.01, p6[1] - 0.01, "")

    plt.savefig('project/static/image.jpg')
    plt.clf()


def lineIntersec(p1, p2, p3, p4):
    try:
        # p1 = [0, 10]
        # p2 = [0, 15]

        # p3 = [-5, 5]
        # p4 = [5, 20]
        # result = line_intersection_own_impl([p1, p2], [p3, p4])

        result = line_intersection_shapely(p1, p2, p3, p4)

        print("line_intersection_result", result)

        draw_2_lines(p1, p2, p3, p4, result)
        return result

        print("Lines intersects at:", result)
    except Exception:
        print("Exception raised, calculate common part")
        commonPoints = getCommonPart(p1, p2, p3, p4)

        if (len(commonPoints) == 0):
            draw_2_lines(p1, p2, p3, p4, None)
            return "Odcinki nie przecinają się"

        commonPoints = sorted(commonPoints, key=lambda tup: (tup[0], tup[1]))

        print("Common points:" + str(commonPoints))
        commonSegmentStart = commonPoints[0]
        commonSegmentEnd = commonPoints[-1]

        draw_3_lines(p1, p2, p3, p4, numpy.array(commonSegmentStart), numpy.array(commonSegmentEnd))
        return [commonSegmentStart, commonSegmentEnd]


def getCommonPart(p1, p2, p3, p4):
    line1 = [tuple(p1)]
    line1.extend(points_on_line(p1, p2))
    line1.append(tuple(p2))
    line2 = [tuple(p3)]
    line2.extend(points_on_line(p3, p4))
    line2.append(tuple(p4))
    commonPoints = intersection(line1, line2)
    return commonPoints
