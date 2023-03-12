import backend.imageConverter as ic

# Time to be creative! Make your own "bitmap" images using your own color palette

# You can now use a custom 3-bit colour depth.
# Got to https://www.color-hex.com/ to find the hexadecimal codes for the colors you want.
colours = {
    0: "#ffffff", 1: "#ff0000", 2: "#0000ff", 3: "#00ff00",
    4: "#000000", 5: "#000000", 6: "#000000", 7: "#000000"
}

# Edit this 2D list either directly or use nested for lists to make the image on the board
pixels = [
    [1, 0, 5],
    [0, 2, 0],
    [5, 0, 3]
]

# Do not edit beyond this line
if __name__ == '__main__':
    ic.displayImage(pixels, ic.hexToCol(colours))

