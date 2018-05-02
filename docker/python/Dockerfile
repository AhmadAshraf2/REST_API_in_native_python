FROM python:3.6

#creating work directory
RUN mkdir -p /var/www
WORKDIR /var/www

#copying code files
COPY . .

RUN pip install -r requirements.txt

#cleanup
USER root
RUN apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
