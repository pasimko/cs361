import time
import random

def generate_random_number():
    while True:
        # Open to read command
        with open("prng-service.txt", "r") as f:
            command = f.read().strip()
            if command == "run":
                random_number = random.randint(1, 1000)  # Adjust the range as needed
                # Open to write number
                with open("prng-service.txt", "w") as output_file:
                    output_file.write(str(random_number))
            else:
                # Sleep to avoid continuous checking when there's no command
                time.sleep(0.5)

if __name__ == "__main__":
    generate_random_number()
