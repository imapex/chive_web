FROM hypriot/rpi-alpine-scratch
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

EXPOSE 5001

RUN apk add --update \
    python \
    py-pip \

  && rm -rf /var/cache/apk/*

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "./chive_web/chive_web.py" ]