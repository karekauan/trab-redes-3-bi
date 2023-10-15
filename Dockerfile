FROM postgres:latest

RUN apt-get update && \
    apt-get install -y postgresql-client

EXPOSE 5432

CMD ["postgres"]