"""
author: danping cai
"""
import requests

def get_api(userID):
    result = requests.get("https://api.github.com/users/{}/repos".format(userID))
    result = result.json()
    if 'message' in result:

        if result["message"].startswith("API rate limit exceeded"):
            print("API rate limit exceeded")
            return None

        if result["message"].startswith("Not Found"):
            print("Not Found")
            return None

    return result

def get_repo(github_api_result):
    repo_list = [repo['name'] for repo in github_api_result]
    return repo_list


def get_commits(userID, list_repo):
    list_commits = []
    for repo in list_repo:
        number = requests.get("https://api.github.com/repos/{}/{}/commits".format(userID, repo))
        number = len((number.json()))
        list_commits.append(number)
    return list_commits


def get_output(list_repo, list_repo_commits_number):
    list_output = ["Repo: {} Number of commits: {}".format(name, commits) for name, commits in
                   zip(list_repo, list_repo_commits_number)]
    return list_output


if __name__ == "__main__":
    userID = input("enter an user ID: ")
    response = get_api(userID)
    if response:
        list_repo = get_repo(response)
        list_repo_commits_number = get_commits(userID, list_repo)
        list_output = get_output(list_repo, list_repo_commits_number)
        print(list_output)