import turtle
import time

ROD_WIDTH = 16
ROD_HEIGHT = 100

FIRST_DISK_WIDTH = 32
DISK_HEIGHT = 16

SLEEP_TIME = 0.5

colors = [
    'red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'purple'
]

towers = [
    [6, 5, 4, 3, 2, 1],
    [],
    []
]


def draw_disk(rod_index, disk_size, disk_index):
    turtle.fillcolor(colors[disk_size - 1 % len(colors)])
    turtle.seth(0)
    turtle.up()
    turtle.goto(turtle.screensize()[0] / 3 * (rod_index - 1), DISK_HEIGHT * disk_index)
    turtle.down()
    turtle.begin_fill()
    disk_width = FIRST_DISK_WIDTH * (1 + 0.5 * (disk_size - 1))
    turtle.left(180)
    turtle.forward(disk_width / 2)
    turtle.right(90)
    turtle.forward(DISK_HEIGHT)
    turtle.right(90)
    turtle.forward(disk_width)
    turtle.right(90)
    turtle.forward(DISK_HEIGHT)
    turtle.right(90)
    turtle.forward(disk_width / 2)
    turtle.end_fill()
    pass


def draw_rods():
    turtle.fillcolor('black')
    for i in [-1, 0, 1]:
        turtle.seth(0)
        turtle.up()
        turtle.goto(turtle.screensize()[0] / 3 * i, 0)
        turtle.down()
        turtle.begin_fill()
        turtle.left(180)
        turtle.forward(ROD_WIDTH / 2)
        turtle.right(90)
        turtle.forward(ROD_HEIGHT)
        turtle.right(90)
        turtle.forward(ROD_WIDTH)
        turtle.right(90)
        turtle.forward(ROD_HEIGHT)
        turtle.right(90)
        turtle.forward(ROD_WIDTH / 2)
        turtle.end_fill()
    pass


def draw_towers():
    turtle.reset()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0)
    draw_rods()
    for tower_number in range(len(towers)):
        for disk_position in range(len(towers[tower_number])):
            draw_disk(tower_number, towers[tower_number][disk_position], disk_position)
    turtle.update()
    time.sleep(SLEEP_TIME)
    pass


def move_tower(from_rod_index, to_rod_index, lower_disk_depth):
    if lower_disk_depth == 1:
        towers[to_rod_index].append(towers[from_rod_index].pop())
        draw_towers()
    else:
        rods_indices = [0, 1, 2]
        rods_indices.remove(from_rod_index)
        rods_indices.remove(to_rod_index)
        free_rod_index = rods_indices[0]

        move_tower(from_rod_index, free_rod_index, lower_disk_depth - 1)
        towers[to_rod_index].append(towers[from_rod_index].pop())
        draw_towers()
        move_tower(free_rod_index, to_rod_index, lower_disk_depth - 1)
    pass

turtle.screensize(600, 300)
turtle.setup(800, 500)

draw_towers()
turtle.update()

move_tower(0, 2, len(towers[0]))

turtle.done()