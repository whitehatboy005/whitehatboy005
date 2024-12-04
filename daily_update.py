import subprocess
from datetime import datetime

def update_file():
    with open("log.txt", "a") as file:
        file.write(f"Updated on {datetime.now()}\n")

def git_commit_push():
    try:
    # Open the file in append mode
    with open("README.md", "a") as f:
        f.write("\nThis is the daily update!")
    print("Update written successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_file()
    git_commit_push()
