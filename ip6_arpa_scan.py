import re
from dns import message, query, exception
import sys

queries = 0
l = []
MAX_FOUND = 1

def reverse_ipv6(ip):
    hex4_blocks = ip.split(':')
    hex4_blocks = list(filter(lambda i: i!='', hex4_blocks))

    for i, h in enumerate(hex4_blocks):
        if len(h) < 4:
            hex4_blocks[i] = '0'*(4-len(h)) + h

    reverse = list(''.join(hex4_blocks))[::-1]
    result = '.'.join(reverse) + ".ip6.arpa."
    result = result.lower()

    return result

def tryquery(q, server):
	try:
		return query.udp(q, server, timeout=3)
	except exception.Timeout:
		return None

def drilldown(base, server, limit, depth=0):
	assert base.endswith('ip6.arpa.')
	global queries, l

	if len(l) >= MAX_FOUND:
		return True

	q = message.make_query(base, 'PTR')
	r = tryquery(q, server)

	if r is None:
		return False

	queries = queries + 1

	if r.rcode() == 0: # NOERROR, this means longer addresses exist, keep drilling down!
		if len(base) == limit:
			l.append(base)
		if len(base) < limit:
			for c in '0123456789abcdef': 
				drilldown(c+'.'+base, server, limit, depth+1)
				
	print('\r%*s, %s queries done, %s found' % (int(limit), base, queries, len(l)))
		
if __name__ == "__main__":
	(base, server) = sys.argv[1:3]
	if len(sys.argv) == 4:
		prefix = int(sys.argv[3])
		limit = int(128-prefix)//4*2+len('ip6.arpa.')
	else:
		limit = 32*2+len('ip6.arpa.')

	arpa = reverse_ipv6(base)

	print ('base %s arpa %s server %s limit %s' % (base, arpa, server, limit))

	drilldown(arpa, server, limit)

	if len(l) == MAX_FOUND:
		print("Active IPv6 found!")
		with open("result.txt", 'a') as fw:
			fw.writelines(f"{base} ---- {arpa}\n")
			fw.close()