def add_element(min_list, p1, p2):
    min_list.append(p1[0] + " " + p1[1] + ",")
    min_list.append(p2[0] + " " + p2[1] + ",")


def cal_dist(p1, p2):
    return (float(p1[0]) - float(p2[0])) ** 2 + (float(p1[1]) - float(p2[1])) ** 2

if __name__ == '__main__':
    # s = "1 1,2 2,3 3,4 4,5 5,1.5 1.5"
    l = []
    for _ in range(int(input())):
        # l.append(input().strip().split(" "))
        s = input()
        l = list(map(lambda x: str(x).split(" "), s.split(",")))
        l = sorted(l, key=lambda x: (float(x[0]), float(x[1])))  # 先排序
        n = len(l)
        min_num = -1
        min_list = []
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = l[i], l[j]
                dis = cal_dist(p1, p2)
                if i == 0 and j == 1:
                    min_num = dis
                    add_element(min_list, p1, p2)
                    break
                if dis < min_num:
                    min_num = dis
                    min_list.clear()
                    add_element(min_list, p1, p2)
                elif dis == min_num:
                    add_element(min_list, p1, p2)
                else:
                    continue
        print("".join(min_list)[:-1])