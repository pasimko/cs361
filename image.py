import time

image_set = [
    "image1.jpg",
    "image3.jpg",
    "image4.jpg",
    "image6.jpg",
]

def get_image_path(index):
    index = index % len(image_set)
    return image_set[index]

def listen_for_requests():
    while True:
        with open("image-service.txt", "r") as f:
            request = f.read().strip()
            if request.isdigit():
                image_path = get_image_path(int(request))
                with open("image-service.txt", "w") as output_file:
                    output_file.write(image_path)
            else:
                time.sleep(0.5)  # Sleep for a while before processing the next request

if __name__ == "__main__":
    listen_for_requests()
