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
git checkout DHCP_exclude
cd vagrants/ovn-3node
```

Create a CentOS VM

```bash
vagrant up
```

After provisioning is complete, ssh to central node, if
everything is worrking `ovn-sbctl show` should list one
chassis:
```bash
vagrant ssh central
sudo ovn-sbctl show
exit
```

The provisioning will set up three network namespaces on
the central node, each with a network device that gets
its IP address and default route via DHCP from OVN. The
vm1 and vm2 devices are on the 172.16.255.192/26 network
and the vm3 device is on the 10.0.0.0/24 network. You
can view the setup\_routing\_central file to see how
the OVN logical switches and routers were set up, as well
as how the network namespaces were set up. The file is
well commented so you should understand how everything
fits together.

You can view the IP address of a given device:
```bash
vagrant ssh central
sudo ip netns exec vm1 ip addr show vm1
exit
```
You can do the same thing with the vm2 and vm3 namespaces to
verify their address assignments. The expected assigned IP
addresses are:

* vm1: 172.16.255.196
* vm2: 172.16.255.197
* vm3: 10.0.0.101

When done, clean up:

```bash
vagrant destroy
```

See also:
* http://www.flaviof.com/blog2/post/main/just-ovn-nodes/
* http://blog.spinhirne.com/2016/09/a-primer-on-ovn.html
