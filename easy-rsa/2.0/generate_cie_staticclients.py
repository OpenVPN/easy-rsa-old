import os

#directory used by openvpn server for static ip assignment
directory = "./staticclients"
if not os.path.exists(directory):
    os.mkdir(directory)

# The ip address and subnet for the client will be of the form
# 6.0.0.3 6.0.0.4. So, we have to skip by 2 to generate the ip
# by 2.
start = 3

count = 1000 #number of cie. For now 1000 is more than enough

for index in range(1,count + 1):
    if start%256 != 255:
        with open("%s/cie%d" %(directory, index), "w") as text_file:
            text_file.write("ifconfig-push 6.0.%d.%d 6.0.%d.%d\n" %(start//256, start%256, start//256, (start+1)%256))
    start += 2
