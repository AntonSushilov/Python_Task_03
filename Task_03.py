from Line import Line


def check(i, j, k):
    line1 = [p for p in range(i.a, i.b+1)]
    line2 = [p for p in range(j.a, j.b+1)]
    line3 = [p for p in range(k.a, k.b+1)]
    return len(set(line1) & set(line2) & set(line3))


def func(objects=list()):
    summ = []
    for i in objects:
        for j in objects:
            for k in objects:
                if (i != j) and (j != k) and (i != k):
                    q = check(i, j, k)
                    summ.append(q)
    return max(summ)


def main():
    mass = list()
    with open("input.txt", "r") as file:
        for s in file.readlines():
            m = s.split()
            x = Line(int(m[0]), int(m[1]))
            mass.append(x)

        print("Objects:")
        for x in mass:
            print("a =", x.a, "b = ", x.b)
    print(func(mass))


if __name__ == '__main__':
    main()
