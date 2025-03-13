import subprocess

def git_push(commit_message, branch="main"):
    try:
        # Pull the latest changes from the remote repository
        subprocess.run(["git", "pull", "origin", branch], check=True)

        # Add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit with a custom message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to the specified branch
        subprocess.run(["git", "push", "origin", branch], check=True)

        print("✅ Changes successfully pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")

# Ask the user for a commit message and run the function
commit_msg = input("Enter commit message: ")
git_push(commit_msg)
