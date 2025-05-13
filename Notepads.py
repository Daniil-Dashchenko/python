import os
import random
import cmath
import subprocess
import sys
import webbrowser
from urllib.parse import urlparse, urlunparse



def notepads(count):
    for _ in range(count):
        subprocess.Popen(['notepad.exe'])   


def Explorer(count):
    for _ in range(count):
        subprocess.Popen(["explorer.exe"])

def cmd(count):
    for _ in range(count):
        subprocess.Popen(["cmd.exe"])
       
if __name__ == "__main__":
    a = 15
    b = 15
    c = 15
    
    notepads(a) 
    Explorer(b)   
    cmd(c)    
    url1 = "https://youtu.be/yrReOczjUIQ?si=YdemOpIPW1SXw5I0"
    webbrowser.open(url1)
    url2 = "https://youtu.be/yrReOczjUIQ?si=YdemOpIPW1SXw5I0"
    webbrowser.open(url2)
    url3 = "https://youtu.be/yrReOczjUIQ?si=YdemOpIPW1SXw5I0"
    webbrowser.open(url3)
