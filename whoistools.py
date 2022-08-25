#!/usr/bin/env python3

import ip2whois

ip2whois_init = ip2whois.Api('THISISNOTMYAPIKEYLOL')

# Lookup domain information
results = ip2whois_init.lookup('timestamp.ovh')
print(results)
