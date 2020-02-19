import random


def make_move_steepest_hill(board):
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
    if len(best_moves) > 0:
        select = random.randint(0, len(best_moves) - 1)
        col = best_moves[select][0]
        row = best_moves[select][1]
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


    sn=0
    fn=0
    success=[]
    fail=[]
    for i in range(0,500):
        p=0
        board=[]
        for j in range(N):
            board.append(random.randint(0, N-1))
        # board=random.sample(range(0,N),N)
        print_board(board,N)
        heu=h_value(board)
        print("heuristic", heu, "\n")
        l=0
        while heu!=0:
            # if (h == 1):
            #     l = l + 1
            newboard=make_move_steepest_hill(board)
            hnew=h_value(newboard)
            if (heu == hnew):
                print("failure", "\n")
                fn = fn + 1
                fail.append(p)
                break
            heu=hnew
            print_board(board, N)
            p=p+1

            #if (u=sn):
            #print("d")
            print("heuristic:", heu, "\n")
            if (heu == 0):
                print("success", "\n")
                sn = sn + 1
                success.append(p)




    a=sn/5
    b=fn/5
    d=float("{0:.4f}".format(sum(success) / len(success)))
    e=float("{0:.4f}".format(sum(fail) / len(fail)))

    return  a,b,d,e


if __name__ == "__main__":
    N = int(input("Enter value of N for N Queen problem"))
    a,b,d,e=main(N)
    print("Percentage success",a)
    print("Percentage failure",b)
    print("Average steps to get success",d)
    print("Average steps to fail",e)
