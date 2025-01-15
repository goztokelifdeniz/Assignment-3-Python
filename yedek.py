import sys


def print_score(score):
    print(f"\nYour score is: {score}")


def print_board(game_list, column_num):
    for index in range(len(game_list)):
        if (index+1) % column_num == 0:
            print(game_list[index][0], end="\n")
        else:
            print(game_list[index][0], end=" ")


def find_column_amount():
    amount_of_numbers_in_board = len(turn_file_into_list())
    row_amount = find_row_amount()
    column_amount = amount_of_numbers_in_board // row_amount
    return column_amount


def turn_file_into_list():
    input_board = open(sys.argv[1], "r")
    input_board_str = input_board.read()
    input_list = [[int(char)] for char in input_board_str if char != " " if char != "\n"]
    input_board.close()
    return input_list


def find_row_amount():
    input_board = open(sys.argv[1], "r")
    row_amount = input_board.read().count("\n") + 1
    input_board.close()
    return row_amount


def add_invalid_marking_as_a_start(list1):
    for i in range(len(list1)):
        list1[i].append("-")
    return list1


def is_game_over(list2, row_num, col_num):
    game_is_over = True
    for index in range(len(list2)):
        if list2[index][0] != " ":
            if row_num > 1 and col_num > 1:  # there are more than one row and column
                if index < col_num:  # top row
                    if index == 0:  # top left corner
                        if list2[index][0] == list2[index + 1][0] or list2[index][0] == list2[index + col_num][0]:
                            game_is_over = False
                    elif (index + 1) == col_num:  # top right corner
                        if list2[index][0] == list2[index - 1][0] or list2[index][0] == list2[index + col_num][0]:
                            game_is_over = False
                    else:  # rest of the top row
                        if (list2[index][0] == list2[index + 1][0] or list2[index][0] == list2[index - 1][0]
                                or list2[index][0] == list2[index + col_num][0]):
                            game_is_over = False

                elif index > (len(list2) - col_num - 1):  # bottom row
                    if index == len(list2) - col_num:  # bottom left corner
                        if list2[index][0] == list2[index + 1][0] or list2[index][0] == list2[index - col_num][0]:
                            game_is_over = False
                    elif index == (len(list2) - 1):  # bottom right corner
                        if list2[index][0] == list2[index - 1][0] or list2[index][0] == list2[index - col_num][0]:
                            game_is_over = False
                    else:  # rest of the bottom row
                        if (list2[index][0] == list2[index + 1][0] or list2[index][0] == list2[index - 1][0]
                                or list2[index][0] == list2[index - col_num][0]):
                            game_is_over = False

                else:  # rows between the top and the middle row
                    if index % col_num == 0:  # on the left edge
                        if (list2[index][0] == list2[index + 1][0] or list2[index][0] == list2[index + col_num][0]
                                or list2[index][0] == list2[index - col_num][0]):
                            game_is_over = False
                    elif (index + 1) % col_num == 0:  # on the right edge
                        if (list2[index][0] == list2[index - 1][0] or list2[index][0] == list2[index + col_num][0]
                                or list2[index][0] == list2[index - col_num][0]):
                            game_is_over = False
                    else:  # rest of the board
                        if (list2[index][0] == list2[index + 1][0] or list2[index][0] == list2[index - 1][0]
                                or list2[index][0] == list2[index + col_num][0]
                                or list2[index][0] == list2[index - col_num][0]):
                            game_is_over = False
            elif row_num == 1 and col_num == 1:  # there is only one number left
                game_is_over = True
            else:  # either (row_num == 1 and col_num > 1) or (row_num > 1 and col_num == 1)
                if index == 0:
                    if list2[index][0] == list2[index + 1][0]:
                        game_is_over = False
                elif index == (len(list2) - 1):
                    if list2[index][0] == list2[index - 1][0]:
                        game_is_over = False
                else:
                    if list2[index][0] == list2[index + 1][0] or list2[index][0] == list2[index - 1][0]:
                        game_is_over = False
    return game_is_over


