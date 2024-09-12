"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None, 'tap_count': 0}  # Añadimos 'tap_count' para contar los taps
hide = [True] * 64
game_over = False


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    if game_over:
        return # Si el juego termino, ignorar taps"""


    spot = index(x, y)
    mark = state['mark']

     # Incrementar contador de taps
    state['tap_count'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Mostrar el número de taps en la esquina superior izquierda
    up()
    goto(-180, 180)
    color('blue')
    write(f'Taps: {state["tap_count"]}', font=('Arial', 20, 'normal'))

    # Verificar si el juego ha terminado (todas las fichas reveladas)
    if all(not hidden for hidden in hide):
        global game_over
        game_over = True
        up()
        goto(0, 0)
        color('black')
        write("¡Juego terminado!", align="center", font=('Arial', 30, 'bold'))

    update()
    if not game_over:
        ontimer(draw, 100) # Solo continuar el temporizador si no se ha terminado el juego


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
