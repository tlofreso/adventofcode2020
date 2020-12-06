from rich import print


def values():

    with open("input.txt") as f:
        my_input = f.read().splitlines()

    return my_input


def puzzle1():

    seats = values()
    to_bin_dict = {ord("F"): "0", ord("B"): "1", ord("R"): "1", ord("L"): "0"}

    my_map = []
    for seat in seats:
        seat = seat.translate(to_bin_dict)
        row = seat[0:7]
        col = seat[7:10]
        seat_map = [row, col]
        my_map.append(seat_map)

    my_seats = []
    for seat in my_map:
        row = int(seat[0], 2)
        col = int(seat[1], 2)
        seat_map = [row, col]
        my_seats.append(seat_map)

    seat_ids = []
    for seat in my_seats:
        seat_id = seat[0] * 8 + seat[1]
        seat_ids.append(seat_id)

    return sorted(seat_ids)


def puzzle2(lst):
    start = lst[0]
    end = lst[-1]

    # thing = [seat for seat in range(seats[0], seats[-1] + 1) if seat not in seats]
    # return sorted(set(range(lst[0], lst[-1])) - set(lst))
    # return sorted(set(range(lst[0], lst[-1])))
    return sorted(set(range(start, end + 1)).difference(lst))


if __name__ == "__main__":

    print(max(puzzle1()))
    lst = puzzle1()
    print(puzzle2(lst))