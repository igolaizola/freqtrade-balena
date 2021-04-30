FROM freqtradeorg/freqtrade:stable_pi

COPY --chown=ftuser:ftuser run.sh /freqtrade/run.sh
COPY --chown=ftuser:ftuser strategies /freqtrade/strategies
COPY --chown=ftuser:ftuser configs /freqtrade/configs

# Default run container without commands
ENTRYPOINT ["tail"]
CMD [ "-f", "/dev/null" ]
