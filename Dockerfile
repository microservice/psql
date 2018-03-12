FROM          alpine:3.7
RUN           apk add --no-cache postgresql-client
ENTRYPOINT    ["/usr/bin/psql"]
