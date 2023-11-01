from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.title('My snake game')
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_scoreboard()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        score.resets()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.resets()



screen.exitonclick()