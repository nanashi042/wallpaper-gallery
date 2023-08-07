import requests

def get_image():
    image_url = "https://images.hdqwalls.com/wallpapers/tokyo-ghoul-anime-4k-o1.jpg"
    image_filename = "./static/img/image.jpg"

    response = requests.get(image_url)

    if response.status_code == 200:
        with open(image_filename, "wb") as f:
            f.write(response.content)
        print("Image downloaded and saved as", image_filename)
    else:
        print("Failed to download image")

get_image()