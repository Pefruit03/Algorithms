import matplotlib.pyplot as plt
plt.title("Circle MidPoint")

def draw8(xc, yc, x, y):
    plt.plot(xc + x, yc + y, 'go', label='marker only')
    plt.plot(xc - x, yc + y, 'go', label='marker only')
    plt.plot(xc + x, yc - y, 'go', label='marker only')
    plt.plot(xc - x, yc - y, 'go', label='marker only')
    plt.plot(xc + y, yc + x, 'go', label='marker only')
    plt.plot(xc - y, yc + x, 'go', label='marker only')
    plt.plot(xc + y, yc - x, 'go', label='marker only')
    plt.plot(xc - y, yc - x, 'go', label='marker only')

def circleMidPoint(xc, yc, r):
    x = 0
    y = r
    p = 5 / 4 - r
    while x < y:
        if p < 0:
            p = p + (2 * x + 3)
        else:
            p = p + (2 * (x - y) + 5)
            y -= 1
        x += 1
        draw8(xc, yc, x, y)

    plt.show()

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    rad = int(input("Enter radius: "))

    circleMidPoint(x, y, rad)

if __name__ == "__main__":
    main()