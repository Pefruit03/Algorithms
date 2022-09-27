import matplotlib.pyplot as plt
plt.title("MidPoint")

def midPoint(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    x = x1
    y = y1
    xcoor = [x]
    ycoor = [y]
    print('x: %s, y: %s' % (x, y))
    while x < x2:
        if d <= 0:
            d = d + incrE
            x = x + 1
        else:
            d = d + incrNE
            x = x + 1
            y = y + 1
        print('x: %s, y: %s' % (x, y))
        xcoor.append(x)
        ycoor.append(y)

    plt.plot(xcoor, ycoor)
    plt.show()

def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    midPoint(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
