#-*-coding:utf-8-*-
import requests
import sched, time

from lxml import html
from Email import Email


asscUrl = "https://shop.antisocialsocialclub.com/"
s = sched.scheduler(time.time, time.sleep)
def newAvailableASSC():
    page = requests.get(asscUrl)
    tree = html.fromstring(page.text)
    gridHeader = tree.xpath('//div[@class="grid-uniform"]')[0]   # Take the start index
    gridGroup = gridHeader.getchildren()
    canBuy = False
    for i in gridGroup:
        if (i.attrib.get("class")):
            classList = (i.attrib.get("class")).split(" ")
            if  not "sold-out" in classList:
                canBuy = True
                print("Found one that you can buy! - ")
        else:
            print("Error class not found in grid item")

    if (canBuy):
        gmail = Email('#your email#', '# your password #')
        gmail.send_email(['#your email#'], 'New ASSC item now available!', 'https://shop.antisocialsocialclub.com/')
    else:
        s.enter(600, 1, newAvailableASSC, ())

#run every 10 min
s.enter(600, 1, newAvailableASSC, ())
s.run()
