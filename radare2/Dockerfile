FROM alpine:edge AS builder

ENV VERSION 4.0.0
ENV radare2_SHA256_4.1.1 c85012e11ae43eb10aa0179e4cee0dba451bf31390a360bc245cd66e960fab80 



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
    python3 \
    meson

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

USER appuser

# Waiting for 4.2 release, until then cloning master

RUN git clone --depth 1 https://github.com/radareorg/radare2.git "$SOURCE_ROOT" && \
    cd "$SOURCE_ROOT/sys" && \
    meson --prefix="$INSTALL_PREFIX" && \
    ninja && \
    ninja install && \
    ln -s "$INSTALL_PREFIX/bin/radare2" "$INSTALL_PREFIX/bin/r2"

RUN r2pm init && \
    r2pm update && \
    r2pm -i r2ghidra-dec && \
    r2pm cache && \
    # && \
    # r2pm clean
    rm -rf /home/appuser/.local/share/radare2/r2pm/git/r2ghidra-dec.git && \
    # Disable r2agent - no use in container
    rm /usr/local/bin/r2agent

# SECOND STAGE

FROM alpine:latest AS runner

ENV INSTALL_PREFIX /usr/local
ENV SOURCE_ROOT /radare2

# libstdc++ required by ghidra-dec in runtime

RUN apk add --no-cache libstdc++ && \
    addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser && \
    # Make directories for possible volume mounting
    mkdir -p /r2/samples && \
    mkdir -p /r2/results && \
    chown -R appuser:appuser /r2/results && \
    chown -R appuser:appuser /r2/samples/

# Get liblarires and bins from builder

COPY --from=builder "$INSTALL_PREFIX" "$INSTALL_PREFIX"
COPY --from=builder /home/appuser/ /home/appuser/

USER appuser

# Plugin manager configuration
ENV R2PM_PLUGDIR=/home/appuser/.local/share/radare2/plugins
ENV R2PM_BINDIR=/home/appuser/.local/share/radare2/prefix/bin
ENV R2PM_DBDIR=/home/appuser/.local/share/radare2/r2pm/db
ENV R2PM_GITDIR=/home/appuser/.local/share/radare2/r2pm/git/

COPY entrypoint.sh "$SOURCE_ROOT/entrypoint.sh"
COPY scripts "$SOURCE_ROOT/scripts"

# Used by wrapper script
ENV R2_HOME="$INSTALL_PREFIX/bin"
ENV R2_SCRIPTS="$SOURCE_ROOT/scripts"

WORKDIR /home/appuser

ENTRYPOINT ["sh", "/radare2/entrypoint.sh"]
