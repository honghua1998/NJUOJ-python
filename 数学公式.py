if __name__ == '__main__':
    for _ in range(int(input())):
        a,b,c = list(map(int,input().strip().split(" ")))
        ans  = 1
        while b >0:
            if b & 1 == 1:
                ans *= a

            a = ((a%c)*(a%c))%c
            b = b >> 1

        print(ans %c)