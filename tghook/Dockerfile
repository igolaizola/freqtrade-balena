# Build image
FROM balenalib/raspberrypi4-64-alpine-golang as build
RUN apk add --no-cache --update git

# Build binaries
ENV GO111MODULE=on
ENV forcepull 2021-05-23_0
RUN GOPROXY=direct go get github.com/igolaizola/tghook/cmd/tghook@595ecaf48016f52bc78e35b686d9addc9bac369d

# Final image
FROM balenalib/raspberrypi4-64-alpine

# Copy files
COPY --from=build /go/bin /bin
COPY /tghook.sh /tghook.sh
RUN chmod +x /tghook.sh

# Default run container without commands
CMD ["tail" "-f", "/dev/null" ]
