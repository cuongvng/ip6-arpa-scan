import subprocess
import pandas as pd
from ip6_arpa_scan import drilldown, reverse_ipv6

DNS_SERVER = "8.8.8.8"
FILES = [
	# "./data/apnic-ipv6-AU.csv",
	# "./data/apnic-ipv6-SG.csv",
	# "./data/apnic-ipv6-IN.csv",
	"./data/apnic-ipv6-JP.csv",
	"./data/apnic-ipv6-KR.csv",
]

def main():
	for file in FILES:
		print(file)

		df = pd.read_csv(file)
		df = df[df["Status"] == "Assigned"]
		df = df[["Range start", "Prefix"]]
		
		with open("result.txt", 'a') as fw:
			fw.write(f'\n{file}\n')
			fw.close()

		for row in df.iterrows():
			addr = row[1]["Range start"]
			subprocess.run(["python", "./ip6_arpa_scan.py", addr, DNS_SERVER])			

if __name__ == '__main__':
	main()