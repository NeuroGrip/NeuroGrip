import tkinter as tk
from PIL import Image, ImageTk
import sys

if len(sys.argv) > 1:
    image_path = sys.argv[1]
else:
    # Load the image
    image_path = "image.png"  # Change to your image file path

image = Image.open(image_path)
img_width, img_height = image.size

# Create the main window
root = tk.Tk()
root.title("Image Click Position")

# Convert the image for Tkinter
tk_image = ImageTk.PhotoImage(image)

# Create a canvas to display the image
canvas = tk.Canvas(root, width=img_width, height=img_height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Label to show coordinates
coord_label = tk.Label(root, text="Click on the image", font=("Arial", 14))
coord_label.pack()

# Function to handle mouse clicks
def on_click(event):
    # Clear previous dots
    canvas.delete("dot")
    
    # Get click coordinates
    x, y = event.x, event.y
    
    # Draw a red dot at the clicked position
    canvas.create_oval(x-6, y-6, x+6, y+6, fill="red", tags="dot")
    
    # Update label with coordinates
    coord_label.config(text=f"Clicked at: ({x}, {y})")

    # Return x and y coordinates
    return x, y

# Function to return (x,y) coordinates for pick up
def pick_up(event, center_point_1, center_point_2, center_point_3, pos_1, pos_2, pos_3):
    # Get top left (x,y) coordinates for box
    x1, y1 = on_click(event)
    
    # Get top right (x,y) coordinates for box
    x2, y2 = on_click(event)
    
    # Get bottom left (x,y) coordinates for box
    x3, y3 = on_click(event)
    
    # Get bottom right (x,y) coordinates for box
    x4, y4 = on_click(event)

    #
    
    

# Bind mouse click event to the canvas
canvas.bind("<Button-1>", on_click)

# Run the application
root.mainloop()
