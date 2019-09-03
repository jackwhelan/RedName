import requests
from tqdm import tqdm

url = "https://www.reddit.com/api/username_available.json?user="
available = []
unavailable = []

namesFile = open('names.txt', 'r')
names = namesFile.read().splitlines()
namesFile.close()

for name in tqdm(names):
    link = url + name
    req = requests.get(link, headers = {'User-agent': 'It Ya Boi'})
    if req.json() == True:
        available.append(name)
    elif req.json() == False:
        unavailable.append(name)

with open('available.txt', 'w') as f:
    for item in tqdm(available):
        f.write("%s\n" % item)

with open('unavailable.txt', 'w') as f:
    for item in tqdm(unavailable):
        f.write("%s\n" % item)
