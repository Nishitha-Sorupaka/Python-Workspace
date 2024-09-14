import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# Rectangle class to store the properties of each rectangle
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = None
        self.y = None
        self.rotated = False

    def rotate(self):
        self.width, self.height = self.height, self.width
        self.rotated = not self.rotated


# Recursive function to place rectangles
def place_rectangles(space_width, space_height, rectangles, x=0, y=0):
    if not rectangles:
        return True  # All rectangles placed

    rect = rectangles[0]  # Get the first rectangle
    rest = rectangles[1:]  # Remaining rectangles

    # Try placing the rectangle without rotation
    if rect.width <= space_width and rect.height <= space_height:
        rect.x, rect.y = x, y
        if place_rectangles(space_width - rect.width - 1, space_height, rest, x + rect.width + 1, y):
            return True

    # Try placing the rectangle with rotation
    rect.rotate()
    if rect.width <= space_width and rect.height <= space_height:
        rect.x, rect.y = x, y
        if place_rectangles(space_width - rect.width - 1, space_height, rest, x + rect.width + 1, y):
            return True

    # If we cannot place the rectangle, return False to backtrack
    return False


# Visualize the rectangles using Matplotlib
def visualize_rectangles(rectangles):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    for rect in rectangles:
        ax.add_patch(Rectangle((rect.x, rect.y), rect.width, rect.height, edgecolor='blue', facecolor='lightgrey'))
        ax.text(rect.x + rect.width / 2, rect.y + rect.height / 2, f'{rect.width}x{rect.height}',
                ha='center', va='center', fontsize=10)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# Main function
def main():
    # Generate 5 rectangles with random width and height
    rectangles = [Rect(random.randint(5, 30), random.randint(5, 30)) for _ in range(5)]

    # Try to place the rectangles in a 100x100 space
    if place_rectangles(100, 100, rectangles):
        print("Rectangles placed successfully!")
        visualize_rectangles(rectangles)
    else:
        print("Failed to place all rectangles.")


if __name__ == "__main__":
    main()
