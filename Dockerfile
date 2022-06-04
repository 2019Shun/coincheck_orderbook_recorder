FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y libpq-dev
RUN apt install -y cron nano screen
RUN pip3 install numpy matplotlib
RUN pip3 install psycopg2
RUN pip3 install requests
RUN pip3 install schedule

RUN mkdir /root/script

RUN echo 'export DB_IPADDRESS="172.30.0.2"' >> /etc/crontab
RUN echo 'export DB_NAME="coincheck"' >> /etc/crontab
RUN echo 'export DB_USER="coincheck"' >> /etc/crontab
RUN echo 'export DB_PASSWORD="coincheck"' >> /etc/crontab
# RUN echo '*/1 * * * * root /root/script/cron.sh >> /root/script/cron.log 2>&1' >> /etc/crontab
RUN echo '* * * * * for i in `seq 0 10 59`;do (sleep ${i}; /root/script/cron.sh) & done;' >> /etc/crontab

RUN service cron restart