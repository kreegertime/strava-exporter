#!/usr/bin/python
import json
import subprocess
from pprint import pprint
from dateutil.parser import parse

should_search = True
page = 1
while should_search:
  p = subprocess.Popen(["./get-activity-data.sh", str(page)], stdout=subprocess.PIPE)
  out, err = p.communicate()
  activity_json = json.loads(out)
  for activity in activity_json:
    try:
      date = parse(activity['start_date'])
      if date.year < 2013:
        should_search = False
      else:
        dp = subprocess.Popen(["./save-activity-id-data.sh", str(activity['id']), str(activity['external_id'])], stdout=subprocess.PIPE)
        dp_out, dp_err = dp.communicate()
        print "Saved activity " + str(activity['id']) + str(activity['external_id']) + " - " + str(date)
    except:
      print "Unexpected error processing activity:"
      print activity
      print "---------------------------------------"
  page += 1

