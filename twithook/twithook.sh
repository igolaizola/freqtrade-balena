#!/bin/bash
/bin/twithook -user elonmusk -filter doge \
-url http://freqtrade:8080/api/v1/forcebuy \
-method POST -data '{"pair": "DOGE/USDT"}' \
-header "Content-Type: application/json" \
-auth-user user -auth-pass pass
