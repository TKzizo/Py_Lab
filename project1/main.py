#!/usr/bin/python3 

import nmap 

scanner = nmap.PortScanner()

print(" Nmap Automation tool:")
print("--------------------------->")

ip_addr = input("Enter targer ip address: ")
print("Entered address is :",ip_addr)

type(ip_addr)

resp = input("""\nEnter the type of scan you want to perform:
		  1)SYN ACK Scan
		  2) UDP Scan
		  3)Comprehensive Scan""")
print("\nyou have selected: ",resp)

if resp == "1":
	print("Nmap version: ",scanner.nmap_version())
	scanner.scan(ip_addr,"1-1024","-v -sS")
	print(scanner.scaninfo())
	print("Ip Status: ",scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print("Opened Ports: ",scanner[ip_addr]["tcp"].keys())	

elif resp == "2":
	print("Nmap version: ",scanner.nmap_version())
        scanner.scan(ip_addr,"1-1024","-v -sU")
        print(scanner.scaninfo())
        print("Ip Status: ",scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Opened Ports: ",scanner[ip_addr]["udp"].keys())

elif resp == "3":
	print("Nmap version: ",scanner.nmap_version())
        scanner.scan(ip_addr,"1-1024","-v -sS -sV sC -A -O")
        print(scanner.scaninfo())
        print("Ip Status: ",scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Opened Ports: ",scanner[ip_addr]["tcp"].keys())
else:
	print("You can select either 1 ,2 ,3")



