import matplotlib.pyplot as plt


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
point1 = [-1, 2]
point2 = [3, 4]
x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]
plt.plot(x_values, y_values, 'bo', linestyle="-")
plt.text(point1[0]-0.015, point1[1]+0.25, "Point1")
plt.text(point2[0]-0.050, point2[1]-0.25, "Point2")
plt.savefig('image.jpg')
