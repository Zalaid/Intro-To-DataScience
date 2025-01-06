import os
import random
from datetime import datetime, timedelta

# Function to generate a random date within the previous month
def get_random_date_in_last_month():
    today = datetime.now()
    first_day_of_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
    last_day_of_last_month = today.replace(day=1) - timedelta(days=1)
    random_date = first_day_of_last_month + timedelta(
        days=random.randint(0, (last_day_of_last_month - first_day_of_last_month).days)
    )
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

# Number of commits to make on each random day (between 3 and 7)
commits_per_day_range = (3, 7)

# Your GitHub email
github_email = "zalaidbutt1@gmail.com"  # Replace with your GitHub email

# Create a set of random commit dates for the previous month
commit_dates = [get_random_date_in_last_month() for _ in range(random.randint(1, 6))]

for commit_date in commit_dates:
    # Determine how many commits to make on this date (between 3 and 7)
    num_commits = random.randint(commits_per_day_range[0], commits_per_day_range[1])

    for _ in range(num_commits):
        # Write something random in the file for each commit
        with open("commit_file.txt", "a") as file:
            file.write(f"Commit made on {commit_date}\n")
        
        # Stage the file
        os.system("git add commit_file.txt")
        
        # Set the GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environment variables
        os.environ["GIT_AUTHOR_DATE"] = commit_date
        os.environ["GIT_COMMITTER_DATE"] = commit_date
        os.environ["GIT_AUTHOR_EMAIL"] = github_email  # Set author email
        os.environ["GIT_COMMITTER_EMAIL"] = github_email  # Set committer email
        
        # Make the commit
        os.system(f'git commit -m "Commit made on {commit_date}"')

print("Commits completed for previous month.")
