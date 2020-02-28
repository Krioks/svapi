import vk
import os
import requests
import time
import traceback
import ctypes
import webbrowser as wb
import random
import json
import codecs
from urllib.parse import parse_qs



def GetAcsessToken(app_id):
    if os.listdir().count('access_token.dat'):
        r = open('acsess_token.dat')
        acsess_token = r.read()
        r.close()
        kernel32 = ctypes.windll.kernel32
        attr = kernel32.GetFileAttributesW('acsess_token.dat')
        kernel32.SetFileAttributesW('access_token.dat', attr | 2)

    else:
        auth_url = ("https://oauth.vk.com/authorize?client_id={app_id}&display=page&redirect_uri="
                    "https://oauth.vk.com/blank.html&scope="
                    "friends,photos,audio,video,docs,"
                    "notes,wall,groups, offline"
                    "&response_type=token&v=5.92&state=42".format(app_id=app_id))
        wb.open_new_tab(auth_url)
        redirected_url = input("Paste here url you were redirected:\n")
        aup = parse_qs(redirected_url)
        aup['access_token'] = aup.pop('https://oauth.vk.com/blank.html#access_token')
        s = open('acsess_token.dat', 'w')
        s.write(aup['acsess_token'][0])
        s.close()
        kernel32 = ctypes.windll.kernel32
        attr = kernel32.GetFileAttributesW('acsess_token.dat')
        kernel32.SetFileAttributesW('access_token.dat', attr | 2)
        acsess_token = aup['acsess_token'][0]
    return acsess_token


def main():
	app_id = 6231475
	access_token = GetAcsessToken(app_id)
	session = vk.Session(access_token=access_token)
	api = vk.API(session, v='5.85', lang='ru', timeout=120)


main()
