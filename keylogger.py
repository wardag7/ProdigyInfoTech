import os

def save_credentials(username, password, file_path):
    # Set the file path to save the credentials
    file_name = f"{username}_credentials.txt"
    file_path = os.path.join(file_path, file_name)

    # Save the credentials to the file
    with open(file_path, "w") as f:
        f.write(f"Username: {username}\n")
        f.write(f"Password: {password}\n")

def main():
    # Get user input for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Set the directory path to save the credentials
    directory_path = r"C:\Users\Wajahat Khan\Desktop\ProdigyInfoTech\keylogger"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Save the credentials
    save_credentials(username, password, directory_path)

if __name__ == "__main__":
    main()
