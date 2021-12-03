# row, column = 5, 5
# # sample = [['a']*column for i in range(row)]
# # print(sample)

# C = int(input(""));
# sample = [['']*column for i in range(row)]
# words = []
# answer = ''

# for i in range(5):
#     t = input("");
#     for j in range(5):
#         sample[i][j] = t[j];

# N = int(input(""));
# for i in range(N):
#     word = input("")
#     words.append(word)


# for i in range(len(sample)):
#     num = 0
#     for j in range(len(sample[i])):
#         if sample[i][j] == words[i][num]:
xy = [ (-1,-1),(0,-1),(1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1), ]

def find_word_st(dx, dy, wd, index):
    for(x,y) in xy:
        if dy+y > 4 or dy+y < 0 or dx+x > 4 or dx+x < 0:
            continue

        if board[dy+y][dx+x] is wd[index] :
            if length == index+1:
                return True
            if find_word_st(dx+x, dy+y, wd, index+1) :
                return True


def find_word_ch(wd):
    global length
    length = len(wd)

    for dy in range(0, 5):
        for dx, ch in enumerate(board[dy]):
            if wd[0] is ch:
                if find_word_st(dx, dy, wd, 1) is True:
                    return 'YES'
    return "NO"



    
for i in range(int(input())):
    board = []

    for i in range(0, 5):
        board.append(input())

    word = []

    for i in range(0, int(input())):
        word.append(input())


    for wd in word:
        print("{0} {1}".format(wd, find_word_ch(wd)))




