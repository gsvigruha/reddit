import json
import urllib.request
import datetime
import time


subreddits=['datascience', 'machinelearning', 'datasets', 'java', 'python', 'opensource', 'startups', 'business', 'entrepreneur']
td = datetime.date.today()
success = 0

for sr in subreddits:
  print(f'Loading {sr}.')
  js = None
  for _ in range(0, 10):
    try:
      with urllib.request.urlopen(f'https://www.reddit.com/r/{sr}/new.json?limit=100') as response:
        js = response.read()
        print(f'Got {sr}.')
        break
    except Exception as e:
      print(f'Error: {e}')
      time.sleep(10)
  time.sleep(15)

  if js is not None:
    with open(f'{td}_{sr}.json', 'wb') as f:
      f.write(js)
      success = success + 1

print(f'Got {success} out of {len(subreddits)}')
