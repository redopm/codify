# codify
It is website which is  provide the web hosting and private cloud platform.

Command for install private cloud 

320  virt-install  --name  rh3  --ram 2048  --vcpu  1  --disk path=/var/lib/libvirt/images/rhvm3.qcow2  --import  --noautoconsole  --graphics=vnc,listen=192.168.10.101,vncport=5993  
  321  virt-install  --name  rh3  --ram 2048  --vcpu  1  --disk path=/var/lib/libvirt/images/rhvm3.qcow2  --import  --noautoconsole  --graphics=vnc,listen=192.168.10.101,port=5993  
  322  virsh list
  323  virt-install  --name  rh2  --ram 2048  --vcpu  1  --disk path=/var/lib/libvirt/images/rhvm2.qcow2  --import  --noautoconsole  --graphics=vnc,listen=192.168.10.101,port=5994,password=redhat123  
  324  ls
  325  qemu-img  create -f qcow2  -b  rhvmdnd.qcow2  rhvm2.qcow2
  326  virt-install  --name  rh2  --ram 2048  --vcpu  1  --disk path=/var/lib/libvirt/images/rhvm2.qcow2  --import  --noautoconsole  --graphics=vnc,listen=192.168.10.101,port=5994,password=redhat123  
  327  virsh list
  328  history 
  329  yum install  ftp://192.168.10.254/pub/ashutoshh/cloud/qrencode-3.4.1-3.el7.x86_64.rpm
  330  cd  /root/Desktop/
  331  qrencode   -s  16x16  -o  myos.png
  332  cd
  333  yum  install python-websockify 
  334  yum  install ftp://192.168.10.254/pub/ashutoshh/cloud/python-websockify-0.6.0-2.el7.noarch.rpm
  335  yum  install ftp://192.168.10.254/pub/ashutoshh/cloud/novnc-0.5.1-2.el7.noarch.rpm
  336  history 
  337  cd  /usr/share/novnc/
  338  ls
  339  cd
  340  websockify   --help
  341  history 
  342  cd /usr/share/novnc/
  343  ls
  344  cd
  345  websockify  --web=/usr/share/novnc   6080  192.168.10.101:5993   
