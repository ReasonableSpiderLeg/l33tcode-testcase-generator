"""Generate test cases for leetcode.com

This library supports
- defining testcases using a JSON format definition,
- automatically determining a selection of edge cases,
- writing them out into sets of 8 in separate text files

"""
import random
import time
import itertools


def write_file(filename: str, string: str):
    """A simple wrapper to write a string to a file.

    Does not allow override of an existing file.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        None
    """
    f = open(filename, "x")
    f.write(string)
    f.close()


def write_testcase(tests):
    """Convert test cases into strings, add line breaks    and write out.
    """
    write_file(tests)


"""Generate testcases for 1514_Path_with_Maximum_Probability.py
"""


def get_testcase_random() -> [int, list, list, int, int]:
    n, edges, succProb, start, end = get_testcase_uniform()
    succProb = [random.random() for i in range(len(succProb))]
    return n, edges, succProb, start, end


def get_testcase_min() -> [int, list, list, int, int]:
    n = 2
    start = 0
    end = 1
    edges = []
    succProb = []
    return n, edges, succProb, start, end


def get_testcase_uniform() -> [int, list, list, int, int]:
    n = 10 ** 4
    start = 0
    end = 10 ** 4 - 1
    edges = []
    succProb = []
    max_edge_count = 2 * n
    for i in range(max_edge_count):
        a = random.randint(start, end)
        b = a
        while b == a or [a, b] in edges or [b, a] in edges:
            b = random.randint(start, end)
        edges.append([a, b])
        succProb.append(1)
    return n, edges, succProb, start, end


def replace_grid_field(grid, x, y, char):
    grid[y] = grid[y][:x] + char + grid[y][x + 1 :]


