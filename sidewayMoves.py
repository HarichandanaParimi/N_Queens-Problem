import random


p_moves=[]
f=0

def make_move_steepest_hill(board):
    global p_moves
    global f
    mn = {}
    for col in range(len(board)):
        best_move = board[col]

        for row in range(len(board)):
            if board[col] == row:
                # We don't need to evaluate the current
                # position, we already know the h-value
                continue

            board_copy = list(board)
            # Move the queen to the new row
            board_copy[col] = row
            mn[(col, row)] = h_value(board_copy)


    best_moves = []
    h_to_beat = h_value(board)
    for i, j in mn.items():
        if j < h_to_beat:
            h_to_beat = j

    for i, j in mn.items():
        if j == h_to_beat:
            best_moves.append(i)

    # Pick a random best move
    p=0
    print("length of best moves",len(best_moves))
    if len(best_moves)==0:
        f=1
        return board
    if len(best_moves) > 0:
        print(best_moves)
        pick = random.randint(0, len(best_moves) - 1)
        print(" this is pick value",pick)
        col = best_moves[pick][0]
        row = best_moves[pick][1]
        board[col] = row

    return board


def print_board(board,N):
    import numpy as np
    board = np.array(board)
    board = N - 1 - board
    l = []
    for i, j in enumerate(board):
        l.append([i, j])

    for i in range(0, N):
        for j in range(0, N):
            if [j, i] in l:
                print("Q", end="")
            else:
                print("- ", end="")
        print(end="\n")


def h_value(board):
    hn = 0
    for l in range(len(board)):
        # checking each column
        for m in range(l + 1, len(board)):
            if board[l] == board[m]:
                hn += 1

            off_set = m - l

            if (board[l] == board[m] - off_set) or (board[l] == board[m] + off_set):
                hn += 1
    return hn


def main(N):
    global p_moves
    global f


    success_no=0
    failure_no=0
    step_succeed=[]
    step_fail=[]
    for i in range(0,500):
        step=0
        f=0
        board=[]
        print("board number = ",i+1)
        for j in range(N):
            board.append(random.randint(0, N-1))
        # board=random.sample(range(0,N),N)
        print_board(board,N)
        h=h_value(board)
        print("value of h=",h,"\n")
        l=0
        while h!=0:
            newboard=make_move_steepest_hill(board)

            hnew=h_value(newboard)

            if step == 100 or f==1:
                failure_no = failure_no + 1
                print("failure", "\n")
                step_fail.append(step)
                break

            h=hnew
            print_board(board, N)
            print(board)

            print("value of h=",h,"\n")
            step = step + 1
            if (h == 0):
                print("success", "\n")
                success_no = success_no + 1
                step_succeed.append(step)



    a= success_no/5
    b=failure_no/5
    d = float("{0:.4f}".format(sum(step_succeed) / len(step_succeed)))
    e = float("{0:.4f}".format(sum(step_fail) / len(step_fail)))

    return a,b,d,e


if __name__ == "__main__":
    N=int(input("Enter value of N for N Queen problem"))
    a,b,d,e=main(N)
    print("Percentage success=",a)
    print("Percentage failure",b)
    print("Average steps success",d)
    print("Average steps fail",e)
