#!/usr/bin/env python3

import sys
import ip2whois

import config as cfg

try:
    arg1 = sys.argv[1]
except IndexError:
    sys.exit('Usage : {} <domain.tld>'.format(sys.argv[0]))

ip2whois_init = ip2whois.Api(cfg.apikey)

# Lookup domain information
results = ip2whois_init.lookup(arg1)
print(results)
