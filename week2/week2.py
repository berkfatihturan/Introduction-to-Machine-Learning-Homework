import matplotlib.pyplot as plt
import numpy as np

# Derste gösterilen butun graplar fonksionlar olarak eklenmiştir.

# Graph
def graph():
    x = np.arange(0, 10, 0.1)

    y = np.sin(x)

    plt.plot(x, y)

    plt.title("Sinüs Grafiği")
    plt.xlabel("X Ekseni")
    plt.ylabel("Y Ekseni")

    plt.show()

# point chart
def point_chart():
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = np.random.randint(50, 150, 50)

    plt.scatter(x, y, c=colors, s=sizes)

    plt.title("Point Chart")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.show()

# histogram
def histogram():
    data = np.random.randn(1000)

    plt.hist(data, bins=30)

    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")

    plt.show()

# Column Chart
def column_chart():
    x = ['A', 'B', 'C', 'D', 'E']
    y = np.random.randint(1, 10, 5)

    plt.bar(x, y)

    plt.title("Column Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")

    plt.show()

# Pie Chart
def pie_chart():
    sizes = [30, 25, 15, 10, 5, 5]

    plt.pie(sizes)
    plt.title("Pie Chart")

    plt.show()

# 3D Graph
def graph_3d():
    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(r)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z)

    ax.set_title("3D Graphics")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")

    plt.show()

if __name__ == '__main__':
    graph()
    point_chart()
    histogram()
    column_chart()
    pie_chart()
    graph_3d()