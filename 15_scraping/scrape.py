import requests
from bs4 import BeautifulSoup
import pprint

res1 = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup1.select('.storylink')
links2 = soup2.select('.storylink')
subtext1 = soup1.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext1 + subtext2


def sort_stories_by_votes(hnList):
    return sorted(hnList, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):

        title = links[index].getText()
        href = links[index].get('href', None)
        vote = mega_subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
