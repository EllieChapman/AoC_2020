f = open('day12_input.txt', 'r')
input=f.readlines()

x = 0
y = 0

facing = "E"

direct = {
    "N" : 0,
    "E" : 90,
    "S" : 180,
    "W" : 270
}

def move(direction, distance):
    global x
    global y
    if direction == "N":
        y = y + int(distance)
    elif direction == "E":
        x = x + int(distance)
    elif direction == "S":
        y = y - int(distance)
    else:
        x = x - int(distance)

def turn(dircetion, angle):
    global facing
    current_angle = direct[facing]
    new_angle = (current_angle + angle)%360
    for key in direct:
        if direct[key] == new_angle:
            facing = key
            break


for i in input:
    if i[0] == "F":
        move(facing, i[1:])
    elif i[0] == "R":
        turn(i[0], int(i[1:]))
    elif i[0] == "L":
        turn(i[0], (360 - int(i[1:])))
    else:
        move(i[0], i[1:])

print(x, y)
print(abs(x)+abs(y))
