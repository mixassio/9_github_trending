import requests, json
from datetime import datetime, date, time, timedelta

def get_trending_repositories(top_size=20):
    date_today = datetime.date(datetime.now())
    date_before_week = date_today - timedelta(days=7)
    date_search = str(date_before_week) + '..' + str(date_today)
    url = 'https://api.github.com/search/repositories?q=created:' + date_search + '&sort=stars'
    params = {'page': 1, 'per_page': top_size}
    repositories = requests.get(url, params)
    repos = repositories.json()
    for rep in repos["items"]:
        print('--------------------------------------------------')
        print('Name: {}, count stars: {}, count open isues: {}'.format(rep['name'], rep['stargazers_count'], rep['open_issues']))
        if rep['open_issues'] > 0:
            print('Open issues:')
            get_open_issues_amount(rep['owner'], rep['name'])
        else:
            print('NO open issues')




def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/' + repo_owner['login'] + '/' + repo_name +'/issues'
    params = {'page': 1, 'per_page': 20}
    list_issusies = requests.get(url, params)
    issues = list_issusies.json()
    for issu in issues:
        print('----',issu['html_url'])


if __name__ == '__main__':
    get_trending_repositories()
