import matplotlib.pyplot as plt
plt.title("Circle Bresenham")

def draw8(xc, yc, x, y):
    plt.plot(xc + x, yc + y, 'go', label='marker only')
    plt.plot(xc - x, yc + y, 'go', label='marker only')
    plt.plot(xc + x, yc - y, 'go', label='marker only')
    plt.plot(xc - x, yc - y, 'go', label='marker only')
    plt.plot(xc + y, yc + x, 'go', label='marker only')
    plt.plot(xc - y, yc + x, 'go', label='marker only')
    plt.plot(xc + y, yc - x, 'go', label='marker only')
    plt.plot(xc - y, yc - x, 'go', label='marker only')

def circleBresen(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r
    #print('x: %s, y: %s' % (xc, yc))
    while x <= y:
        if p > 0:
            y -= 1
            p = p + (4 * (x - y) + 10)
        else:
            p = p + (4 * x + 6)
        draw8(xc, yc, x, y)
        x += 1
    plt.show()

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    rad = int(input("Enter radius: "))

    circleBresen(x, y, rad)

if __name__ == "__main__":
    main()
