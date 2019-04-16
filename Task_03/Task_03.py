from Line import Line

def Check(i,j,k):
    s = 0
    a = i.a
    b = i.b
    c = j.a
    d = j.b
    e = k.a
    f = k.b
    #print(a,b,c,d,e,f)
    if (a<c and b<c) and (a<e and b<e):
        if (c<e and d<e)or(e<c and f<c):
            s = b-a + d-c + f-e
    elif (c<a and d<a) and (c<e and d<e):
        if (a<e and b<e)or(e<a and f<a):
            s = b-a + d-c + f-e
    elif (e<a and f<a) and (e<c and f<c):
        if (a<c and b<c)or(c<a and d<a):
            s = b-a + d-c + f-e
    return s

def func(objects = list()):
    summ = []
    for i in objects:
        for j in objects:
                for k in objects:
                    if (i!=j)and(j!=k)and(i!=k):
                        q = Check(i,j,k)
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
            print("a =",x.a,"b = ", x.b)
    print(func(mass))

main()