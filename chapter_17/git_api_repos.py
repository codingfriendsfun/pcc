import requests

class RepoAPI:
    """Handle Git API calls."""

    def __init__(self, url):
        """Initialize attributes."""
        self.url = url
        
        self.repo_dicts = self._collect_dicts()


    def _api_call(self):
        """Make an API call and check the response."""

        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        self.r = requests.get(self.url, headers=self.headers)
        
        # Status Code
        self.status_code = self.r.status_code
        print(f"Status code: {self.status_code}")
        
        return self.r


    def _response_dict(self):
        """Convert the response to a dictionary."""

        self.r = self.r.json()
        return self.r
    

    def _collect_dicts(self):
        """Store all dictionaries."""
        
        self._api_call()
        self._response_dict()

        return self.r['items']


    def process_results(self):
        """Process results."""

        # API results
        print(f"Total Repositories: {self.r['total_count']}")
        print(f"Complete results: {not self.r['incomplete_results']}")

        # Collect Dictionaries
        print(f"Repositories returned: {len(self.repo_dicts)}")

        # Summarize the top repositories.
        print("\nSelected information about each repository:")

        for repo_dict in self.repo_dicts:
            print(f"\nName: {repo_dict['name']}")
            print(f"Owner: {repo_dict['owner']['login']}")
            print(f"Stars: {repo_dict['stargazers_count']}")
            print(f"Repository: {repo_dict['html_url']}")
            print(f"Description: {repo_dict['description']}")
