from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.body = self.segments[1]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        # Justa as a note: Below lines 31 and 32 were replaced by line 33 because it was
        # creating a bug when the new segment was appended. 
        #last_segment_x = self.segments[-1].xcor()
        #last_segment_y = self.segments[-1].xcor()
        # Below code seems to be more faster and the snake extention now looks better.
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
        new_segment.showturtle()
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        

    # Below code was usefull only before implementing the reset Method. I will save it just in case.
    
    # def up(self):
    #     # If the x coordinate of the head is more on the right side than the second segment, the head of the turtle will turn to the LEFT.
    #     if self.head.xcor() > self.body.xcor():
    #         self.head.left(90)
    #     # # If the x coordinate of the head is more on the right side than the second segment, the head of the turtle will turn to the RIGHT.
    #     elif self.head.xcor() < self.body.xcor():
    #         self.head.right(90)
    #     else:
    #         pass

    # def down(self):
    #     # If the x coordinate of the head is more on the right side than the second segment, the head of the turtle will turn to the LEFT.
    #     if self.head.xcor() < self.body.xcor():
    #         self.head.left(90)
    #     # # If the x coordinate of the head is more on the right side than the second segment, the head of the turtle will turn to the RIGHT.
    #     elif self.head.xcor() > self.body.xcor():
    #         self.head.right(90)
    #     else:
    #         pass

    # def left(self):
    #     # If the y coordinate of the head is more on the top than the body, the head of the turtle will turn to the LEFT.
    #     if self.head.ycor() > self.body.ycor():
    #         self.head.left(90)
    #     # # If the y coordinate of the head is below the body, the head of the turtle will turn to the RIGHT.
    #     elif self.head.ycor() < self.body.ycor():
    #         self.head.right(90)
    #     else:
    #         pass

    # def right(self):
    #     # If the y coordinate of the head is over the body, the head of the turtle will turn to the RIGHT.
    #     if self.head.ycor() > self.body.ycor():
    #         self.head.right(90)
    #     # # If the y coordinate of the head is below the body, the head of the turtle will turn to the LEFT.
    #     elif self.head.ycor() < self.body.ycor():
    #         self.head.left(90)
    #     else:
    #         pass
