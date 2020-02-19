import unittest
import requests
from retrive_repo import get_commits, get_repo, get_api, get_output


class TestGithub_Repo_list(unittest.TestCase):

    def test_get_Github_API(self):
        userID = 'cdp2323'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):
            self.assertEqual(get_api('cdp2323'), response)
            self.assertEqual(get_api('users'), None)
        else:
            self.assertEqual(get_api('cdp2323'), None)

    def test_get_repo_list(self):
        userID = 'cdp2323'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        print(response)
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):
            list1 = get_repo(response)
            self.assertEqual(get_repo(response), list1)

    def test_get_repo_commits_number(self):
        userID = 'cdp2323'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):
            list1 = get_repo(response)
            list2 = get_commits(userID, list1)
            self.assertEqual(get_commits(userID, list1), list2)

    def test_get_output_list(self):
        userID = 'cdp2323'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):
            list1 = get_repo(response)
            list2 = get_commits(userID, list1)
            list3 = get_output(list1, list2)
            self.assertAlmostEqual(get_output(list1, list2), list3)


if __name__ == "__main__":
    unittest.main()