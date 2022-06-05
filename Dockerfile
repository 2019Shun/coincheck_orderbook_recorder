FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y libpq-dev
RUN apt install -y cron nano screen
RUN pip3 install numpy matplotlib
RUN pip3 install psycopg2
RUN pip3 install requests

RUN mkdir /root/script

RUN echo 'nohup python3 /root/script/recordCoincheckBtcOrderbook.py > /root/script/out.log &' >> /root/.bashrc