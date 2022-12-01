#!/bin/bash
unzip -d /opt/ep/matlab /opt/ep/btc_ep.jar scripts/* spec/* x64/* linux/*
mkdir /opt/ep/matlab/java
mv /opt/ep/btc_ep.jar /opt/ep/matlab/java/
sudo mv /opt/ep/matlab/scripts/m/init/btc_eprc.m /opt/matlab/toolbox/local/

echo "/opt/ep/matlab/java/btc_ep.jar">>/opt/matlab/toolbox/local/classpath.txt

echo "if (isempty(which('btc_eprc')))">>/opt/matlab/toolbox/local/matlabrc.m
echo "   rehash toolboxcache">>/opt/matlab/toolbox/local/matlabrc.m
echo "end">>/opt/matlab/toolbox/local/matlabrc.m
echo "btc_eprc;">>/opt/matlab/toolbox/local/matlabrc.m
