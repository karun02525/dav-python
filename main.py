# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json


def print_hi(name):
    req = requests.get('https://api.postalpincode.in/pincode/821108')
    res = req.json()
    for item in res:
        print(item['Message'])
        print(item['Status'])
        for i in item['PostOffice']:
            print(i['Name'] + " " + i['Block'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
