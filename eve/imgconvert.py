import base64

with open("image.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

with open("encoded_image.txt", "w") as txt_file:
    txt_file.write(encoded_string)