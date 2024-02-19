# 8-13. User Profile

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('Alexa', 'Adams',
                             location='San Diego',
                             field='Sofware Engineering',
                             energy='tired')
print(my_profile)