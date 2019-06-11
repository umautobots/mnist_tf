#! /bin/bash
if [ -z $1 ] ; then
  PORT=6006
else
  PORT=$1
fi

nvidia-docker run -it --rm \
  -v $PWD/logs:/logs:ro \
  -p $PORT:$PORT \
  tensorflow/tensorflow:1.13.1-gpu-py3 \
  tensorboard --logdir=/logs --port=$PORT
