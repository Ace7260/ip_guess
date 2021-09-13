def which_class_ip(ipAddress):
    if(ipAddress[0]>=0 and ipAddress[0]<=127):
        return "Class A"
    elif (ipAddress[0]>=128 and ipAddress[0]<=191):
        return "Class B"
    elif(ipAddress[0]>=192 and ipAddress[0]<=223):
        return "Class C"
    elif(ipAddress[0]>=224 and ipAddress[0]<=239):
        return "Class D"
    else:
        return "Class E"
#la piraterie n'est jamais finie 
ipAddress=str(input("Ip Address :"))
ipAddress=ipAddress.split(".")
ipAddress=[int(i) for i in ipAddress]
print(which_class_ip(ipAddress))

from ipaddress import ip_address
def public_private_ip(fucking_ip):
    if (ip_address(fucking_ip).is_private):
        return "Private Ip"
    else:
        return "Plublic Ip"
print(public_private_ip(str(input("Ip to verify :"))))