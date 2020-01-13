FROM alpine:edge AS builder

ENV VERSION 4.0.0
ENV radare2_SHA256_4.1.0 f86a4e070c61f58290c94d97897d6433ee8c4fef102e26d94be9279b7ab70988
ENV radare2_SHA256 5ec7639fc6625dd395ce81c192a7d4a7d624ac87405621d3aae0ecbcd89c670c
ENV radare2_SHA256_4.1.1 c85012e11ae43eb10aa0179e4cee0dba451bf31390a360bc245cd66e960fab80 
# ENV radare2_SHA256 c85012e11ae43eb10aa0179e4cee0dba451bf31390a360bc245cd66e960fab80 


ENV SOURCE_ROOT /radare2
ENV INSTALL_PREFIX /usr/local

# Dependencies
RUN apk add --no-cache \
        libc6-compat \
        make \
        ncurses-libs \
		npm \
        cmake \
        g++ \
        gcc \
        git \
        linux-headers \
        unzip \
        wget \
        curl \
        git \
        bison \
        flex \
        xxd \
        pkgconfig \ 
        python3 

RUN apk add --no-cache meson

RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

# RUN install -d -o appuser -g appuser -m 770 /radare2/
RUN mkdir "$SOURCE_ROOT" \
    && chown -R appuser:appuser "$SOURCE_ROOT" \
    && chmod -R 775 "$SOURCE_ROOT" \
    && chown -R appuser:appuser "$INSTALL_PREFIX" \
    && chmod -R 775 "$INSTALL_PREFIX"

# RUN wget --progress=bar:force -O "$INSTALL_ROOT"/radare2.zip "https://github.com/radareorg/radare2/archive/$VERSION.zip" \
#     && echo "$radare2_SHA256"  \
#     && sha256sum "$INSTALL_ROOT"/radare2.zip \
#     && echo "$radare2_SHA256  $INSTALL_ROOT/radare2.zip" | sha256sum -c - \
#     && unzip "$INSTALL_ROOT"/radare2.zip -d "$INSTALL_ROOT"



# WORKDIR "$INSTALL_ROOT/radare2-$VERSION/sys"

# WORKDIR "$SOURCE_ROOT/sys"


# RUN sh user.sh --install-path "$INSTALL_ROOT" && make install

# Build portable binaries with meson
# RUN ./meson.py --dir "/$INSTALL_ROOT/build" --local

# RUN mkdir -p "${INSTALL_ROOT}/build/lib" && \
#     sh build.sh "$INSTALL_ROOT/build/" && make install

# RUN sh user.sh --install-path "$INSTALL_ROOT/build/" && make install
USER appuser

RUN git clone --depth 1 https://github.com/radareorg/radare2.git "$SOURCE_ROOT" && \
    cd "$SOURCE_ROOT/sys" && \
    meson --prefix="$INSTALL_PREFIX" && \
    ninja && \
    ninja install && \
    ln -s "$INSTALL_PREFIX/bin/radare2" "$INSTALL_PREFIX/bin/r2"
# && \



RUN r2pm init && \
    r2pm update && \
    r2pm -i r2ghidra-dec && \
    r2pm cache && \
    # && \
    # r2pm clean
    rm -rf /usr/appuser/.local/share/radare2/r2pm/git/r2ghidra-dec.git


# USER root

# # Script based packages

# RUN apk add --no-cache graphviz

# Folders for scripts

# SECOND STAGE

FROM alpine:latest AS runner

# ENV INSTALL_ROOT /radare2

# ENV VERSION 4.0.0
# ENV R2_PIPE_PY_VERSION=1.4.2

# # # Get liblarires and bins from builder
ENV INSTALL_PREFIX /usr/local
ENV SOURCE_ROOT /radare2

RUN apk add --no-cache git && \
    addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

COPY --from=builder "$INSTALL_PREFIX" "$INSTALL_PREFIX"
COPY --from=builder /home/appuser/ /home/appuser/




RUN mkdir -p /r2/samples && \
    mkdir -p /r2/results && \
    chown -R appuser:appuser /r2/results && \
    chown -R appuser:appuser /r2/samples/


USER appuser
# Optional r2dec r2frida


# Plugin manager configuration
ENV R2PM_PLUGDIR=/home/appuser/.local/share/radare2/plugins
ENV R2PM_BINDIR=/home/appuser/.local/share/radare2/prefix/bin
ENV R2PM_DBDIR=/home/appuser/.local/share/radare2/r2pm/db
ENV R2PM_GITDIR=/home/appuser/.local/share/radare2/r2pm/git/

COPY entrypoint.sh "$SOURCE_ROOT"/entrypoint.sh
COPY scripts "$SOURCE_ROOT"/scripts


# RUN du -sh /radare2 && du -sh /home/appuser/.local/share/radare2/

# Used by wrapper script
ENV R2_HOME="$INSTALL_PREFIX/bin"
ENV R2_SCRIPTS="$SOURCE_ROOT/scripts"



# COPY --from=builder /home/appuser/.local/share/radare2/ /home/appuser/.local/share/radare2

# # Plugin manager configuration
# ENV R2PM_PLUGDIR=/home/appuser/.local/share/radare2/plugins
# ENV R2PM_BINDIR=/home/appuser/.local/share/radare2/prefix/bin
# ENV R2PM_DBDIR=/home/appuser/.local/share/radare2/r2pm/db
# ENV R2PM_GITDIR=/home/appuser/.local/share/radare2/r2pm/git/

# Remove .git directory
# RUN rm -rf /home/appuser/.local/share/radare2/r2pm/git/



# USER appuser

# WORKDIR /home/appuser

USER root

# ENTRYPOINT ["sh", "/radare2/entrypoint.sh"]
