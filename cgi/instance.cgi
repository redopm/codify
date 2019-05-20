#!/usr/bin/python2

import  cgi,cgitb,os,commands,time,subprocess
cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_name=web.getvalue('n')
os_ram=web.getvalue('r')
os_cpu=web.getvalue('c')
os_hdd=web.getvalue('h')

print  os_name,os_ram,os_cpu,os_hdd
#  launching os 

if  os_name ==  "ubuntu1610"  :
	print  os.system('sudo  virt-install  --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --nodisk  --cdrom  /ubuntu1610.iso --noautoconsole')

elif  os_name == "redhat"  :
	print  os.system('sudo  virt-install  --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/osrhel75.qcow2,size='+os_hdd+'  --location ftp://192.168.10.254/pub/rhel75/')

elif  os_name ==  "rhel7"  :
	#  a fresh copy 
	print  os.system('sudo  qemu-img   create -f  qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2  /var/lib/libvirt/images/'+os_name+'.qcow2')
	print  os.system('sudo  virt-install  --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2  --import  --noautoconsole')




