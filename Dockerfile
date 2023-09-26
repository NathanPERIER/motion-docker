FROM alpine:edge

RUN apk update && apk add motion --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

RUN apk add python3 py3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt && rm requirements.txt


RUN mkdir /etc/scripts
COPY scripts /etc/scripts/

ENTRYPOINT motion -c '/etc/motion/motion.conf'