def cell_has_a_valid_neighbor(list3, col_num, input_row, input_column):
    index = (input_row - 1) * col_num + input_column - 1
    if index < col_num:  # top row
        if index == 0:  # top left corner
            if list3[index][0] == list3[index + 1][0] or list3[index][0] == list3[index + col_num][0]:
                return True
        elif (index + 1) == col_num:  # top right corner
            if list3[index][0] == list3[index - 1][0] or list3[index][0] == list3[index + col_num][0]:
                return True
        else:  # rest of the top row
            if (list3[index][0] == list3[index + 1][0] or list3[index][0] == list3[index - 1][0]
                    or list3[index][0] == list3[index + col_num][0]):
                return True

    elif index > (len(list3) - col_num - 1):  # bottom row
        if index == len(list3) - col_num:  # bottom left corner
            if list3[index][0] == list3[index + 1][0] or list3[index][0] == list3[index - col_num][0]:
                return True
        elif index == (len(list3) - 1):  # bottom right corner
            if list3[index][0] == list3[index - 1][0] or list3[index][0] == list3[index - col_num][0]:
                return True
        else:  # rest of the bottom row
            if (list3[index][0] == list3[index + 1][0] or list3[index][0] == list3[index - 1][0]
                    or list3[index][0] == list3[index - col_num][0]):
                return True

    else:  # rows between the top and the middle row
        if index % col_num == 0:  # on the left edge
            if (list3[index][0] == list3[index + 1][0] or list3[index][0] == list3[index + col_num][0]
                    or list3[index][0] == list3[index - col_num][0]):
                return True
        elif (index + 1) % col_num == 0:  # on the right edge
            if (list3[index][0] == list3[index - 1][0] or list3[index][0] == list3[index + col_num][0]
                    or list3[index][0] == list3[index - col_num][0]):
                return True
        else:  # rest of the board
            if (list3[index][0] == list3[index + 1][0] or list3[index][0] == list3[index - 1][0]
                    or list3[index][0] == list3[index + col_num][0] or list3[index][0] == list3[index - col_num][0]):
                return True
    return False


def mark_chosen_cell_and_close_neighbors(list4, col_num, input_row, input_column):
    index = (input_row - 1) * col_num + input_column - 1
    list4[index][1] = "+"  # the cell chosen by user

    if not (index + 1) % col_num == 0:  # if the cell is not on the right edge of the board
        if list4[index][0] == list4[index + 1][0]:  # check right neighbor
            list4[index + 1][1] = "+"
    if not index % col_num == 0:  # if the cell is not on the left edge of the board
        if list4[index][0] == list4[index - 1][0]:  # check left neighbor
            list4[index - 1][1] = "+"
    if not index > (len(list4) - col_num - 1):  # if the cell is not on the bottom row
        if list4[index][0] == list4[index + col_num][0]:  # check down neighbor
            list4[index + col_num][1] = "+"
    if not index < col_num:  # if the cell is not on the top row
        if list4[index][0] == list4[index - col_num][0]:  # check up neighbor
            list4[index - col_num][1] = "+"

    return list4


def mark_far_neighbors(list5, row_num, col_num):
    if row_num > 3:
        checking_times = row_num
    else:  # so that even when r is small, list can be checked properly
        checking_times = 3
    for times in range(checking_times):
        for index in range(len(list5)):
            if list5[index][1] == "+":
                if not (index + 1) % col_num == 0:
                    if list5[index][0] == list5[index + 1][0]:
                        list5[index + 1][1] = "+"
                if not index % col_num == 0:
                    if list5[index][0] == list5[index - 1][0]:
                        list5[index - 1][1] = "+"
                if not index > (len(list5) - col_num - 1):
                    if list5[index][0] == list5[index + col_num][0]:
                        list5[index + col_num][1] = "+"
                if not index < col_num:
                    if list5[index][0] == list5[index - col_num][0]:
                        list5[index - col_num][1] = "+"

    return list5


def destroy_valid_cells_add_to_score_update_marks(list6, score):
    for index in range(len(list6)):
        if list6[index][1] == "+":
            if list6[index][0] != " ":
                score = score + int(list6[index][0])
            list6[index][0] = " "
            list6[index][1] = "-"
    return list6, score


