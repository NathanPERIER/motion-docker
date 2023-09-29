FROM alpine:edge

RUN apk update && apk add motion --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python
COPY ./requirements.txt ./
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED && pip3 install -r requirements.txt && rm requirements.txt

ENV MOTION_STARTUP_DELAY=1m

RUN mkdir /etc/scripts /opt/motion
COPY scripts /etc/scripts/

WORKDIR /opt/motion
COPY start.sh ./

ENTRYPOINT sh start.sh

