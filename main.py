from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title('my snake game')
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:

    screen.update()
    
    time.sleep(0.05)
    snake.move()

    # If the snake collides with any food object.
    if snake.head.distance(food) < 15:
        # Program creates a new random object in the screen.
        food.refresh()
        # Scoreboard increases in 1.
        scoreboard.increase_score()
        # A new segment will be added
        snake.add_segment()
    
    # If the snake collides with the screen borders, it dies.
    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 325 or snake.head.ycor() < -350:
        # game_on = False
        scoreboard.reset()
        snake.reset()
        screen.update()

    # If the snake collides with its body, the game ends.
    # Everytime the snake moves, this code will check if it is close enough to any of its segments to finish the game. 
    for i in range(1, len(snake.segments)-1):
        if snake.head.distance(snake.segments[i]) < 15:
            scoreboard.reset()
            snake.reset()
            screen.update()
            # game_on = False
    
        
# scoreboard.game_over()
screen.exitonclick()

