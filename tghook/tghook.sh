#!/bin/bash
/bin/tghook -channel igotest01 -filter "COIN IS[: ]*([A-Z]+)" \
-url http://freqtrade_2:8080/api/v1/forcebuy \
-method POST -data '{"pair": "$1/BTC"}' \
-header "Content-Type: application/json" \
-auth-user user -auth-pass pass \
-upper true --trim true
