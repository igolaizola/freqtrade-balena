#!/bin/bash

# Create user directory structure if not exists
if [ ! -d "/freqtrade/user_data/data" ]; then
    freqtrade create-userdir --userdir user_data
fi

# Copy strategy files to user_data folder
cp -r strategies/. user_data/strategies

# Obtain telegram enviroment variable name from argument
VAR_TELEGRAM_TOKEN="$3"

# Inject environment variables in config file
sed -e 's/TELEGRAM_TOKEN/'"${!VAR_TELEGRAM_TOKEN}"'/g' \
    -e 's/TELEGRAM_CHAT_ID/'"$TELEGRAM_CHAT_ID"'/g' \
    -e 's/EXCHANGE_KEY/'"$EXCHANGE_KEY"'/g' \
    -e 's/EXCHANGE_SECRET/'"$EXCHANGE_SECRET"'/g' \
    configs/secret.json.template > configs/secret.json

# Launch bot
freqtrade trade \
      --logfile /freqtrade/user_data/logs/freqtrade.log \
      --db-url sqlite:////freqtrade/user_data/tradesv3.sqlite \
      --config "/freqtrade/configs/$1" \
      --config /freqtrade/configs/secret.json \
      --strategy "$2"
