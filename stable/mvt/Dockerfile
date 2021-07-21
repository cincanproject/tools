ARG tool_version=v1.0.11

FROM python:3-slim-buster

ARG tool_version
ENV TOOL_VERSION=$tool_version

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y libusb-1.0-0 \
    wget \
    unzip \ 
    gosu \
    usbutils \
    adb \
    udev && \
    pip3 install mvt==${TOOL_VERSION} && \
    groupadd -g 1000 appuser && \
    groupadd adbusers && \
    useradd -u 1000 -g appuser -s /sbin/nologin -m appuser && \
    usermod -aG plugdev appuser && \
    usermod -aG adbusers appuser && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/*

# Use existing comprehensive list https://github.com/M0Rf30/android-udev-rules
RUN wget -O /etc/udev/rules.d/51-android.rules https://raw.githubusercontent.com/M0Rf30/android-udev-rules/master/51-android.rules && \
    chmod a+r /etc/udev/rules.d/51-android.rules && \
    gosu appuser mkdir /home/appuser/tool && \
    # First run to create some default files
    gosu appuser adb start-server && \
    gosu appuser adb kill-server

WORKDIR /home/appuser/
COPY entrypoint.sh .
COPY meta.json /opt/

WORKDIR /home/appuser/tool

USER appuser

ENTRYPOINT [ "bash", "/home/appuser/entrypoint.sh" ]
CMD ["--help"]