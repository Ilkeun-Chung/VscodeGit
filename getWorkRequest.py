
import requests
from oci.config import from_file
from oci.signer import Signer
import json



config = from_file()
auth = Signer(
tenancy=config['tenancy'],
user=config['user'],
fingerprint=config['fingerprint'],
private_key_file_location=config['key_file'],
pass_phrase=config['pass_phrase']
)

iaas_url=config['iaas_url'] 
compartment=config['compartment']

endpoint = iaas_url + 'workRequests?compartmentId=' + compartment
response = requests.get(endpoint, auth=auth)

for y in json.loads(response.text):
    print("{:<30} {:<20} {:<7} {:<20} {:<20}".format(y['operationType'],y['status'], y['percentComplete'], y['timeStarted'],  str(y['timeFinished'])))