import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while (x1, y1) != (x2, y2):
        points.append((x1, y1))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    points.append((x2, y2))
    return points

x1 = int(input("Masukkan koordinat x1 (titik awal): "))
y1 = int(input("Masukkan koordinat y1 (titik awal): "))
x2 = int(input("Masukkan koordinat x2 (titik akhir): "))
y2 = int(input("Masukkan koordinat y2 (titik akhir): "))

points = bresenham(x1, y1, x2, y2)

for point in points:
    plt.plot(point[0], point[1], 'bo')

plt.grid(True)
plt.show()
