import subprocess
from datetime import datetime

def update_file():
    with open("log.txt", "a") as file:
        file.write(f"Updated on {datetime.now()}\n")

def git_commit_push():
    try:
        subprocess.run(["git", "add", "log.txt"], check=True)
        subprocess.run(["git", "commit", "-m", "Automated daily update"], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")

if __name__ == "__main__":
    update_file()
    git_commit_push()
