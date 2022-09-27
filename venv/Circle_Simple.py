import matplotlib.pyplot as plt
import math
plt.title("Simple Draw Circle")

def draw8(xc, yc, x, y):
    plt.plot(xc + x, yc + y, 'go', label='marker only')
    plt.plot(xc - x, yc + y, 'go', label='marker only')
    plt.plot(xc + x, yc - y, 'go', label='marker only')
    plt.plot(xc - x, yc - y, 'go', label='marker only')
    plt.plot(xc + y, yc + x, 'go', label='marker only')
    plt.plot(xc - y, yc + x, 'go', label='marker only')
    plt.plot(xc + y, yc - x, 'go', label='marker only')
    plt.plot(xc - y, yc - x, 'go', label='marker only')

def simpleDrawCircle(xc, yc, r):
    x = 0
    y = r
    while x <= y:
        x += 1
        y = round(math.sqrt(pow(r, 2) - pow(x, 2)))
        draw8(xc, yc, x, y)

    plt.show()

if __name__ == "__main__":
    xc = int(input("Enter x: "))
    yc= int(input("Enter y: "))
    r = int(input("Enter radius: "))

    simpleDrawCircle(xc, yc, r)
