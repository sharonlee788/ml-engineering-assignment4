import os 

USER_NAME = "sharonlee"

def say_hi(msg: str = "Hi!", file_directory: str = "/app/data/") -> None:
    file_name = f"{USER_NAME}_output.txt"
    file_path = os.path.join(file_directory, file_name)

    with open(file_path, "w") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

if __name__ == "__main__":
    say_hi()