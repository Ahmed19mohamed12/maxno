import requests
from bs4 import BeautifulSoup
import csv
import os
payload = {
    #college data
    "email":"ahmed.mohamed.ahady@gmail.com",
    "password":"Zkr}z:'L~bk3A5@",
    #waleedkassab data
    "email":"ahmed.mohamed.ahady@gmail.com",
    "password":"Zkr}z:'L~bk3A5@",
    "login":"login"
}
current_video = 1
limit = 1000
f = open("colleg2.csv","a")
writer = csv.writer(f)
writer.writerow(["Session Name","Session Url On Site","Session Url On Browser"])
login_url = "https://college-center.net/student/index.php"
video_url = "https://college-center.net/student/showvideo.php?id="
found = 0
with requests.Session() as s:
    p = s.post(
        login_url,
        data = payload
    )
    while(limit>=current_video):
        ps = s.get(video_url+str(current_video))
        soup = BeautifulSoup(ps.text, 'lxml')
        try :
            sessionName = soup.find_all("h2",{"class":"vname"})[0].text
            # print(sessionName + " ==============>>>>>>>>>>>>>> " + str(current_video))
            sessionName2 = soup.find_all("iframe")[0].src
            writer.writerow([sessionName,video_url+str(current_video),sessionName2])
            found = found + 1
            os.system('cls' if os.name == "nt" else 'clear')
            print("found "+str(found))
        except :
            # os.system('cls' if os.name == "nt" else 'clear')
            print("failed " + str(current_video))
            pass
        current_video = current_video + 1
        
