#!/usr/bin/env python2

import contextlib
import os
import urllib
import urllib2

def format_alert():
    return '%s - %s is %s' % (
        os.getenv('NOTIFICATIONTYPE', '???'),
        os.getenv('SERVICEDISPLAYNAME', '???'),
        os.getenv('SERVICEOUTPUT', '???')
    )

def send_alert():
    pager = os.getenv('USERPAGER')
    if pager is None:
        return
    query = urllib.urlencode({
        'dest': pager,
        'text': format_alert()
    })

    url = 'http://172.19.0.2/cgi-bin/sms?%s' % query

    with contextlib.closing(urllib2.urlopen(url)) as req:
        print 'Response: %s' % (req.read())

if __name__ == '__main__':
    send_alert()
