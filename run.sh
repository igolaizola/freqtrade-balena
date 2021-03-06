#!/bin/bash

# Create user directory structure if not exists
if [ ! -d "/freqtrade/user_data/data" ]; then
    freqtrade create-userdir --userdir user_data
fi

# Copy strategy files to user_data folder
cp -r strategies/. user_data/strategies

# Obtain enviroment variable names from argument
VAR_TELEGRAM_TOKEN="$3"
VAR_EXCHANGE_KEY="$4"
VAR_EXCHANGE_SECRET="$5"

# Inject environment variables in config file
sed -e 's/TELEGRAM_TOKEN/'"${!VAR_TELEGRAM_TOKEN}"'/g' \
    -e 's/TELEGRAM_CHAT_ID/'"$TELEGRAM_CHAT_ID"'/g' \
    -e 's/EXCHANGE_KEY/'"${!VAR_EXCHANGE_KEY}"'/g' \
    -e 's/EXCHANGE_SECRET/'"${!VAR_EXCHANGE_SECRET}"'/g' \
    configs/secret.json.template > configs/secret.json

# Launch bot
freqtrade trade \
      --logfile /freqtrade/user_data/logs/freqtrade.log \
      --db-url sqlite:////freqtrade/user_data/tradesv3.sqlite \
      --config "/freqtrade/configs/$1" \
      --config /freqtrade/configs/secret.json \
      --strategy "$2"
