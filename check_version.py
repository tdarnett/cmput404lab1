#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get("http://www.google.com")
print response.status_code
print response.text
