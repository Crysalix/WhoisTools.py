#!/usr/bin/env python3

import ip2whois

import config as cfg

ip2whois_init = ip2whois.Api(cfg.apikey)

# Lookup domain information
results = ip2whois_init.lookup('timestamp.ovh')
print(results)
