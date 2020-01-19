import requests
from bs4 import BeautifulSoup
import ctypes

g_NASA_POTD_URL = "https://apod.nasa.gov/"
g_PIC_DIR = "C:\\Users\\steph\\Pictures\\NASA_potd\\"

def setWallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

def getImage():
    url = requests.get(g_NASA_POTD_URL)
    soup = BeautifulSoup(url.content, "html.parser")
    print(url)

    date = soup.findAll("p")[1].text.strip()
    print(date)

    image_url = soup.find("img")['src']
    print(image_url)

    image = requests.get(image_url)

    with open("{g_PIC_DIR}{date}.jpg") as f:
        f.write()

    setWallpaper("{g_PIC_DIR}{date}.jpg")


getImage()