from dns import message, query, exception
import sys

queries = 0
l = []
progress = [0]*30

def tryquery(q, server):
	while 1:
		try:
			return query.udp(q, server, timeout=2)
		except exception.Timeout:
			pass

def drilldown(base, server, limit, depth=0):
	global queries, l, progress

	q = message.make_query(base, 'PTR')
	r = tryquery(q, server)
	queries = queries + 1

	if r.rcode() == 0:
		if len(base) == limit:
			l.append(base)
		if len(base) < limit:
			for c in '0123456789abcdef':
				if depth < len(progress):
					progress[depth]=int(c, 16)
				print ("progress[%s]=%s" % (depth, progress[depth]))
				drilldown(c+'.'+base, server, limit, depth+1)
				
	print('\r%*s, %s queries done, %s found' % (int(limit), base, queries, len(l)))
		
if __name__ == "__main__":
	(base, server) = sys.argv[1:3]
	if len(sys.argv) == 4:
		limit = int(sys.argv[3])//4*2+len('ip6.arpa.')
	else:
		limit = 32*2+len('ip6.arpa.')

	print ('base %s server %s limit %s' % (base, server, limit))

	if base.endswith('ip6.arpa'):
		base = base + '.'

	if not base.endswith('ip6.arpa.'):
		print ('please pass an ip6.arpa name')
		sys.exit(1)

	try:
		drilldown(base, server, limit)
	except KeyboardInterrupt:
		print('\naborted, partial results follow')