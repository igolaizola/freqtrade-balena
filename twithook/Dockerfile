# Build image
FROM balenalib/raspberrypi4-64-alpine-golang as build
RUN apk add --no-cache --update git

# Build binaries
ENV GO111MODULE=on
ENV forcepull 2021-05-10_0
RUN GOPROXY=direct go get github.com/igolaizola/twithook/cmd/twithook@8b334729612a99c15b5ce8d8a3852f5ef710eb78

# Final image
FROM balenalib/raspberrypi4-64-alpine

# Copy files
COPY --from=build /go/bin /bin
COPY /twithook.sh /twithook.sh
RUN chmod +x /twithook.sh

# Default run container without commands
CMD ["tail" "-f", "/dev/null" ]
