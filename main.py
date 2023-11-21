from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()



    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")


    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()







    screen.exitonclick()




if __name__ == "__main__":
    main()
