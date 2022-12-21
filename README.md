# Clear-Device-Registrations

A simple python script for clearing out SDK, soft client, and device registrations for an individual user.  

It is sometimes the case that while testing a new browser SDK integration, you will hit a device registration limit if you are refreshing your page many times in a short period of time.

This script attempts to resolve this issue for a single user.

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
