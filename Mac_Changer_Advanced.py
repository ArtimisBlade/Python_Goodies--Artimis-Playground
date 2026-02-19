# Allows access to CLI commands to use in our code
import subprocess
# Allows us to get args from user and parse them.
import optparse
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.parse_args()

interface = input("Please enter the interface you want to use(e.g. wlan0): ")
new_mac = input("Please enter the new MAC address(e.g 10:22:33:44:88): ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# ---Less Secure ---
#subprocess.call("ifconfig" + interface+ " down", shell=True)
#subprocess.call("ifconfig" + interface + " hw ether" + new_mac, shell=True)
#subprocess.call("ifconfig" + interface + " up", shell=True)

# --- More Secure ---
subprocess.call(["ifconfig", interface,  "down"])
subprocess.call(["ifconfig", interface,  "hw", "ether", new_mac,])
subprocess.call(["ifconfig", interface, "up"])
