#!/bin/bash

cd /tmp/www/$1
sudo ip netns exec $1 python -m SimpleHTTPServer 8000
