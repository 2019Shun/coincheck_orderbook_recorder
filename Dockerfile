FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libpq-dev
RUN pip3 install numpy matplotlib
RUN pip3 install psycopg2
RUN pip3 install requests

RUN mkdir /root/script