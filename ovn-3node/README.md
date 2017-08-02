# ovn-3node: Virtual OVN Cluster using Vagrant

Install vagrant and libvirt provider:

```bash
sudo yum install -y vagrant
sudo yum install -y vagrant-libvirt
```

Make sure vagrant has permissions needed to use libvirt:

```bash
sudo gpasswd -a ${USER} libvirt
newgrp libvirt
```

Checkout this repository.

```bash
git clone https://github.com/putnopvut/vagrants
cd vagrants/ovn-3node
```

Create CentOS VMs (OVN central and two OVN compute nodes):

```bash
vagrant up central
vagrant up compute1
vagrant up compute2
```

After provisioning is complete, ssh to central node, if
everything is worrking `ovn-sbctl show` should list two
chassis:
```bash
vagrant ssh central
sudo ovn-sbctl show
exit
```

Optionally, a third compute node running Fedora can be started:
```bash
vagrant up compute3
exit
```

When done, clean up:

```bash
vagrant destroy
```

See also:
* http://www.flaviof.com/blog2/post/main/just-ovn-nodes/
* http://blog.spinhirne.com/2016/09/a-primer-on-ovn.html

