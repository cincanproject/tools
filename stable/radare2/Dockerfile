ARG tool_version=5.3.1
# use commit for while (pre 5.4.0, huge submodule removed)
ARG ghidra_tool_version=55ecb8666ecb8405d962871215c6f9731360e5a5

# Version number is used in r2ghidra plugin as well for selecting correct tag

FROM alpine:latest AS builder

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

ARG ghidra_tool_version
ENV GHIDRA_TOOL_VERSION=$ghidra_tool_version

ENV radare2_SHA256 3be923f7d67f7a800fada59d035b1caad46c3b206ea87b0c02ae273f2c7305dd

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

USER appuser

RUN wget --progress=bar:force -O "$SOURCE_ROOT"/radare2.zip "https://github.com/radareorg/radare2/archive/$TOOL_VERSION.zip" \
    && echo "$radare2_SHA256"  \
    && sha256sum "$SOURCE_ROOT"/radare2.zip \
    && echo "$radare2_SHA256  $SOURCE_ROOT/radare2.zip" | sha256sum -c - \
    && unzip "$SOURCE_ROOT"/radare2.zip -d "$SOURCE_ROOT"

RUN cd "$SOURCE_ROOT/radare2-$TOOL_VERSION/sys" && \
    meson --prefix="$INSTALL_PREFIX" && \
    ninja && \
    ninja install

USER root
RUN apk add patch
USER appuser

RUN git clone  https://github.com/radareorg/r2ghidra ~/.local/share/radare2/r2pm/git/r2ghidra && \
    cd ~/.local/share/radare2/r2pm/git/r2ghidra && \
    git checkout "$GHIDRA_TOOL_VERSION" && \
#     # git submodule init && \
    git submodule update --init
#     make ghidra/ghidra/Ghidra && \
#     mkdir build && cd build && \
#     cmake -DCMAKE_INSTALL_PREFIX=~/.local .. && \
#     make && \
#     make install

RUN r2pm init && \
    r2pm update && \
    r2pm -ci r2ghidra && \
    r2pm cache && \
    rm -rf /home/appuser/.local/share/radare2/r2pm/git/r2ghidra && \
    # Disable r2agent - no use in container
    rm /usr/local/bin/r2agent

# SECOND STAGE

FROM alpine:latest AS runner

ARG tool_version
ENV TOOL_VERSION=$tool_version

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

# Get libarires and bins from builder

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

# Copy .cincanignore file - these files are never downloaded into host
COPY .cincanignore /home/appuser/.cincanignore

# Used by wrapper script
ENV R2_HOME="$INSTALL_PREFIX/bin"
ENV R2_SCRIPTS="$SOURCE_ROOT/scripts"

WORKDIR /home/appuser
COPY meta.json /opt/
ENTRYPOINT ["sh", "/radare2/entrypoint.sh"]
