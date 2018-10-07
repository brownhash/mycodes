import urllib.request as req
myval=input("Enter a word >>> ")
conn = req.urlopen("http://wdylike.appspot.com/?q="+myval)
print(conn.read())
