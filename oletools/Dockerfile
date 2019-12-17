FROM python:3.8-alpine as build

# olevba latest installation in python3

LABEL MAINTAINER=cincan.io

RUN apk update && \
	# apk add --no-cache --update python3 \
	# python3-dev \
	# openssl-dev \
	git=2.20.1-r0 \
	gcc 
	# libffi-dev \
	# libc-dev && \
	# pip3 install --upgrade pip && \
	# pip3 install --upgrade pip setuptools 

RUN pip3 install -U oletools --user

FROM python:3.8-alpine as runtime

RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser && 

COPY --from=build /root/.local /oletools

ENV PATH=/oletools/.local/bin:$PATH

ADD Oletools-license .

USER appuser

ENTRYPOINT ["olevba"]
CMD ["--help"]
