import matplotlib.pyplot as plt
plt.title("DDA")

def Round(a):
    return int(a + 0.5)

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)
    x_inc = dx / step
    y_inc = dy / step
    x = x1
    y = y1
    k = 1
    xcoor = [x]
    ycoor = [y]
    print('x: %s, y: %s' % (x, y))
    while k <= step:
        x1 += x_inc
        y1 += y_inc
        print('x: %s, y: %s' % (Round(x1), Round(y1)))
        xcoor.append(Round(x1))
        ycoor.append(Round(y1))
        k += 1

    plt.plot(xcoor, ycoor)
    plt.show()

def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    DDA(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
