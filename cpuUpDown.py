# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl 
# or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import requests
from oci.config import from_file
from oci.signer import Signer
import json
import sys, getopt

def main(argv):
     global tvm, cpu 
     tvm = ''
     cpu = ''
     try:
          opts, args = getopt.getopt(argv,"hv:c:")
     except getopt.GetoptError:
          print('cpuUpDown.py -v <x or y or z> -c <ocpu>')
          sys.exit(2)
     for opt, arg in opts:
          if opt == '-h':
               print('cpuUpDown.py -v <x or y or z> -c <ocpu>')
               sys.exit()
          elif opt in ("-v"):
               tvm = arg
          elif opt in ("-c"):
               cpu = arg

     if tvm not in ["x", "y", "z"]:
          print('vm sholud be one of x, y, z')
          sys.exit(2)


if __name__ == "__main__":
   main(sys.argv[1:])


config = from_file()
auth = Signer(
tenancy=config['tenancy'],
user=config['user'],
fingerprint=config['fingerprint'],
private_key_file_location=config['key_file'],
pass_phrase=config['pass_phrase']
)


database_url=config['database_url']  
if tvm == "x": 
     vm=config['vmx']
elif tvm == "y": 
     vm=config['vmy']
elif tvm == "z": 
     vm=config['vmz']     
 
#GET
endpoint = database_url + 'vmClusters/' + vm
response = requests.get(endpoint, auth=auth)
y=json.loads(response.text)
print(y["displayName"], y["lifecycleState"], ": CPU ",  y["cpusEnabled"], "-->", cpu )

if str(y["cpusEnabled"]) == str(cpu):
     print('OCPU is same.')
     sys.exit(2)

# PUT
endpoint = database_url + 'vmClusters/' + vm

body = {
     "cpuCoreCount" : cpu
}

response = requests.put(endpoint, json=body, auth=auth)

json.loads(response.text)
#json.loads(response.raise_for_status())

