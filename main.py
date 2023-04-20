import requests
from requests.auth import HTTPBasicAuth

# URL to Search all issues.
url = "https://txxxxxxpython.atlassian.net/rest/api/2/search"

# Create an authentication object,using
# registered emailID, and, token received.
auth = HTTPBasicAuth("admin@foreachtoil.com",
                     "asdasdasd")

# The Header parameter, should mention, the
# desired format of data.
headers = {
    "Accept": "application/json"
}
query = {
    'jql': 'project =MedicineAppBugs '
}

TICKETS = [
    {
        'category': 'whitelabel',
        'title': 'Deploy Whitelabel release on Production',
        'description': '''Deploy release on Production environments:
        '''
    }, {
        'category': 'whitelabel',
        'title': 'Deploy Whitelabel release on Non-Production',
        'description': '''Deploy release on Non-Production environments: 
        '''
    }, {
        'id': 'helmdev',
        'category': 'helm',
        'title': 'Update Helm Releases & deploy to DEV',
        'description': '''Update the Helm Releases version for DEV environments'''
    }, {
        'id': 'helmnonprod',
        'category': 'helm',
        'title': 'Update Helm Releases & deploy to INT',
        'description': '''Update the Helm Releases versions for Non-Production Environments (except Dev)''',
        'relationships': [
            {
                'type': 'blockedby',
                'target': 'helmdev'
            }
        ]
    }, {
        'id': 'helmprod',
        'category': 'helm',
        'title': 'Update Helm Releases & deploy to PROD',
        'description': '''Update the Helm Releases versions for Production Environments''',
        'relationships': [
            {
                'type': 'blockedby',
                'target': 'helmnonprod'
            }
        ]
    }
]


def get_current_release():
    """
    Get current Whitelabel Gitlab Release
    :return:
    """
    return "11.2.9"


def create_jira_ticket(title: str, description: str, relationships=None, **kwargs):
    if not relationships:
        relationships = []
    print(f'Creating ticket with Title: {title}')
    print(f'Creating ticket with Description: {description}')
    for relationship in relationships:
        print(relationship)
    print('kwargs')
    print(kwargs)


def main():
    for ticket in TICKETS:
        create_jira_ticket(**ticket)


if __name__ == '__main__':
    main()
