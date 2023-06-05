import turtle as tmodule
from tkinter import Tk, Button, OptionMenu, StringVar, filedialog
import random
import color_chooser

def create_art():
    picasso.clear()
    picasso.penup()
    dot_count = int(dot_var.get())

    # Starting position set
    if dot_count == 100:
        picasso.setpos(-220, -230)
    elif dot_count == 225:
        picasso.setpos(-350, -350)
    elif dot_count == 400:
        picasso.setpos(-470, -4700)

    # Adjust canvas size based on dot count
    canvas_width = 600
    canvas_height = 600

    if dot_count == 100:
        canvas_width = 800
        canvas_height = 800
    elif dot_count == 225:
        canvas_width = 1200
        canvas_height = 1200
    elif dot_count == 400:
        canvas_width = 1500
        canvas_height = 1500
    screen.setup(canvas_width, canvas_height)

    tmodule.colormode(255)  # Set the color mode to 255

    for i in range(dot_count):
        color = random.choice(color_list)
        r, g, b = color  # Extract RGB values from the tuple
        picasso.dot(30, (r, g, b))  # Pass the RGB tuple directly to picasso.dot()

        if dot_count == 100:
            picasso.forward(50)
            if (i + 1) % 10 == 0:
                picasso.setheading(90)
                picasso.forward(50)
                picasso.setheading(180)
                picasso.forward(550)
                picasso.setheading(0)
                picasso.forward(50)  # Additional forward step for the next row

        elif dot_count == 225:
            picasso.forward(50)
            if (i + 1) % 15 == 0:
                picasso.setheading(90)
                picasso.forward(50)
                picasso.setheading(180)
                picasso.forward(800)
                picasso.setheading(0)
                picasso.forward(50)  # Additional forward step for the next row

        elif dot_count == 400:
            picasso.forward(50)
            if (i + 1) % 20 == 0:
                picasso.setheading(90)
                picasso.forward(50)
                picasso.setheading(180)
                picasso.forward(1050)
                picasso.setheading(0)
                picasso.forward(50)  # Additional forward step for the next row


def choose_image():
    # Open file dialog to select an image file
    filepath = filedialog.askopenfilename(filetypes=[("jpg files", "*.jpg"), ("jpge files", "*.jpeg")])

    # Process the selected image path
    if filepath:
        # Process the image file
        # Replace this line with your own implementation
        print("Selected image:", filepath)


def quit_app():
    window.destroy()


# Create the Tkinter window
window = Tk()
window.title("Dot Art Maker")

# Create the turtle canvas
screen = tmodule.Screen()
screen.setup(600, 600)  # Set the initial canvas size
picasso = tmodule.RawTurtle(screen)
picasso.speed("fastest")
picasso.hideturtle()

# Define the color list and dot count options
color_list = color_chooser.palette
dot_options = ["100", "225", "400"]

# Create a button to create art
create_button = Button(window, text="Create Art", command=create_art)
create_button.pack()

# Create a button to choose an image
choose_button = Button(window, text="Choose Image", command=choose_image)
choose_button.pack()

dot_var = StringVar(window)
dot_var.set(dot_options[0])  # Set the default dot count
dot_menu = OptionMenu(window, dot_var, *dot_options)
dot_menu.pack()

quit_button = Button(window, text="Quit", command=quit_app)
quit_button.pack()

# Run the Tkinter event loop
window.mainloop()
