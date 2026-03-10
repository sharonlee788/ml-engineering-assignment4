import os 

USER_NAME = "sharonlee"

def build_filename(user_name: str) -> str:
    return f"{user_name}_output.txt"

def say_hi(msg: str = "Hi!", file_directory: str = "/app/data/") -> None:
    file_name = build_filename(USER_NAME)
    file_path = os.path.join(file_directory, file_name)

    with open(file_path, "w") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

if __name__ == "__main__":
    say_hi()