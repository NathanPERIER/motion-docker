#!/bin/sh

export MOTION_START_TIME=$(date '+%Y%m%d%H%M%S')


motion -c '/etc/motion/motion.conf'

