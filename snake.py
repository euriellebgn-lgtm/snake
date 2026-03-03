import tkinter as tk
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "blue"
BACKGROUND_COLOR = "black"

def run_game():
    game = tk.Tk()
    game.title("Snake")
    game.focus_set()

    score = 0
    direction = "down"

    label = tk.Label(game, text=f"Score: {score}", font=("Helvetica", 20))
    label.pack()

    canvas = tk.Canvas(game, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
    canvas.pack()

    class Snake:
        def __init__(self):
            self.coordinates = []
            self.squares = []
            for i in range(BODY_PARTS):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(
                    x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                    fill=SNAKE_COLOR, tag="snake"
                )
                self.squares.append(square)

    class Food:
        def __init__(self):
            x = random.randrange(0, GAME_WIDTH, SPACE_SIZE)
            y = random.randrange(0, GAME_HEIGHT, SPACE_SIZE)
            self.coordinates = [x, y]
            canvas.create_oval(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=FOOD_COLOR, tag="food"
            )

    def next_turn():
        nonlocal score, food, snake, direction

        x, y = snake.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, [x, y])
        square = canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=SNAKE_COLOR
        )
        snake.squares.insert(0, square)

        if [x, y] == food.coordinates:
            score += 1
            label.config(text=f"Score: {score}")
            canvas.delete("food")
            food = Food()
        else:
            canvas.delete(snake.squares[-1])
            snake.squares.pop()
            snake.coordinates.pop()

        if check_collisions():
            game_over()
        else:
            game.after(SPEED, next_turn)

    def change_direction(new):
        nonlocal direction
        opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if new != opposites.get(direction):
            direction = new

    def check_collisions():
        x, y = snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True

        for part in snake.coordinates[1:]:
            if part == [x, y]:
                return True

        return False

    def game_over():
        canvas.delete("all")
        canvas.create_text(
            GAME_WIDTH / 2,
            GAME_HEIGHT / 2,
            text="GAME OVER",
            fill="red",
            font=("Helvetica", 50, "bold")
        )

    def restart():
        nonlocal score, snake, food, direction
        canvas.delete("all")
        score = 0
        direction = "down"
        label.config(text=f"Score: {score}")
        snake = Snake()
        food = Food()
        next_turn()

    game.bind("<Left>", lambda e: change_direction("left"))
    game.bind("<Right>", lambda e: change_direction("right"))
    game.bind("<Up>", lambda e: change_direction("up"))
    game.bind("<Down>", lambda e: change_direction("down"))

    tk.Button(game, text="Restart", command=restart).pack(pady=5)

    snake = Snake()
    food = Food()
    next_turn()

    game.mainloop()


run_game()