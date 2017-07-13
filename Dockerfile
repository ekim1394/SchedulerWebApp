FROM alpine:3.1

MAINTAINER Eugene Kim

# Adding/Updating python
RUN apk add --update python py-pip

# Adding Source Files
ADD /CCSite /webapp

# Install app dependencies
RUN pip install -r /webapp/requirements.txt

EXPOSE  8080

WORKDIR /webapp

CMD ["python", ".\CCSite\run.py"]