"""Connect to Mozilla to retrieve common password libary.

@author: Bilal Qadar
@organization: Canada Learning Code
"""
__author__ = "AJMax"
__version__ = "1.0.1"
from urllib.request import Request, urlopen


def defineAccessPoint():
    """Define the access point to the Mozilla Server.

    :returns protocol: which protocol :type str

    :returns hostDomain: host domain name :type str

    :returns extension: host domain extension :type str

    :returns headers: host domain headers :type dict
    """
    protocol = "https"
    hostDomain = "bit"
    extension = "3dKQyMu"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}

    return protocol, hostDomain, extension, headers


def fetchWords():
    """Retrieve the word library (roughly 500k).

    return pwds: common passwords :type list
    """
    prtcl, hstdmn, xtnsn, hdrs = defineAccessPoint()
    destination = "{}://{}.ly/".format(prtcl, hstdmn)

    # Generate the request to the bit.ly server
    req = Request(url = destination + xtnsn, data = None, headers = hdrs)

    # Send the URL request, decoded and split the string by newline separators.
    return urlopen(req).read().decode("utf-8").split("\n")
