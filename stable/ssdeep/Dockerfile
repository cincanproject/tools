# "Ssdeep is a program for computing context triggered piecewise hashes (CTPH), also called fuzzy hashes"
#  GNU General Public License:  https://www.gnu.org/licenses/gpl-3.0.html

ARG tool_version=d8705da60369a27a2b5d22da488416e8ab348d8f
FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	make>4.2.1-r2 \
	automake>1.16.1-r0 \
	autoconf>2.69-r2 \
	libtool>2.4.6-r7 \
	g++>9.2.0-r3 \
	git>2.24.1-r0 \
	&& git clone https://github.com/ssdeep-project/ssdeep.git \
	&& cd ssdeep \
	&& git checkout $TOOL_VERSION \
	&& ./bootstrap \
	&& ./configure --prefix=/ssdeep \
	&& make \
	&& make install \
	&& adduser -s /sbin/login -D appuser \
	&& chown -R appuser:appuser /ssdeep

USER appuser

WORKDIR /home/appuser

# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["/ssdeep/ssdeep"]
CMD ["-h"]
