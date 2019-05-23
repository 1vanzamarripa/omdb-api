FROM python:3.7-alpine3.8

ENV PROJ=/proj/
ENV MOVIE=''

WORKDIR ${PROJ}
COPY src .

RUN pip install requests

CMD python /proj/do_get_rating.py $MOVIE
