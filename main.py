import pywhatkit
import pandas as pd

list = [123456, 2343242423, 2134124234, 2423423141234, 2412453264, 235, 2352352]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read = open('C:/Users/waseem/Desktop/message.txt')
    message = read.read()
    i = 0
    while i <= len(list):
        pywhatkit.sendwhatmsg_instantly("+" + str(list[i]), message, wait_time=15, tab_close=True, close_time=2)
        i = i + 1
