from operator import itemgetter

import requests


class HackerNewsAPI:
    """Handles API calls to Hacker News."""

    def __init__(self, url):
        """Initialize attributes."""

        self.url = url


    def _api_call(self):

        self.r = requests.get(self.url)
        self.status_code = self.r.status_code

        self.r = self.r.json()

        return self.r


    def _collect_submission_info(self):
        """Process information about each submission."""

        self.submission_dicts = []

        for sub_id in self.submission_ids[:5]:
            # Make a new API call for each submission.
            self.url = f"https://hacker-news.firebaseio.com/v0/item/{sub_id}.json"

            response_dict = self._api_call()
            sub_dict = self._make_dictionary(response_dict, sub_id)

            self.submission_dicts.append(sub_dict)


    def _make_dictionary(self, dict, id):

        submission_dict = {
            'title': dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={id}",
            'comments': dict['descendants'],
        }

        return submission_dict
    

    def process_api_call(self):
        """Collect initial API call, plus all info for returned data."""

        self.submission_ids = self._api_call()
        
        self._collect_submission_info()
