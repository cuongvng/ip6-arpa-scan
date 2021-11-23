import subprocess
from sys import prefix
import pandas as pd
from ip6_arpa_scan import drilldown, reverse_ipv6
from glob import glob

DNS_SERVER = "8.8.8.8"
COUNTRIES = glob("./data/*.csv")

def main():
	for c in COUNTRIES[:5]:
		print(c)

		df = pd.read_csv(c)
		df = df[df["Status"] == "Assigned"]
		df = df[["Range start", "Prefix"]]
		
		with open("result.txt", 'a') as fw:
			fw.write(f'\n{c}\n')
			fw.close()

		for row in df.iterrows():
			addr = row[1]["Range start"]
			prefix = str(row[1]["Prefix"])
			subprocess.run(["python", "./ip6_arpa_scan.py", addr, DNS_SERVER, prefix])			

if __name__ == '__main__':
	main()