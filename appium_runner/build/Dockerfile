FROM python:3.10
 
USER root
 
RUN apt-get update && apt-get install -yy nano \
    curl

WORKDIR /test

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]

CMD [ "start.sh" ]
