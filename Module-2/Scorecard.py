import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

divs = soup.find_all("div", class_="ds-p-4")

scorecards=[]
for div in divs:
  links = div.find_all('a', href=lambda href: href and 'scorecard' in href)
  for link in links:
    scorecards.append(link.get('href'))

scorecards = ['https://www.espncricinfo.com/' + s for s in scorecards]
print(scorecards)
