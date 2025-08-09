import requests

REPO_OWNER = "web-coder-of-rpi"
REPO_NAME = "PyServer-Designer"
CONTRIBUTORS_FILE = "CONTRIBUTORS.md"

def fetch_contributors(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch contributors:", response.status_code)
        return []

def update_contributors_md(contributors):
    with open(CONTRIBUTORS_FILE, "w") as f:
        f.write("<!-- filepath: /workspaces/PyServer-Designer/CONTRIBUTERS.md -->\n")
        f.write("This is a list of all the contributors of this repository.\n")
        f.write("It is updated automatically.\n\n")
        f.write("## Contributors\n")
        for user in contributors:
            f.write(f"- [{user['login']}]({user['html_url']})\n")

if __name__ == "__main__":
    contributors = fetch_contributors(REPO_OWNER, REPO_NAME)
    update_contributors_md(contributors)
