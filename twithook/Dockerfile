# Build image
FROM --platform=linux/arm golang:alpine as build
RUN apk add --no-cache --update git

# Build binaries
ENV GO111MODULE=on
ENV forcepull 2021-05-01_0
RUN GOPROXY=direct go get github.com/igolaizola/twithook/cmd/twithook@7bcb0f8d8ae5899cc02c55a63ce173234b4734d7

# Final image
FROM --platform=linux/arm alpine

# Copy files
COPY --from=build /go/bin /bin
COPY /twithook.sh /twithook.sh
RUN chmod +x /twithook.sh

# Default run container without commands
CMD ["tail" "-f", "/dev/null" ]
