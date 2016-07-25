#!/bin/bash
#


# Interactive Sanity check, check login and environment variables are set.
function CheckSetup() {
    if [ "$ASPACE_API_URL" = "" ]; then
        echo "Enter the URL to the AchivesSpace REST API (e.g. http://localhost:8089) "
        read -p "URL: " ASPACE_API_URL
        if [ "$ASPACE_API_URL" = "" ]; then
            ASPACE_API_URL="http://localhost:8089"
        fi
        export ASPACE_API_URL
    fi
    if [ "$ASPACE_API_TOKEN" = "" ]; then
        echo "Enter the ArchivesSpace username and password to authenticate and get token:"
        read -p "Username: " ASPACE_USERNAME
        read -s -p "Password: " ASPACE_PASSWORD
        if [ "$ASPACE_USERNAME" = "" ]; then
            ASPACE_USERNAME="admin"
        fi
        if [ "$ASPACE_PASSWORD" = "" ]; then
            ASPACE_PASSWORD="admin"
        fi
        export ASPACE_API_TOKEN=$(curl -L -X GET -Fpassword=$ASPACE_PASSWORD $ASPACE_API_URL/users/$ASPACE_USERNAME/login | jq -r '.session')
    fi
}

function Usage () {
    cat <<EOM
 USAGE

    ./scripts/api.sh API_PATH [METHOD] [FILENAME_FOR_PAYLOAD]
 
 Provides a wrapper around *curl* and *jq* for working with the 
 ArchivesSpace v1.5.0 API

EOM

    exit 1
}

#
# Process command line args
#
CheckSetup
API_PATH=$1
METHOD=$2
PAYLOAD=$3

if [ "$API_PATH" = "" ]; then
    Usage
fi
if [ "$METHOD" = "" ]; then
    METHOD="GET"
fi




if [ "$PAYLOAD" = "" ]; then
cat <<CMD
    curl -H "X-ArchivesSpace-Session: $ASPACE_API_TOKEN" \
        -X "$METHOD" \
        "$ASPACE_API_URL/$API_PATH" | jq .
CMD

    curl -H "X-ArchivesSpace-Session: $ASPACE_API_TOKEN" \
        -X "$METHOD" \
        "$ASPACE_API_URL/$API_PATH" | jq .
else
    curl -H "X-ArchivesSpace-Session: $ASPACE_API_TOKEN" \
        -X $METHOD \
        --data-binary "@PAYLOAD" \
        $ASPACE_API_URL/$API_PATH | jq .
fi
