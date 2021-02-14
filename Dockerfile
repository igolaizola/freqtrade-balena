FROM freqtradeorg/freqtrade:stable_pi

COPY run.sh /freqtrade/run.sh
COPY strategies /freqtrade/strategies
COPY configs /freqtrade/configs

# Default run container without commands
ENTRYPOINT ["tail"]
CMD [ "-f", "/dev/null" ]
