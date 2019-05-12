import json
import datetime
import collections
import functools

data = []

def load(fn):
  with open(fn, 'r') as f:
    j = json.load(f)
  for c in j['data']['children']:
    if not c['data']['pinned']:
      data.append(c['data'])

load('python1.json')
load('machinelearning1.json')
load('datascience1.json')
load('opensource1.json')
load('java1.json')
load('startups1.json')


def hour(ts):
  return int(ts.hour/2)*2


def day(ts):
  return ts.weekday()

# 60-80 seems optimal
def title(d):
  t = len(d['title'])
  return '0-40' if t < 40 else ('40-60' if t < 60 else ('60-80' if t<80 else '80-100'))


# 1000+ seems best
def text(d):
  t = len(d['selftext'])
  return '1: 0' if t == 0 else ('2: 1-350' if t < 350 else ('3: 350-600' if t<600 else ('4: 600-1000' if t<1000 else '5: 1000-10000')))



buckets = {}
for d in data:
  ts = datetime.datetime.utcfromtimestamp(int(d['created']))
  b = text(d)
  if b not in buckets:
    buckets[b] = []
  buckets[b].append(int(d['score']))

buckets = collections.OrderedDict(sorted(buckets.items()))
for k, v in buckets.items():
  s = functools.reduce(lambda x, y: x + y, map(lambda x: 1 if x > 100 else 0, v))
  print(k, len(v), s/len(v))


