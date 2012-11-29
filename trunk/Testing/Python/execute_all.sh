#!/bin/sh
# Use this simple script to send all available execute requests to a WPS server

#HOST="http://localhost/cgi-bin/wps"
# HOST="http://blockfloete/wps"
HOST="http://192.168.56.101/cgi-bin/wps"
REQUESTS=1

for FILE in `find ExecuteRequests/ -name \*.xml` ; do
	echo "Send $FILE"
	python SendRequests.py --file=${FILE} --url=${HOST} --requests=${REQUESTS}
done
