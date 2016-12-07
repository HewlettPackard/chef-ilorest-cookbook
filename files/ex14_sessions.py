# Copyright 2016 Hewlett Packard Enterprise Development LP
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.

import sys
import urlparse
from _restobject import RestObject


def ex14_sessions(restobj, login_account, login_password):
    sys.stdout.write("\nEXAMPLE 14: Create/Use/Delete a user session\n")
    new_session = {"UserName": login_account, "Password": login_password}
    response = restobj.rest_post("/rest/v1/Sessions", new_session)
    restobj.error_handler(response)
    
    if response.status == 201:
        session_uri = response.getheader("location")
        session_uri = urlparse.urlparse(session_uri)
        sys.stdout.write("\tSession " + session_uri.path + " created\n")

        x_auth_token = response.getheader("x-auth-token")
        sys.stdout.write("\tSession key " + x_auth_token + " created\n")

        # Delete the created session
        sessresp = restobj.rest_delete(session_uri.path)
        restobj.error_handler(sessresp)
    else:
        sys.stderr.write("ERROR: failed to create a session.\n")

if __name__ == "__main__":
    # When running on the server locally use the following commented values
    # iLO_https_url = "blobstore://."
    # iLO_account = "None"
    # iLO_password = "None"

    # When running remotely connect using the iLO secured (https://) address, 
    # iLO account name, and password to send https requests
    # iLO_https_url acceptable examples:
    # "https://10.0.0.100"
    # "https://f250asha.americas.hpqcorp.net"
    try:
        iLO_https_url = "https://" + str(sys.argv[1])
        iLO_account = str(sys.argv[2])
        iLO_password = str(sys.argv[3])
    
        #Create a REST object
        REST_OBJ = RestObject(iLO_https_url, iLO_account, iLO_password)
		ex14_sessions(REST_OBJ, "admin", "admin123")

    except Exception:
        sys.stderr.write("Credentials Error \n")
