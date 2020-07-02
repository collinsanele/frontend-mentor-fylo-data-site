from PIL import Image

img =  Image.open("bg-mobile.png")

img.save("bg-mobile.jpg", "PNG")

print("Done")