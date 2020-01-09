# "Ssdeep is a program for computing context triggered piecewise hashes (CTPH), also called fuzzy hashes"
#  GNU General Public License:  https://www.gnu.org/licenses/gpl-3.0.html

FROM alpine:3.11

LABEL MAINTAINER=cincan.io

ENV VERSION=2.14.1

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	make \
	automake \
	autoconf \
	libtool \
	g++ \
	git \
	&& git clone https://github.com/ssdeep-project/ssdeep.git \
	&& cd ssdeep \
	&& git checkout d8705da60369a27a2b5d22da488416e8ab348d8f \
	&& ./bootstrap \
	&& ./configure --prefix=/ssdeep \
	&& make \
	&& make install \
	&& adduser -s /sbin/login -D appuser \
	&& chown -R appuser:appuser /ssdeep

USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["/ssdeep/ssdeep"]
CMD ["-h"]
