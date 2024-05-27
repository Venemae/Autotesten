FROM python:3.10

USER root

RUN apt-get update && apt-get install -yy nano curl
    
WORKDIR /card_deck

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

ENTRYPOINT [ "/bin/bash" ]

CMD [ "start.sh" ]