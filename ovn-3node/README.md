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
git clone https://github.com/hlrichardson/vagrants
cd vagrants/ovn-3node
```

Create CentOS VM:

```bash
vagrant up
```

This will create a load balancer scenario you can test. There are
scripts included that can help you to test properly. I found the
easiest way to test is to open multiple ssh sessions.

In session 1
```bash
vagrant ssh central
/vagrant/run_http.sh vm1
```

In session 2
```bash
vagrant ssh central
/vagrant/run_http.sh vm2
```

In session 3
```bash
vagrant ssh central
/vagrant/curl_http.sh 10.0.0.100:8000
```

In session 3, you should see either "I am vm1" or "I am vm2"
each time you run the `curl_http.sh` script.

When done, clean up:

```bash
vagrant destroy
```

See also:
* http://www.flaviof.com/blog2/post/main/just-ovn-nodes/
* http://blog.spinhirne.com/2016/09/a-primer-on-ovn.html

