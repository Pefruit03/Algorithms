import matplotlib.pyplot as plt
plt.title("Bresenham")

def bresenham(x1, y1, x2, y2):
    if x1 > x2:
        tamp = x1
        x1 = x2
        x2 = tamp
        tamp = y1
        y1 = y2
        y2 = tamp

    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx
    c1 = 2 * dy
    c2 = 2 * (dy - dx)
    x = x1
    y = y1
    xcoor = [x1]
    ycoor = [y1]
    while x < x2:
        if p < 0:
            y = y
            p = p + c1
        else:
            y = y + 1
            p = p + c2
        x = x + 1
        xcoor.append(x)
        ycoor.append(y)

    plt.plot(xcoor, ycoor)
    plt.show()


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    bresenham(x1, y1, x2, y2)


if __name__ == "__main__":
    main()
