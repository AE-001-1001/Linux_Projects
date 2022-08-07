import subprocess
import numpy as np
cmd = ["curl www.google.com","nmap -A -dd -open -packet-trace -D 4  www.robinhood.com","sudo nmap -sS -dd -A  104.56.234.160","sudo nmap --script vuln 127.0.0.1 -Pn -sS -dd  -r -p1-65535","sudo nmap --script vuln 0.0.0.0 -Pn -sV -dd  -r","sudo nmap --script -A vulns 0.0.0.0 "]
array = np.array([cmd[0],cmd[1],cmd[2],cmd[3],cmd[4],cmd[5]])
def testing_networks():
	for exe in cmd:
		ex1 = subprocess.Popen(exe,shell=True)
		ex1.wait()
		if ex1.returncode == 0:
			print("\2\7 Success!")

'''
End of Testing networks
'''

newarr = array.reshape(2,3,1)
for i in array:
	subprocess.Popen(i, shell=True)
	
