FROM tensorflow/tensorflow:latest-gpu-jupyter
MAINTAINER Kim-Ken
RUN apt-get update
RUN apt-get install -y python3-pip git 
RUN pip3 install torch sklearn gym  
RUN mkdir /work