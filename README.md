# Clear-Device-Registrations
Welcome to our WXSD DEMO Repo! <!-- Keep this here --> 

This is a simple python script for clearing out SDK, soft client, and device registrations for an individual user.  

It is sometimes the case that while testing a new browser SDK integration, you will hit a device registration limit if you are refreshing your page many times in a short period of time.

This script attempts to resolve this issue for a single user.


<!-- Keep the following here -->  
 *_Everything included is for demo and Proof of Concept purposes only. Your use of the site is solely at your own risk. This site may contain links to third party content, which we do not warrant, endorse, or assume liability for. These demos are for Cisco Webex usecases, but are not Official Cisco Webex Branded demos._
 
 
## Overview

Requirements:
1. python version >= 3.8
2. pip install modules.

## Setup

1. Clone this repository
2. Set a user token for the impacted user on line 9 of **clear_devices.py**
3. Navigate to the cloned directory in your terminal, and make sure you have the requests module installed. Run:
```
pip install requests
```
4. Run the following in the terminal:
```
python clear_devices.py
```


## Support

Please reach out to the WXSD team at [wxsd@external.cisco.com](mailto:wxsd@external.cisco.com?cc=<your_cec>@cisco.com&subject=RepoName).
