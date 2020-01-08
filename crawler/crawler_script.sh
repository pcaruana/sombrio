#!/bin/bash

tor --SocksPort 9150 &
sleep 15
./crawl_server.py --port "5000" --threads 4 --user-agent "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0" --queue-host "x.x.x.x" --queue-port "5000" --mgmt-host "y.y.y.y" --mgmt-port "5000"
