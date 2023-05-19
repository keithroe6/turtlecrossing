from turtle import Turtle
STARTING_POSITION = (0, -280)   # tuple unchangeable data type
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
class Player(Turtle):
    """Creating the player class. You can add in move_forward, reset_turtle, crossed_finish"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.right(270)
        self.goto(0, -280)
    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def move_backward(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())


    
    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())


    def reset_turtle(self):
        self.goto(STARTING_POSITION)
    def crossed_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False