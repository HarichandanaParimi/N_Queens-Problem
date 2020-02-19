import random
import sidewayMoves


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


    steps_s=[]
    avg_b=[]
    for i in range(0,500):
        flag = 1
        step = 0
        l=0
        while flag !=0:
            board = []
            for j in range(N):
                board.append(random.randint(0, N - 1))
            l = l + 1
            print_board(board, N)
            h = h_value(board)
            print("heuristic=", h, "\n")
            while h != 0:
                newboard = sidewayMoves.make_move_steepest_hill(board)
                hnew = h_value(newboard)
                if (h == hnew):
                    print("failure", "\n")
                    break
                h = hnew
                print_board(board, N)



                print("heuristic=", h, "\n")
                if (h == 0):
                    print("success", "\n")
                    flag=0
                    steps_s.append(step)
                    avg_b.append(l)
                step = step + 1

    a=sum(avg_b)/len(avg_b)
    b=sum(steps_s) / len(steps_s)

    print("Average iterations",a)
    print("Average steps",b)


if __name__ == "__main__":
    N = int(input("Enter value of N for N Queen problem"))
    main(N)

