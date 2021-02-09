import requests
from bs4 import BeautifulSoup
import re
import pprint

def get_news(page_number):
    url = f'https://news.ycombinator.com/news?p={page_number}'
    html = site_content(url)
    scrape_html(html)


def site_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        return print('page number is not valid')

def scrape_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    story = soup.select('a.storylink')
    stats = soup.select('td.subtext')
    rankings = soup.select('.rank')

    # Collect articles for display
    daily_news = []
    check_score = re.compile('\d+ point')
    check_link = re.compile('^https.+')
    for article_number in range(len(story)):
        hn_rank = rankings[article_number].text
        hn_rank = int(re.findall(r'^\d+', hn_rank)[0])
        title = story[article_number].text
        link = story[article_number].get('href')
        article_subtext = stats[article_number].text.strip()
        score = int(re.findall(r'^\d+', article_subtext)[0])  # grab score from subtext 

        # Filter articles to show
        if score >= 100 and check_link.match(link) and check_score.match(article_subtext):
            story_info = {
                '1. Article Rank': hn_rank,
                '2. Title': title,
                '3. Link' : link,
                '4. Score': score
            }
            daily_news.append(story_info)
    return pprint.pprint(daily_news)

if __name__ == '__main__':
    pages_viewed = 0
    page = ''
    while page != 'q':
        if pages_viewed > 0:
            page = input("Enter desired page to view next ('q' to quit): ")
        get_news(page)
        pages_viewed += 1