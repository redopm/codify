#!/usr/bin/python
import  cgi
import  commands
import  os
import  cgitb  # traceback errors in  web apps
cgitb.enable()
# print("Content-Type: text/html;charset=utf-8")
print  "Content-Type: text/html\r\n\r\n"
print  ""
# gettting  html data 
mypage=cgi.FieldStorage()
#print mypage
mycmd=mypage.getvalue('running_instance')
if mycmd :
	print "<html>"
	print "<meta http-equiv='refresh' content='100;url=http://localhost/ec2manage.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print commands.getoutput(virsh list)
	print "<pre></h2>"
	print "</body>"
	print "</html>"

else :
	redirectURL = "http://localhost/ec2manage.html"
	print('<html>')
	print('  <head>')
	print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
	print('  </head>')
	print('</html>')

print CGI::header();
