import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original 
# draw_polygon(num_sides, size, orientation, location, color, border_size)



class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self, x_offset, y_offset):
        self.location[0] += x_offset
        self.location[1] += y_offset


class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.reduction_ratio = reduction_ratio

    def draw(self):
        current_size = self.size
        current_location = self.location[:]

        while current_size > 10:
            super().draw()  # Draw
            
            # Adjust the size
            current_size *= self.reduction_ratio
            
            # Recalculate the new location
            turtle.penup()
            turtle.goto(current_location[0], current_location[1])
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.right(90)
            
            # Update the location and size for the next smaller polygon
            current_location = [turtle.pos()[0], turtle.pos()[1]]
            self.size = current_size
            self.location = current_location


class PolygonArt:
    def __init__(self, num_polygons, num_sides, embedded=False, all_random=False):
        self.num_polygons = num_polygons
        self.num_sides = num_sides
        self.embedded = embedded
        self.all_random = all_random

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def run(self):
        for _ in range(self.num_polygons):
            if self.num_sides == 0 or self.all_random:
                num_sides = random.randint(3, 5) # All Shapes
            else:
                num_sides = self.num_sides
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            reduction_ratio = 0.618

            if self.all_random:
                self.embedded = random.choice([True, False])

            if self.embedded:
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, reduction_ratio)
                polygon.draw()
            else:
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw()              

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# Create and run PolygonArt with a desired number of polygons
user_input = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

NUM_POLYGONS = 15

if user_input == 1:
    art = PolygonArt(NUM_POLYGONS, 3)
    art.run()
elif user_input == 2:
    art = PolygonArt(NUM_POLYGONS, 4)
    art.run()
elif user_input == 3:
    art = PolygonArt(NUM_POLYGONS, 5)
    art.run()
elif user_input == 4:
    art = PolygonArt(NUM_POLYGONS, 0)
    art.run()
elif user_input == 5:
    art = PolygonArt(NUM_POLYGONS, 3, True)
    art.run()
elif user_input == 6:
    art = PolygonArt(NUM_POLYGONS, 4, True)
    art.run()
elif user_input == 7:
    art = PolygonArt(NUM_POLYGONS, 5, True)
    art.run()
elif user_input == 8:
    art = PolygonArt(NUM_POLYGONS, 0, True)
    art.run()
elif user_input == 9:
    art = PolygonArt(NUM_POLYGONS, 4, True, True)
    art.run()


# hold the window; close it by clicking the window close 'x' mark
turtle.done()