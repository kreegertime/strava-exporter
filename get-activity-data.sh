#!/bin/sh
curl -k -G https://www.strava.com/api/v3/athlete/activities \
  -H "Authorization: Bearer ee98c9f6b56ed710bfcfe9376211d353c7c7779c" \
  -d page=$1
