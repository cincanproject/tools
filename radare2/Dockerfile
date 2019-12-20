FROM alpine:edge AS builder

# Prevent build fails because of interactive scripts when compiling
ENV DEBIAN_FRONTEND noninteractive

ENV VERSION 4.0.0
ENV radare2_SHA256_4.1.0 f86a4e070c61f58290c94d97897d6433ee8c4fef102e26d94be9279b7ab70988
ENV radare2_SHA256 5ec7639fc6625dd395ce81c192a7d4a7d624ac87405621d3aae0ecbcd89c670c


ENV INSTALL_ROOT /radare2
# Dependencies
RUN apk add --no-cache \
        libc6-compat \
        make \
        ncurses-libs \
       	nodejs-current \
		npm \
        cmake \
        g++ \
        gcc \
        git \
        linux-headers \
        unzip \
        wget \
        curl 
        # sudo


RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

# RUN install -d -o appuser -g appuser -m 770 /radare2/
RUN mkdir "$INSTALL_ROOT" \
    && chown -R appuser:appuser "$INSTALL_ROOT" \
    && chmod -R 775 "$INSTALL_ROOT"

USER appuser

RUN wget --progress=bar:force -O "$INSTALL_ROOT"/radare2.zip "https://github.com/radareorg/radare2/archive/$VERSION.zip" \
    && echo "$radare2_SHA256"  \
    && sha256sum "$INSTALL_ROOT"/radare2.zip \
    && echo "$radare2_SHA256  $INSTALL_ROOT/radare2.zip" | sha256sum -c - \
    && unzip "$INSTALL_ROOT"/radare2.zip -d "$INSTALL_ROOT"

WORKDIR "$INSTALL_ROOT/radare2-$VERSION/sys"

RUN sh user.sh && make install

# RUN git clone --recurse-submodules https://github.com/radareorg/cutter.git /opt/cutter
# RUN cd /opt/cutter && \
#     bash build.sh && \
#     bash -c 'if [[ ! -x "/opt/cutter/build/Cutter" ]]; then exit -1; fi'

# FROM alpine:edge AS runner

# # Add the dependencies we need for running
# RUN apk add --no-cache \
#          bash \
#          libuuid \
#          make \
#          python3 \
#          qt5-qtbase \
#          shadow \
#          su-exec

# # Get the compiled Cutter, r2 libs and bins from the builder
# COPY --from=builder /opt/cutter /opt/cutter
# COPY --from=builder /usr/lib /usr/lib
# COPY --from=builder /usr/share/radare2 /usr/share/radare2
# RUN cd /opt/cutter/radare2/binr && \
#     make install && \
#     make symstall install-symlink

# # Add r2 user
# RUN useradd r2

# # Prepare files to mount configurations later on
# RUN mkdir /var/sharedFolder && \
#     mkdir -p /home/r2/.config/radare2 && \
#     touch /home/r2/.radare2rc && \
#     chown -R r2:r2 /var/sharedFolder && \
#     chown -R r2:r2 /home/r2/

# WORKDIR /home/r2
# ADD entrypoint.sh /usr/local/bin/entrypoint.sh

# ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
