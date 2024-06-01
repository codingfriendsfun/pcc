from git_api_repos import RepoAPI
import pytest


@pytest.fixture
def new_api_call():
    """Instance of RepoAPI"""

    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    new_api_call = RepoAPI(url)

    return new_api_call


def test_status_code(new_api_call):
    """Test that the status code is 200"""

    assert new_api_call.status_code == 200


def test_dictionary_conversion(new_api_call):
    """Test that the response is correctly converted to a dictionary."""

    is_dict = type(new_api_call.r)

    assert is_dict == dict


def test_total_repositories(new_api_call):
    """Test the correct number of total repositories are found."""

    repos = new_api_call.r['total_count']

    assert repos >= 200


def test_collected_repository_numbers(new_api_call):
    """Test the correct number of repos are returned."""

    num_of_dicts = len(new_api_call.repo_dicts)

    assert num_of_dicts >= 30



