import requests
import json
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

userToken = "<USER_TOKEN>"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {userToken}",
}


def sendSpark(method, url, soapheaders=None, mydata=None):
    if mydata:
        contents = requests.request(
            method, url, data=json.dumps(mydata), headers=soapheaders, verify=False
        )
    else:
        contents = requests.request(method, url, headers=soapheaders, verify=False)
    # print(contents)
    return contents


# get device urls
url = "https://u2c-a.wbx2.com/wdm/api/v1/devices"
devices = sendSpark("GET", url, soapheaders=headers)

l_devices = devices.json()
for blah in l_devices["devices"]:
    print(blah["url"])
    thisDevUrl = blah["url"]
    try:
        delete_device = sendSpark("DELETE", thisDevUrl, soapheaders=headers)
    except:
        print(
            f"Unable to delete the connection. Must be done manually with the url {thisDevUrl}",
            sys.exc_info()[0],
        )
    if delete_device.status_code == 200:
        print("we deleted successfully")
    else:
        print("failed to delete successfully")

sys.exit() 