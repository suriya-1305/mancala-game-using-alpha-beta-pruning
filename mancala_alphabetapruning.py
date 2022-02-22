class Board:
    def __init__(self, board ):
        if board!=None:
            self.board = board[:]
        else:
            self.board=[0 for i in range(14)]
            for i in range(0,6,1): self.board[i]=4
            for i in range(7, 13, 1): self.board[i] = 4
    def move(self, i):
        j=i
        againturn=False
        add=self.board[j]
        self.board[j] = 0
        if i>6:
            stones = add
            while(stones>0):
                i+=1
                i=i % 14
                if i==6 : continue
                else:
                    self.board[i%14]+=1
                stones-=1
            if i>6 and self.board[i]==1 and i!=13 and self.board[5-(i-7)]!=0:
                self.board[13]+=1+self.board[5-(i-7)]
                self.board[i]=0
                self.board[5-(i-7)]=0
            if i==13:
                againturn = True
        else:
            stones = add
            while (stones > 0):
                i += 1
                i = i % 14
                if i == 13:
                    continue
                else:
                    self.board[i%14] += 1
                stones -= 1
            if i < 6 and self.board[i] == 1 and i !=6 and self.board[-i + 12]!=0:
                self.board[6] += 1 + self.board[-i + 12]
                self.board[i] = 0
                self.board[-i + 12] = 0
            if i == 6:
                againturn = True
        return againturn
    def isEnd(self):
        if sum(self.board[0:6])==0 :
            self.board[13]+=sum(self.board[7:13])
            for i in range(14):
                if  (i != 13 and i != 6):
                    self.board[i] = 0
            return True
        elif sum(self.board[7:13])==0:
            self.board[6] += sum(self.board[0:6])
            for i in range(14):
                if  (i != 13 and i != 6):
                    self.board[i] = 0
            return True
        return False
    def printBoard(self):
        for i in range(12,6,-1):
            print('  ',self.board[i],'   ',end='')
        print('  ')
        print(self.board[13],'                                           ',self.board[6])

        for i in range(0,6,1):
            print('  ',self.board[i],'   ',end='')
        print('  ')
    def husVal(self):
        if self.isEnd():
            if self.board[13]>self.board[6]:
                return 100
            elif self.board[13]==self.board[6]:
                return 0
            else :
                 return -100
        else:
            return self.board[13]- self.board[6]
def alphabeta(board, depth, alpha, beta , MinorMax):
     if depth == 0 or board.isEnd():
         return board.husVal(),-1
     if MinorMax:
         v = -1000000
         move = -1
         for i in range(7,13,1):
             if board.board[i]==0: continue
             a=Board(board.board[:])
             minormax = a.move(i);
             newv,_ =  alphabeta(a, depth-1, alpha, beta, minormax)
             if v< newv:
                 move=i
                 v =newv
             alpha = max(alpha, v)
             if alpha >= beta :
                 break
         return v, move
     else:
         v = 1000000
         move = -1
         for i in range(0, 6, 1):
             if board.board[i] == 0: continue
             a = Board(board.board[:])
             minormax = a.move(i);
             newv,_ = alphabeta(a, depth - 1, alpha, beta, not  minormax)
             if v > newv:
                 move = i
                 v = newv
             beta = min(beta, v)
             if alpha >= beta:
                 break
         return v, move

if __name__ == "__main__":
    j=Board(None)
    j.printBoard()
    while(True):
        if j.isEnd():
            break
        while(True):
            if j.isEnd():
                break
            print("COMPUTER TURN ")
            _,k = alphabeta(j,10,-100000,100000,True)
            print('move-->',k)
            t=j.move(k)
            j.printBoard()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("PLAYER'S TURN ")
            h= int(input())
            if h>5 or j.board[h]==0:
                print('you can\'t play')
                break
            t=j.move(h)
            j.printBoard()
            if not t: break
    print('GAME ENDED')
    j.printBoard()
