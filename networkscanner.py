import scapy.all as scapy

#Destination
target ="192.168.31.1/24"

#Create ARP packet

packet =scapy.ARP(pdst=target)

ether = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

#stack 

newpacket = ether/packet

answer=scapy.srp(newpacket,timeout=3)[0]
#print(answer.show())


for i in answer:
    print(i[1].psrc)
    print(i[1].hwsrc)
    print("..............................................")








