from collections import Counter
from dateutil.parser import parse
import requests, json

url = "https://api.github.com/users/brendasalenave/repos"
repos = json.loads(requests.get(url).text)

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

#print(dates)
#print(month_counts)
#print(weekday_counts)

last_5_repositories = sorted(repos, key=lambda r: r["created_at"], reverse=True)[:5]
#print(last_5_repositories)

last_5_languages = [repo["language"] for repo in last_5_repositories]
print(last_5_languages)
