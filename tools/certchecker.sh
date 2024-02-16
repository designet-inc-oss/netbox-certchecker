#!/bin/bash

function checkaccess() {
    expire=""
    expire=`curl -v $1 3> /dev/null 2>&1 1>&3 | grep "expire date" | sed 's/\*\s*expire date:\s*\(.*\)/\1/g'`
    if [ $? -ne 0 ]; then
        echo "Failed to ssl connect: $1"
        echo "command: curl -v $1" 
        return 1
    fi

    echo $expire
    return 0
}

function send_mail() {
    cat <<EOF | curl -q --ssl --url smtp://$SMTP_SERVER:$SMTP_PORT/ -u $SMTP_USER:$SMTP_PASSWORD --mail-from $MAIL_FROM --mail-rcpt $MAIL_RECIPIENT -T - >/dev/null 2>&1
From: <$MAIL_FROM>
To: <$MAIL_RECIPIENT>
Subject: $SUBJECT_PREF - $name

Certificate error detected for $url.

ID: $id
Name: $name
URL: $url

[Netbox resource]
URL: $NETBOX_URLPREF/$id/

[Expire date]
$expire
EOF

}

##################################################
# Main
##################################################
config_file="/etc/netbox_certchecker.conf"

while getopts ":c:" opt; do
  case $opt in
    c)
      config_file=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

if [ ! -f "$config_file" ]; then
  echo "Invalid config file $config_file" >&2
  exit 1
fi

source "$config_file"

# Get data from the API endpoint
response=$(curl -s -H "Authorization: Token $API_TOKEN" "$API_ENDPOINT")

# Check if the response contains results
if [[  -z $(echo "$response" | jq -r '.results[]') ]]; then
   #  echo "No data found in the API response."
   exit 0
fi

# Process each element in the results array
echo "$response" | jq -c '.results[]' | while read element; do
    id="$(echo "$element" | jq -r '.id')"
    name="$(echo "$element" | jq -r '.name')"
    url="$(echo "$element" | jq -r '.url')"
    
    # Check certificate error
    expire=`checkaccess $url`
    if [ $? -ne 0 ]; then
        send_mail
        exit 0
    fi
  
    nowtimestamp=`date +%s`
    expire_timestamp=`date -d "$expire" +"%s"`
    diff=$(( ${expire_timestamp} - ${nowtimestamp} ))
    if [ $diff -lt $(($EXPIRE_WARN_DAY * 60 * 60 * 24)) ]; then
        send_mail
    fi
done
exit 0
