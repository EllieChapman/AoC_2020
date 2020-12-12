f = open('day12_input.txt', 'r')
input=f.readlines()

x = 0
y = 0

xdiff = 10
ydiff = 1


def move(direction, distance):
    global xdiff
    global ydiff
    if direction == "N":
        ydiff = ydiff + int(distance)
    elif direction == "E":
        xdiff = xdiff + int(distance)
    elif direction == "S":
        ydiff = ydiff - int(distance)
    else:
        xdiff = xdiff - int(distance)

def turn(angle):
    global x
    global xdiff
    global y
    global ydiff

    if angle == 180:
        xdiff = -xdiff
        ydiff = -ydiff
    elif angle == 90:
        temp = xdiff
        xdiff = ydiff
        ydiff = -temp
    elif angle == 270:
        temp = xdiff
        xdiff = -ydiff
        ydiff = temp


for i in input:
    if i[0] == "F":
        x = x + ( int(i[1:]) * xdiff )
        y = y + ( int(i[1:]) * ydiff )
    elif i[0] == "R":
        turn(int(i[1:]))
    elif i[0] == "L":
        turn(360 - int(i[1:]))
    else:
        move(i[0], i[1:])

print(x, y)
print(abs(x)+abs(y))