def erase_empty_rows_and_update_row_num(list7, row_num, col_num):
    for checking_times in range(row_num):
        for rows in range(0, (len(list7) - col_num + 1), col_num):
            row_is_empty = True
            for in_row in range(col_num):
                if not list7[rows + in_row][0] == " ":
                    row_is_empty = False

            if row_is_empty:
                for whole_row in range(col_num):
                    list7.pop(rows)
                row_num = row_num - 1
                break
    return list7, row_num


def erase_empty_columns_and_update_col_num(list8, row_num, col_num):
    for checking_times in range(col_num):
        for cols in range(col_num):
            col_is_empty = True
            for in_col in range(0, (row_num - 1) * col_num + 1, col_num):
                if not list8[cols + in_col][0] == " ":
                    col_is_empty = False

            if col_is_empty:
                for whole_col in range(0, row_num * (col_num - 1), col_num - 1):
                    list8.pop(cols + whole_col)
                col_num = col_num - 1
                break
    return list8, col_num


def cells_slide_down_if_their_down_neighbor_is_empty(list9, row_num, col_num):
    for checking_times in range(row_num):
        for index in range(0, (row_num - 1) * col_num):
            if list9[index + col_num][0] == " ":
                list9[index + col_num][0] = list9[index][0]
                list9[index][0] = " "
    return list9


def play_board_game(list10, row_num, col_num, score):
    game_is_over = is_game_over(list10, row_num, col_num)
    if not game_is_over:
        user_input = input("Please enter head row and head column number: ")
        print("")
        input_row, input_column = user_input.split(" ")
        input_row = int(input_row)
        input_column = int(input_column)
        if 1 <= input_row <= row_num and 1 <= input_column <= col_num:
            if cell_has_a_valid_neighbor(list10, col_num, input_row, input_column):
                first_marked_list = mark_chosen_cell_and_close_neighbors(list10, col_num, input_row, input_column)
                second_marked_list = mark_far_neighbors(first_marked_list, row_num, col_num)
                destroyed_list, score = destroy_valid_cells_add_to_score_update_marks(second_marked_list, score)
                row_erased_list, row_num = erase_empty_rows_and_update_row_num(destroyed_list, row_num, col_num)
                if len(row_erased_list) == 0:
                    print_score(score)
                    print("")
                    print("Game over")
                else:
                    col_erased_list, col_num = erase_empty_columns_and_update_col_num(row_erased_list, row_num, col_num)
                    if len(col_erased_list) == 0:
                        print_score(score)
                        print("")
                        print("Game over")
                    else:
                        slid_list = cells_slide_down_if_their_down_neighbor_is_empty(col_erased_list, row_num, col_num)
                        last_list, row_num = erase_empty_rows_and_update_row_num(slid_list, row_num, col_num)
                        if not is_game_over(list10, row_num, col_num):
                            print_board(last_list, col_num)
                            print_score(score)
                            print("")
                            play_board_game(last_list, row_num, col_num, score)
                        else:
                            if len(list10) == 0:
                                print("\n")
                            else:
                                print_board(list10, col_num)
                            print_score(score)
                            print("")
                            print("Game over")

            else:
                print("No movement happened try again")
                print("")
                print_board(list10, col_num)
                print_score(score)
                print("")
                play_board_game(list10, row_num, col_num, score)
        else:
            print("Please enter head correct size!")
            print("")
            play_board_game(list10, row_num, col_num, score)
    else:
        if len(list10) == 0:
            print("\n")
        else:
            print("")
            print_board(list10, col_num)
            print("")
        print_score(score)
        print("")
        print("Game over")


def main():
    row = find_row_amount()
    col = find_column_amount()
    board_list = turn_file_into_list()
    score = 0

    print_board(board_list, col)
    print_score(score)
    print("")
    add_invalid_marking_as_a_start(board_list)
    play_board_game(board_list, row, col, score)


if __name__ == "__main__":
    main()
