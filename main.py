import tinify
import glob
tinify.key = 'enter your api key here'
all_images = glob.glob("*.jpg")
for image in all_images:
    file_name = str(image)
    name = file_name.split(".")
    with open(image, 'rb') as source:
        image_to_resize = tinify.from_file(source)
        resized_image = image_to_resize.resize(method="fit", width=250, height=250)
        resized_image.to_file(name[0]+'-compressed-resized.jpg')
    print(name[0]+".jpg resized.")
