FROM alpine:edge

RUN apk update && apk add motion --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

ENTRYPOINT motion -c '/etc/motion/motion.conf'

