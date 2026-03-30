from PIL import Image

img = Image.open("Q1.png").convert("RGB")
pixels = img.load()

for y in range(img.height):
    for x in range(img.width):
        r, g, b = pixels[x, y]
        
        if (r, g, b) == (255, 255, 255):
            pixels[x, y] = (0, 0, 0)
        elif (r, g, b) == (0, 0, 0):
            pixels[x, y] = (255, 255, 255)

img.save("Q1I.png")
