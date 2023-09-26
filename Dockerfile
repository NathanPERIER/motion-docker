FROM alpine:edge

RUN apk update && apk add motion --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python
COPY ./requirements.txt ./
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED && pip3 install -r requirements.txt && rm requirements.txt


RUN mkdir /etc/scripts
COPY scripts /etc/scripts/

ENTRYPOINT motion -c '/etc/motion/motion.conf'