def main(challenge_id=-1):
    implemented_challenges = [
        1514,
        864,
        1970,
        2305,
        1601,
        137,
        1493,
        209,
        3,
        2272,
        111,
        2551,
        863,
        802,
        207,
        1218,
        1751,
        735,
        673,
        1870,
        712,
        139,
        33,
        63,
        2369,
        239,
        1615,
        1489,
        1203,
        459,
        97,
        403,
        1326,
        2707,
        1376,
        1282,
        1647,
        135,
        332,
        1584,
        1631,
        847,
        1337,
        287,
        287,
        1658,
        4,
        392,
        1048,
        799,
        389,
        316,
        880,
        905,
        896,
        456,
        557,
        2038,
        1512,
        706,
        229,
        343,
        1420,
        1458,
        34,
        2009,
        2251,
        1095,
        746,
        2742,
        1269,
        119,
        1361,
        2050,
        844,
        341,
        1425,
        1793,
        342,
        515,
        779,
        823,
        5,
        1220,
        458,
        1356,
        2433,
        501,
        2265,
        1441,
        1503,
        1535,
        1845,
        1921,
        2849,
        1759,
        1743,
        2642,
        815,
        2785,
        1930,
        1846,
        1980,
        1877,
        1838,
        1887,
        2391,
        1814,
        1424,
        1630,
        1561,
        1685,
        1727,
        935,
        2147,
        191,
        1611,
        1662,
        1160,
        1266,
        2264,
        1688,
        1716,
        1903,
        606,
        94,
        867,
        1287,
        # insert next challenge here
    ]
    if int(challenge_id) == -1:
        challenge_id = implemented_challenges[-1]

    if int(challenge_id) not in implemented_challenges:
        print(
            "Required argument challenge_id: must be a value of "
            + implemented_challenges.__str__()
        )
        return -1

    tests = []
    if int(challenge_id) == 2305:
        tests = ""
        for k in [7, *range(2, 9)]:
            cookies = [random.randint(1, 100000) for i in range(8)]
            tests += "\n".join([kwa.__str__() for kwa in [cookies, k]]) + "\n"

    if int(challenge_id) == 1514:
        tests.extend(
            [
                get_testcase_random(),
                get_testcase_random(),
                get_testcase_random(),
                #
                get_testcase_uniform(),
                get_testcase_uniform(),
            ]
        )
        tests = "\n".join([kwa.__str__() for kwa in tests])

    if int(challenge_id) == 864:
        grid = ["".join(["." for i in range(30)]) for j in range(30)]

        replace_grid_field(grid, 0, 0, "@")
        replace_grid_field(grid, 29, 29, "b")
        replace_grid_field(grid, 20, 1, "a")
        replace_grid_field(grid, 20, 2, "#")
        replace_grid_field(grid, 21, 0, "#")
        replace_grid_field(grid, 21, 1, "B")
        replace_grid_field(grid, 21, 2, "#")
        replace_grid_field(grid, 15, 15, "A")
        replace_grid_field(grid, 14, 16, "#")
        replace_grid_field(grid, 13, 17, "#")

        test = '["' + '","'.join([row.__str__() for row in grid]) + '"]'

        test2 = '["@......#.............#........",".......#######......dB........","#####..#.....#......##........",".......#...#.#..........#.....","...........#.#..........#.....","....########............#.a...","............f...........#.....","######.#E#######D########C####",".......#e...F...........#.....",".......######..........##.....",".......#..............#.......",".......#.......b....##........",".......#...........#..........",".......#.........##...........",".......#........#.............",".......#.......A..............",".......#......#...............",".......#######................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................","..............................",".............................c"]'
        tests = test + "\n" + test2

    if int(challenge_id) == 1970:
        row = 100
        col = 200
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests = "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 10000
        col = 2
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 2
        col = 10000
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 200
        col = 100
        cells = []
        for x in range(col):
            for y in range(row):
                cells.append([y + 1, x + 1])
        random.shuffle(cells)
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 200
        col = 100
        cells = []
        for x in range(col):
            for y in range(row - 1, -1, -1):
                cells.append([y + 1, x + 1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 3
        col = 6666
        cells = []
        for x in range(col):
            for y in range(row - 1, -1, -1):
                cells.append([y + 1, x + 1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

        row = 2
        col = 10000
        cells = []
        for x in range(col):
            for y in range(row - 1, -1, -1):
                cells.append([y + 1, x + 1])
        tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    if int(challenge_id) == 1601:
        tests = ""
        for test in range(8):
            building = 20
            request_count = 16
            requests = []
            for i in range(request_count):
                requests.append(
                    [random.randint(0, building - 1), random.randint(0, building - 1)]
                )
            tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

        building = 20
        requests = [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [3, 4],
            [4, 3],
            [3, 4],
            [4, 3],
            [3, 4],
            [4, 3],
        ]
        tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

        building = 4
        for orig in range(0, 4):
            for dest in range(0, 4):
                requests.append(orig, dest)
        tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

    if int(challenge_id) == 137:

        def numrandom(i):
            num = random.randint(-10000, 10000)
            num *= 10000
            num += i
            return num

        tests = []
        for test in range(8):
            n = 9999
            nums = []
            num = 0
            for i in range(n):
                num = numrandom(i)
                nums.append(num)
                nums.append(num)
                nums.append(num)
            i += 1
            num = numrandom(i)
            nums.append(num)
            random.shuffle(nums)
            tests.append(nums.__str__())
        tests = "\n".join(tests)

    if int(challenge_id) == 1493:
        nums = [0 for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [1 for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [random.randint(0, 1) for i in range(10 ** 5)]
        tests.append(nums.__str__())
        nums = [1]
        tests.append(nums.__str__())
        nums = [0]
        tests.append(nums.__str__())
        nums = [1, 1]
        tests.append(nums.__str__())
        nums = [0, 0]
        tests.append(nums.__str__())
        nums = [0, 1]
        tests.append(nums.__str__())
        nums = [1, 0]
        tests.append(nums.__str__())

        tests = "\n".join(tests)

    if int(challenge_id) == 209:
        tests = ["10000, \n[1337]", "10, \n[1337]"]

        for i in range(6):
            target = random.randint(1, 10 ** 9)
            nums = [random.randint(1, 10 ** 4) for i in range(10 ** 5)]
            tests.append(target.__str__() + "\n" + nums.__str__())
        tests = "\n".join(tests)

    if int(challenge_id) == 3:
        letters = """qwertyuiopsdfghjklzxcvbnm,.1234567890-=+_"""
        tests = [" ", "", "0", "1", "4", "10", "*", "-"]
        x = ["1", "2", "3"]
        tests.append("".join(["A" for i in range(5 * 10 ** 4)]))
        tests.append("".join(["A" for i in range(5 * 10 ** 4 - 1)]) + "B")
        tests.append("B" + "".join(["A" for i in range(5 * 10 ** 4 - 2)]) + "B")
        tests.append("B" + "".join(["A" for i in range(5 * 10 ** 4 - 2)]))
        tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=3)])
        tests.extend(["".join(list(p)) for p in itertools.product(x, repeat=4)])
        for i in range(8):
            test = "".join(
                [
                    letters[random.randint(0, len(letters) - 1)]
                    for i in range(5 * 10 ** 4)
                ]
            )
            tests.append(test)
        tests = "\n".join(['"' + test + '"' for test in tests])

    if int(challenge_id) == 2272:
        letters = "abc"
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        letters = "zyqwertyuiopasdfghjklzxcvbnmabc"
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        test = [random.choice(letters) for i in range(10 ** 4)]
        tests.append('"' + "".join(test) + '"')
        tests = "\n".join(tests)

    if int(challenge_id) == 111:
        trees = ["[]", "[1]"]
        tree = [1]
        tree.extend([1 for i in range(10 ** 5 - 1)])
        trees.append(tree.__str__())

        vals = [1, None]
        tree = [1]
        tree.extend([None for i in range(10 ** 5 - 1)])
        for i in range(150):
            if 2 ** i + 1 < len(tree):
                tree[2 ** i] = 1
                # tree[i**2-1] = 1
            else:
                break
            # print(i, i**2, tree[i**2])

        trees.append(tree.__str__())
        tests = "\n".join(trees)

    if int(challenge_id) == 2551:
        tests = []
        for n in range(8):
            weights = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]
            k = random.randint(1, len(weights))
            test = weights.__str__() + "\n" + k.__str__()
            tests.append(test)
        tests = "\n".join(tests)

    if int(challenge_id) == 863:
        tests = []
        possible_values = [i for i in range(500)]
        for test in range(8):
            tree = []
            number_of_nodes = 488
            # tree = possible_values
            tree.extend(random.sample(possible_values, number_of_nodes))
            target = tree[-1]
            distance = test * 3
            tests.append(
                "\n".join([tree.__str__(), target.__str__(), distance.__str__()])
            )
        tests = "\n".join(tests)

    if int(challenge_id) == 802:
        tests = []
        # min test
        graph = [[0]]
        tests.append(graph.__str__())

        graph = [[0], [1]]
        tests.append(graph.__str__())

        graph = [[0, 1], [0, 1]]
        tests.append(graph.__str__())

        graph = [[], [1], []]
        tests.append(graph.__str__())

        possible_edges = [i for i in range(10 ** 4 - 2)]
        for test in range(4):
            graph = []
            number_of_edges_sum = 0
            for node in range(10 ** 4 - 2):
                number_of_edges = random.randint(0, 6)
                number_of_edges_sum += number_of_edges
                graph.append(sorted(random.sample(possible_edges, number_of_edges)))
            print(number_of_edges_sum)
            tests.append(graph.__str__())

        for test in range(4):
            graph = []
            number_of_edges = 0
            number_of_edges_sum = 0
            for node in range(10 ** 4 - 2):
                number_of_edges = 6 - (node // 1500)
                number_of_edges %= len(possible_edges)
                graph.append(sorted(random.sample(possible_edges, number_of_edges)))
                number_of_edges_sum += number_of_edges
            print(number_of_edges, number_of_edges_sum)
            tests.append(graph.__str__())
        tests = "\n".join(tests)

    if int(challenge_id) == 207:
        tests = []
        # min test
        number_of_nodes = 1
        graph = [[0, 0]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 2
        graph = [[0, 0], [1, 1]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 2
        graph = [[0, 1], [1, 0], [0, 0], [1, 1]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 5
        graph = []
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 3
        graph = [[1, 1]]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        # giant loop
        number_of_nodes = 2000
        graph = [[i, (i + 1) % 2000] for i in range(number_of_nodes)]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        # giant line
        number_of_nodes = 2000
        graph = [[i, (i + 1) % 2000] for i in range(number_of_nodes - 1)]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        # giant reverse line
        number_of_nodes = 2000
        graph = [[i - 1, i] for i in range(1, number_of_nodes)]
        tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        number_of_nodes = 2000
        possible_edges = [i for i in range(number_of_nodes)]
        for test in range(4):
            graph = []
            number_of_edges_sum = 0
            for node in range(number_of_nodes):
                number_of_edges = random.randint(0, 4)
                number_of_edges_sum += number_of_edges
                edges = random.sample(possible_edges, number_of_edges)
                for e in edges:
                    graph.append([node, e])
            print(number_of_edges_sum)
            tests.append(str(number_of_nodes) + "\n" + graph.__str__())

        for test in range(4):
            graph = []
            number_of_edges = 0
            number_of_edges_sum = 0
            for node in range(number_of_nodes):
                number_of_edges = random.randint(0, 10)
                number_of_edges_sum += number_of_edges
                if number_of_edges_sum >= 5000:
                    number_of_edges_sum -= number_of_edges
                    break
                edges = random.sample(possible_edges, number_of_edges)
                for e in edges:
                    graph.append([node, e])
            print(number_of_edges, number_of_edges_sum)
            tests.append(str(number_of_nodes) + "\n" + graph.__str__())
        tests = "\n".join(tests)

    if int(challenge_id) == 1218:
        from . import Generator1218
        tests = Generator1218.generate()

    if int(challenge_id) == 1751:
        from . import Generator1751
        tests = Generator1751.generate()

    if int(challenge_id) == 735:
        from . import Generator735
        tests = Generator735.generate()

    if int(challenge_id) == 673:
        from . import Generator673
        tests = Generator673.generate()

    if int(challenge_id) == 1870:
        from . import Generator1870
        tests = Generator1870.generate()

    if int(challenge_id) == 712:
        from . import Generator712
        tests = Generator712.generate()

    if int(challenge_id) == 139:
        from . import Generator139
        tests = Generator139.generate()

    if int(challenge_id) == 33:
        from . import Generator33
        tests = Generator33.generate()

    if int(challenge_id) == 63:
        from . import Generator63
        tests = Generator63.generate()

    if int(challenge_id) == 2369:
        from . import Generator2369
        tests = Generator2369.generate()

    if int(challenge_id) == 239:
        from . import Generator239
        tests = Generator239.generate()

    if int(challenge_id) == 1615:
        from . import Generator1615
        tests = Generator1615.generate()

    if int(challenge_id) == 1489:
        from . import Generator1489
        tests = Generator1489.generate()

    if int(challenge_id) == 1203:
        from . import Generator1203
        tests = Generator1203.generate()

    if int(challenge_id) == 459:
        from . import Generator459
        tests = Generator459.generate()

    if int(challenge_id) == 97:
        from . import Generator97
        tests = Generator97.generate()

    if int(challenge_id) == 403:
        from . import Generator403
        tests = Generator403.generate()

    if int(challenge_id) == 1326:
        from . import Generator1326
        tests = Generator1326.generate()

    if int(challenge_id) == 2707:
        from . import Generator2707
        tests = Generator2707.generate()

    if int(challenge_id) == 1376:
        from . import Generator1376
        tests = Generator1376.generate()

    if int(challenge_id) == 1282:
        from . import Generator1282
        tests = Generator1282.generate()

    if int(challenge_id) == 1647:
        from . import Generator1647
        tests = Generator1647.generate()

    if int(challenge_id) == 135:
        from . import Generator135
        tests = Generator135.generate()

    if int(challenge_id) == 332:
        from . import Generator332
        tests = Generator332.generate()

    if int(challenge_id) == 1584:
        from . import Generator1584
        tests = Generator1584.generate()

    if int(challenge_id) == 1631:
        from . import Generator1631
        tests = Generator1631.generate()

    if int(challenge_id) == 847:
        from . import Generator847
        tests = Generator847.generate()

    if int(challenge_id) == 1337:
        from . import Generator1337
        tests = Generator1337.generate()

    if int(challenge_id) == 287:
        from . import Generator287
        tests = Generator287.generate()

    if int(challenge_id) == 287:
        from . import Generator287
        tests = Generator287.generate()

    if int(challenge_id) == 1658:
        from . import Generator1658
        tests = Generator1658.generate()

    if int(challenge_id) == 4:
        from . import Generator4
        tests = Generator4.generate()

    if int(challenge_id) == 392:
        from . import Generator392
        tests = Generator392.generate()

    if int(challenge_id) == 1048:
        from . import Generator1048
        tests = Generator1048.generate()

    if int(challenge_id) == 799:
        from . import Generator799
        tests = Generator799.generate()

    if int(challenge_id) == 389:
        from . import Generator389
        tests = Generator389.generate()

    if int(challenge_id) == 316:
        from . import Generator316
        tests = Generator316.generate()

    if int(challenge_id) == 880:
        from . import Generator880
        tests = Generator880.generate()

    if int(challenge_id) == 905:
        from . import Generator905
        tests = Generator905.generate()

    if int(challenge_id) == 896:
        from . import Generator896
        tests = Generator896.generate()

    if int(challenge_id) == 456:
        from . import Generator456
        tests = Generator456.generate()

    if int(challenge_id) == 557:
        from . import Generator557
        tests = Generator557.generate()

    if int(challenge_id) == 2038:
        from . import Generator2038
        tests = Generator2038.generate()

    if int(challenge_id) == 1512:
        from . import Generator1512
        tests = Generator1512.generate()

    if int(challenge_id) == 706:
        from . import Generator706
        tests = Generator706.generate()

    if int(challenge_id) == 229:
        from . import Generator229
        tests = Generator229.generate()

    if int(challenge_id) == 343:
        from . import Generator343
        tests = Generator343.generate()

    if int(challenge_id) == 1420:
        from . import Generator1420
        tests = Generator1420.generate()

    if int(challenge_id) == 1458:
        from . import Generator1458
        tests = Generator1458.generate()

    if int(challenge_id) == 34:
        from . import Generator34
        tests = Generator34.generate()

    if int(challenge_id) == 2009:
        from . import Generator2009
        tests = Generator2009.generate()

    if int(challenge_id) == 2251:
        from . import Generator2251
        tests = Generator2251.generate()

    if int(challenge_id) == 1095:
        from . import Generator1095
        tests = Generator1095.generate()

    if int(challenge_id) == 746:
        from . import Generator746
        tests = Generator746.generate()

    if int(challenge_id) == 2742:
        from . import Generator2742
        tests = Generator2742.generate()

    if int(challenge_id) == 1269:
        from . import Generator1269
        tests = Generator1269.generate()

    if int(challenge_id) == 119:
        from . import Generator119
        tests = Generator119.generate()

    if int(challenge_id) == 1361:
        from . import Generator1361
        tests = Generator1361.generate()

    if int(challenge_id) == 2050:
        from . import Generator2050
        tests = Generator2050.generate()

    if int(challenge_id) == 844:
        from . import Generator844
        tests = Generator844.generate()

    if int(challenge_id) == 341:
        from . import Generator341
        tests = Generator341.generate()

    if int(challenge_id) == 1425:
        from . import Generator1425
        tests = Generator1425.generate()

    if int(challenge_id) == 1793:
        from . import Generator1793
        tests = Generator1793.generate()

    if int(challenge_id) == 342:
        from . import Generator342
        tests = Generator342.generate()

    if int(challenge_id) == 515:
        from . import Generator515
        tests = Generator515.generate()

    if int(challenge_id) == 779:
        from . import Generator779
        tests = Generator779.generate()

    if int(challenge_id) == 823:
        from . import Generator823
        tests = Generator823.generate()

    if int(challenge_id) == 5:
        from . import Generator5
        tests = Generator5.generate()

    if int(challenge_id) == 1220:
        from . import Generator1220
        tests = Generator1220.generate()

    if int(challenge_id) == 458:
        from . import Generator458
        tests = Generator458.generate()

    if int(challenge_id) == 1356:
        from . import Generator1356
        tests = Generator1356.generate()

    if int(challenge_id) == 2433:
        from . import Generator2433
        tests = Generator2433.generate()

    if int(challenge_id) == 501:
        from . import Generator501
        tests = Generator501.generate()

    if int(challenge_id) == 2265:
        from . import Generator2265
        tests = Generator2265.generate()

    if int(challenge_id) == 1441:
        from . import Generator1441
        tests = Generator1441.generate()

    if int(challenge_id) == 1503:
        from . import Generator1503
        tests = Generator1503.generate()

    if int(challenge_id) == 1535:
        from . import Generator1535
        tests = Generator1535.generate()

    if int(challenge_id) == 1845:
        from . import Generator1845
        tests = Generator1845.generate()

    if int(challenge_id) == 1921:
        from . import Generator1921
        tests = Generator1921.generate()

    if int(challenge_id) == 2849:
        from . import Generator2849
        tests = Generator2849.generate()

    if int(challenge_id) == 1759:
        from . import Generator1759
        tests = Generator1759.generate()

    if int(challenge_id) == 1743:
        from . import Generator1743
        tests = Generator1743.generate()

    if int(challenge_id) == 2642:
        from . import Generator2642
        tests = Generator2642.generate()

    if int(challenge_id) == 815:
        from . import Generator815
        tests = Generator815.generate()

    if int(challenge_id) == 2785:
        from . import Generator2785
        tests = Generator2785.generate()

    if int(challenge_id) == 1930:
        from . import Generator1930
        tests = Generator1930.generate()

    if int(challenge_id) == 1846:
        from . import Generator1846
        tests = Generator1846.generate()

    if int(challenge_id) == 1980:
        from . import Generator1980
        tests = Generator1980.generate()

    if int(challenge_id) == 1877:
        from . import Generator1877
        tests = Generator1877.generate()

    if int(challenge_id) == 1838:
        from . import Generator1838
        tests = Generator1838.generate()

    if int(challenge_id) == 1887:
        from . import Generator1887
        tests = Generator1887.generate()

    if int(challenge_id) == 2391:
        from . import Generator2391
        tests = Generator2391.generate()

    if int(challenge_id) == 1814:
        from . import Generator1814
        tests = Generator1814.generate()

    if int(challenge_id) == 1424:
        from . import Generator1424
        tests = Generator1424.generate()

    if int(challenge_id) == 1630:
        from . import Generator1630
        tests = Generator1630.generate()

    if int(challenge_id) == 1561:
        from . import Generator1561
        tests = Generator1561.generate()

    if int(challenge_id) == 1685:
        from . import Generator1685
        tests = Generator1685.generate()

    if int(challenge_id) == 1727:
        from . import Generator1727
        tests = Generator1727.generate()

    if int(challenge_id) == 935:
        from . import Generator935
        tests = Generator935.generate()

    if int(challenge_id) == 2147:
        from . import Generator2147
        tests = Generator2147.generate()

    if int(challenge_id) == 191:
        from . import Generator191
        tests = Generator191.generate()

    if int(challenge_id) == 1611:
        from . import Generator1611
        tests = Generator1611.generate()

    if int(challenge_id) == 1662:
        from . import Generator1662
        tests = Generator1662.generate()

    if int(challenge_id) == 1160:
        from . import Generator1160
        tests = Generator1160.generate()

    if int(challenge_id) == 1266:
        from . import Generator1266
        tests = Generator1266.generate()

    if int(challenge_id) == 2264:
        from . import Generator2264
        tests = Generator2264.generate()

    if int(challenge_id) == 1688:
        from . import Generator1688
        tests = Generator1688.generate()

    if int(challenge_id) == 1716:
        from . import Generator1716
        tests = Generator1716.generate()

    if int(challenge_id) == 1903:
        from . import Generator1903
        tests = Generator1903.generate()

    if int(challenge_id) == 606:
        from . import Generator606
        tests = Generator606.generate()

    if int(challenge_id) == 94:
        from . import Generator94
        tests = Generator94.generate()

    if int(challenge_id) == 867:
        from . import Generator867
        tests = Generator867.generate()

    if int(challenge_id) == 1287:
        from . import Generator1287
        tests = Generator1287.generate()

    # insert next challenge import here

    date = time.time()
    write_file(f"testcase_{challenge_id}_{int(date)}.txt", tests)
