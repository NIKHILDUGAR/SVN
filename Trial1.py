from __future__ import print_function
from platform import python_version
from sys import exit
from time import sleep
from os import path
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror
RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'
def check_EVIL(url):

    '''
    Check evil chars in URL
    :param url: suspicious URL
    :return: result of check and the evil chars
    '''

    bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
    result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]

    if result:
        msg = '\n{0}[*] Evil URL detected: {1}{2}{3}{1}'.format(YELLOW,END,RED,url)
        msg += '\n{0}[*] Evil characters used: {1}{2}{3}{1}'.format(YELLOW,END,RED,result)
    else:
        msg = '\n{0}[*] Evil URL NOT detected:{1} {2}{3}{1}'.format(YELLOW, END, GREEN, url)

    return msg
def checkURL():
    print ('\n{0}[{1}*{0}]{1} CheckURL module loaded.'.format(GREEN, END))
    print ('\nOperation modes: \n\n{0}[{1}1{0}]{1} Check single URL\n{0}[{1}2{0}]{1} Check from a list'.format(RED, END))
    if input('\n>{0}>{1}> '.format(RED, END)) == '1':
        url = input('{0}>{1} Insert an url: '.format(RED, END))
        print ('\n * Do you want to check connection? (y/n)')
        if input('\n>{0}>{1}> '.format(RED, END)).upper() == 'Y':
            print (check_EVIL(url))
def Runner():
    print ('\nSelect an option: \n\n{0}[{1}1{0}]{1} Generate evil urls\n{0}[{1}2{0}]{1} Detect evil urls'.format(RED, END))
    opt = input('\n>{0}>{1}> '.format(RED, END))
    if opt == '1':
        main()
    elif opt == '2':
        checkURL()
    else:
        print ('{0}[{1}!{0}]{1} Invalid Option.\nReturning to main in few seconds...'.format(RED, END))
        sleep(2)
        Runner()
if __name__ == '__main__':
    try:
        Runner()
    except KeyboardInterrupt:
        exit()