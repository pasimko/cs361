import time
from PIL import Image

def image_to_ascii(filename, terminal_width=80):
    try:
        # Load the image
        image = Image.open(filename)

        # Define the ASCII characters to use for different intensity levels
        ASCII_CHARS = "@%#*+=-:. "

        # Resize the image to fit the terminal width while preserving the aspect ratio
        aspect_ratio = image.height / image.width
        new_width = terminal_width
        new_height = int(terminal_width * aspect_ratio * 0.55)
        resized_image = image.resize((new_width, new_height))

        # Convert the image to grayscale
        grayscale_image = resized_image.convert("L")

        # Convert each pixel to an ASCII character based on intensity
        ascii_image = ""
        for pixel_value in grayscale_image.getdata():
            ascii_image += ASCII_CHARS[pixel_value // 25]

        # Split the ASCII image into lines to match the terminal height
        lines = [ascii_image[i:i + terminal_width] for i in range(0, len(ascii_image), terminal_width)]

        # Return the ASCII art as a string
        return "\n".join(lines)

    except Exception as e:
        return str(e)

def main():
    while True:
        print("Press Enter to generate and display a random image:")
        input()
        
        # Prompt and then wait for PRNG Service
        with open("prng-service.txt", "w") as f:
            f.write("run")
        time.sleep(0.5)

        # Read the output of PRNG service
        with open("prng-service.txt", "r") as f:
            random_number = int(f.read().strip())
        
        # Prompt and then wait for image service
        with open("image-service.txt", "w") as f:
            f.write(str(random_number))
        time.sleep(0.5)
        
        # Read the image path from image-service.txt
        with open("image-service.txt", "r") as f:
            image_path = f.read().strip()
        
        ascii_art = image_to_ascii(image_path)
        print(ascii_art)

        # Clear files
        with open("prng-service.txt", "w") as f:
            f.write("")
        with open("image-service.txt", "w") as f:
            f.write("")

if __name__ == "__main__":
    main()
