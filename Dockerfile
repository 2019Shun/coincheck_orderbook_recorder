FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y libpq-dev
RUN apt install -y cron nano screen
RUN pip3 install numpy matplotlib
RUN pip3 install psycopg2
RUN pip3 install requests

RUN mkdir /root/script

RUN echo '*/1 * * * * root /usr/bin/bash -l /root/script/cron.sh >> /root/script/cron.log 2>&1' >> /etc/crontab

RUN service cron restart