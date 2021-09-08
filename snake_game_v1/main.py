from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

# Set up game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Game")
screen.tracer(0) # Turn off "tracing" (afterImages) of drawings after movement

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Map keys with certain snake actions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start game
game_on = True
while game_on:
    screen.update() # Refresh screen pixels
    time.sleep(0.1) # Wait 
    snake.move() # Move snake
    #game_on = False

    # Dectect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.addPoint()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.gameOver()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.gameOver()

# Terminate game on mouse click
screen.exitonclick()