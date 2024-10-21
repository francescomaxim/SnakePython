from tkinter import *
import random

WIDTH = 700
HEIGHT = 600
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#FF0000"
FOOD_COLOR = "#00FF00"
BACKGROUND_COLOR = "#FFFFFF"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int(WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

def nextTurn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global  score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if checkGameStatus(snake):
        isGameOver()
    else:
        window.after(SPEED, nextTurn, snake, food)

def changeDirection(newDirection):
    global direction

    if newDirection == "up":
        if direction != "up":
            direction = newDirection
    elif newDirection == "down":
        if direction != "down":
            direction = newDirection
    elif newDirection == "left":
        if direction != "left":
            direction = newDirection
    elif newDirection == "right":
        if direction != "right":
            direction = newDirection


def checkGameStatus(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x > WIDTH:
        return True
    elif y < 0 or y > HEIGHT:
        return True

    for bodyPart in snake.coordinates[1:]:
        if x == bodyPart[0] and y == bodyPart[1]:
            return True

    return False

def isGameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="GAME OVER", fill=SNAKE_COLOR, tags="gameOver")

window = Tk()
window.title("Snake")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=("consolas", 40), fg=SNAKE_COLOR, bg=BACKGROUND_COLOR)
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR ,width=WIDTH, height=HEIGHT)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
a = int((screen_width / 2) - (window_width / 2))
b = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{a}+{b}")

window.bind('<Left>', lambda event: changeDirection('left'))
window.bind('<Right>', lambda event: changeDirection('right'))
window.bind('<Up>', lambda event: changeDirection('up'))
window.bind('<Down>', lambda event: changeDirection('down'))

snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()