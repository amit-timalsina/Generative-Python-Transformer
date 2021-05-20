<<<<<<< HEAD
from curtsies.fmtfuncs import cyan, bold
=======
>>>>>>> 9a201987d7a6490e552e7d03d8281330895ef733
from github import Github
import time
from datetime import datetime
import os

ACCESS_TOKEN =  open('token.txt', 'r').read()
g = Github(ACCESS_TOKEN)
print(g.get_user())

<<<<<<< HEAD
end_time = time.time() - 86400 * 2
=======
end_time = time.time()
>>>>>>> 9a201987d7a6490e552e7d03d8281330895ef733
start_time = end_time - 86400


for i in range(1):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
    end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
    query = f"language:Python created:{start_time_str}..{end_time_str}"
    print(query)
    end_time -=86400
    start_time -= 86400
    result = g.search_repositories(query)
    print(result.totalCount)

    for repository in result:
        print(f"{repository.clone_url}")
        print(f"{repository._clone_url}")
        print(f"{repository.tags_url}")
        # print(f"{dir(repository)}")

<<<<<<< HEAD
        os.system(f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}")
        print(cyan(bold(f"current start time {start_time}")))

print("Finished, your new end time must be:", start_time)
=======
        os.system(f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}")
>>>>>>> 9a201987d7a6490e552e7d03d8281330895ef733
