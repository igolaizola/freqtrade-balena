#!/bin/bash
/bin/tghook -channel "$TGHOOK_CHANNEL" -filter "COIN IS[: ]*([a-Z]+)" \
-url http://freqtrade_2:8080/api/v1/forcebuy \
-method POST -data '{"pair": "$1/BTC"}' \
-header "Content-Type: application/json" \
-auth-user user -auth-pass pass \
-wait 100ms \
-upper true --trim true
