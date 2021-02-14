# freqtrade deployment

Configuration of the freqtrade trading bot using balena for the deployment and running on a raspberry pi.

 - Freqtrade: https://www.freqtrade.io/
 - Balena: https://www.balena.io/
 - Raspberry pi: https://www.raspberrypi.org/

## Setup

A binance, telegram, balena and github accounts are required to setup this deployment.

### Binance

 - Create an account on binance
 - Generate an API key and secret, save it for later

### Telegram
 - Follow the freqtrade instructions to create a telegram bot and obtain your chat id: https://www.freqtrade.io/en/latest/telegram-usage/

### Balena

 - Create an account on balena
 - Create an application and add a device to it
 - Use [balenaEtcher](https://www.balena.io/etcher/) to flash on a micro sd the image downloaded from balena
 - Plug in a raspberry pi with the micro sd and check if it appears as online on balena dashboard
 - Obtain a balena API key on "Preferences > Access Tokens" and save it for later
 - Add the folowing environment variables to your application
   - `EXCHANGE_KEY` (your binance api key)
   - `EXCHANGE_SECRET` (your binance api secret)
   - `TELEGRAM_TOKEN` (your telegram token)
   - `TELEGRAM_TOKEN_2` (another telegram token if you want to run 2 bots)
   - `TELEGRAM_CHAT_ID` (your telegram chat id)

### Github
 - Fork this github project
 - Add the folowing secrets to the repository on "Settings > Secrets"
   - `BALENA_API_TOKEN` (your balena api key)
   - `BALENA_APPLICATION_NAME` (the name of the application you have created on balena)
 - Modify configs and strategies to adjust to your preferences
