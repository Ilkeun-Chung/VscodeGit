# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl 
# or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import requests
from oci.config import from_file
from oci.signer import Signer
import json
import pprint


config = from_file()
auth = Signer(
tenancy=config['tenancy'],
user=config['user'],
fingerprint=config['fingerprint'],
private_key_file_location=config['key_file'],
pass_phrase=config['pass_phrase']
)

database_url=config['database_url'] 
compartment=config['compartment']
vm=config['vmx']

endpoint = database_url + 'dbHomes?compartmentId=' + compartment + '&vmcluster=' + vm

response = requests.get(endpoint, auth=auth)
#response.raise_for_status()
#print(response.text)

#pprint.pprint(json.loads(response.text))

for y in json.loads(response.text):
    print("{:<35} {:<20} {:<45} {:<10}".format(y['displayName'],y['dbVersion'], y['dbHomeLocation'], y['lifecycleState']))