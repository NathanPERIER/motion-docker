FROM alpine:latest

RUN apk update && apk add motion --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python
RUN --mount=type=bind,source=./requirements.txt,target=/tmp/requirements.txt \
    pip3 install --break-system-packages -r /tmp/requirements.txt

ENV MOTION_STARTUP_DELAY=1m

RUN mkdir /etc/scripts /opt/motion
COPY scripts /etc/scripts/

WORKDIR /opt/motion
COPY start.sh ./

ENTRYPOINT ["sh", "start.sh"]

