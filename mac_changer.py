
import subprocess
import optparse
import random
parse = optparse.OptionParser()
parse.add_option("-i" ,"--interface" , dest="INTERFACE",help="please enter the interface")
parse.add_option("-m" ,"--mac_add" , dest="mac_add",help="please enter the mac")
parse.parse_args()
 
a = random.randint(00,99)
interface = input("interface >")
print("automatically generate the mac address")
print("mac address change user defined interface ")

subprocess.call(["ifconfig" + interface + "down"],shell=True)
subprocess.call(["ifconfig" + interface +"hw ether" +a+":"+a+":"+a+":"+a+":"+a] ,shell=True)
subprocess.call(["ifconfig " + interface + "up"],shell=True)
print("Sucessfully change the mac address")
