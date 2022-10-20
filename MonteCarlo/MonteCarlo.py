import turtle
import random
import matplotlib.pyplot as plt
import math

# myPen = turtle.Turtle()
# myPen.hideturtle()
# myPen.speed(0)
#
# myPen.up()
# myPen.setposition(-100, -100)
# myPen.down()
# myPen.fd(200)
# myPen.left(90)
# myPen.fd(200)
#
# myPen.left(90)
# myPen.fd(200)
# myPen.left(90)
# myPen.fd(200)
# myPen.left(90)
#
#
# myPen.up()
# myPen.setposition(0, -100)
# myPen.down()
# myPen.circle(100)

in_circle = 0
out_circle = 0
pi_value = []

for i in range(5):
    for j in range(1000):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)
        if x**2 + y**2 > 100**2:

            out_circle = out_circle + 1
        else:

            in_circle = in_circle + 1
        pi = 4.0 * in_circle/(in_circle + out_circle)
        pi_value.append(pi)
        avg_pi_errors = [abs(math.pi - pi)/math.pi*100 for pi in pi_value]
    print(pi_value[-1])
plt.figure(figsize=(5,3.5))
plt.axhline(math.pi, color='g',linestyle='-')
plt.plot(pi_value)
plt.xlabel("Samples")
plt.ylabel("Values of PI")
plt.grid("auto")
plt.tight_layout()
plt.savefig("pi.png")
# plt.show()

plt.figure(figsize=(5,3.5))
plt.axhline(0, color ='g', linestyle='-')
plt.plot(avg_pi_errors)
plt.xlabel("Samples")
plt.ylabel("Error [%]")
plt.grid("auto")
plt.tight_layout()
plt.savefig("error.png")
plt.show()