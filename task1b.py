import backend.imageConverter as ic

# Please play with the 2D list, pixels, provided to recreate the pattern on the board

# We are using a 2-bit colour depth
# White = 0, Red = 1, Blue = 2, Green = 3

# Edit this 2D list either directly or use nested for lists to make the image on the board
pixels = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
]

# Do not edit beyond this line
if __name__ == '__main__':
    ic.displayImage(pixels, ic.COLOURS)

