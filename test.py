import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

plt.style.use('fivethirtyeight')

hdr = {'User-Agent': 'Mozilla/5.0'}
site = 'https://www.opensecrets.org/industries./recips.php?ind=E01++'
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
donation_amount = []
donation_recipient = []
for strg in soup.find_all('td', class_='number'):
    donation_amount.append(strg.string)

for td in soup.find_all('td'):
    for a in td.find_all('a'):
        str = a.string
        name = str.replace(',', '').split(' ')
        donation_recipient.append(name[1] + ' ' + name[0])
# print(donation_amount)
# print(donation_recipient)

donations_num = []
for amount in donation_amount:
    donations_num.append(int(amount.replace('$', '').replace(',','')))

list_tuples = list(zip(donation_recipient, donation_amount, donations_num))
df = pd.DataFrame(list_tuples, columns=['Recipient','Amount (str)', 'Amount'])

fig1, ax1 = plt.subplots(figsize=(50,15))
fig1.suptitle('Amount of donations from oil and gas', size=30)
ax1.bar(df['Recipient'], df['Amount'],color='darkseagreen')
plt.savefig('donations.png')
plt.show()