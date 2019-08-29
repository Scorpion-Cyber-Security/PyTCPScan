#!/usr/bin/python
# -*- coding: utf-8 -*-

 
# PyTCPScan Version 1.0 (beta)

import socket

def baner():
	print " "
	print "██████╗ ██╗   ██╗████████╗ ██████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗"
	print "██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║"
	print "██████╔╝ ╚████╔╝    ██║   ██║     ██████╔╝███████╗██║     ███████║██╔██╗ ██║"
	print "██╔═══╝   ╚██╔╝     ██║   ██║     ██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║"
	print "██║        ██║      ██║   ╚██████╗██║     ███████║╚██████╗██║  ██║██║ ╚████║"
	print "╚═╝        ╚═╝      ╚═╝    ╚═════╝╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝"
	print "                                                                            "



baner()

target_host = raw_input("Enter target host: ")
target_port = int(input("Enter target port: "))

print "Start scan"

#criando um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectando o cliente
client.connect((target_host, target_port))

#enviando alguns dados
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recebendo alguns dados
response = client.recv(4096)

print response
