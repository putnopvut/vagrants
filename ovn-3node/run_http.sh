#!/bin/bash
#sudo ip netns exec $1 python -m SimpleHTTPServer 8000

cd /tmp/www/$1
ipaddr=$(sudo ip netns exec $1 ip -o -6 addr show permanent primary scope global | sed -r 's_.*(fd0f[^/]+)/.*$_\1_')
sudo ip netns exec $1 /vagrant/http.py $ipaddr
