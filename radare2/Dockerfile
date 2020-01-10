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
        # sudo


RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

# RUN install -d -o appuser -g appuser -m 770 /radare2/
RUN mkdir "$SOURCE_ROOT" \
    && chown -R appuser:appuser "$SOURCE_ROOT" \
    && chmod -R 775 "$SOURCE_ROOT"

# RUN wget --progress=bar:force -O "$INSTALL_ROOT"/radare2.zip "https://github.com/radareorg/radare2/archive/$VERSION.zip" \
#     && echo "$radare2_SHA256"  \
#     && sha256sum "$INSTALL_ROOT"/radare2.zip \
#     && echo "$radare2_SHA256  $INSTALL_ROOT/radare2.zip" | sha256sum -c - \
#     && unzip "$INSTALL_ROOT"/radare2.zip -d "$INSTALL_ROOT"

RUN git clone --depth 1 https://github.com/radareorg/radare2.git "$SOURCE_ROOT"

# WORKDIR "$INSTALL_ROOT/radare2-$VERSION/sys"

WORKDIR "$SOURCE_ROOT/sys"

# RUN sh user.sh --install-path "$INSTALL_ROOT" && make install

# Build portable binaries with meson
# RUN ./meson.py --dir "/$INSTALL_ROOT/build" --local

# RUN mkdir -p "${INSTALL_ROOT}/build/lib" && \
#     sh build.sh "$INSTALL_ROOT/build/" && make install

# RUN sh user.sh --install-path "$INSTALL_ROOT/build/" && make install

RUN meson --prefix="$INSTALL_PREFIX" && \
    ninja && \
    ninja install && \
    ln -s "$INSTALL_PREFIX/bin/radare2/" "$INSTALL_PREFIX/bin/r2/" && \
    su - appuser && \
    r2pm init && \
    r2pm update && \
    r2pm -i r2ghidra-dec && \
    rm -rf /usr/appuser/.local/share/radare2/r2pm/git/r2ghidra-dec.git


# RUN cp "$INSTALL_ROOT/binr/r2pm/r2pm" /usr/local/bin/ && \
#     # cp "$INSTALL_ROOT/radare2-$VERSION/binr/r2pm/r2pm" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/r2agent/r2agent" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/rabin2/rabin2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/radare2/radare2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/radiff2/radiff2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/rafind2/rafind2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/ragg2/ragg2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/rahash2/rahash2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/rarun2/rarun2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/rasm2/rasm2" /usr/local/bin/ && \
#     cp "$INSTALL_ROOT/build/binr/rax2/rax2" /usr/local/bin/ && \
#     ln -s /usr/local/bin/radare2 /usr/local/bin/r2 && \
#     # cp "$INSTALL_ROOT/radare2-$VERSION/binr/r2pm/r2pm" /usr/local/bin/
#     cp "$INSTALL_ROOT/binr/r2pm/r2pm" /usr/local/bin/ && \
#     mkdir -p /usr/include/libr/ && \
#     cp -a "$INSTALL_ROOT/build/libr/" /usr/include/


# ENV PATH="$INSTALL_ROOT"/bin:"$PATH"

# ENV Radare2_LIBRARIES "$INSTALL_ROOT"/build/libr
# RUN cp -RT /radare2/lib/ /usr/lib && cp -RT /radare2/include/ /usr/include && cp -RT /radare2/share/ /usr/share

# # RUN rm -rf /radare2/lib /radare2/include /radare2/share

# USER appuser

# RUN 

# USER root
# RUN		apk del --purge -r \
#         libc6-compat \
#         make \
#         ncurses-libs \
# 		npm \
#         cmake \
#         g++ \
#         gcc \
#         git \
#         linux-headers \
#         unzip \
#         wget \
#         curl \
#         git \
#         pkgconfig \
#         bison \
#         flex \
# 		&& rm -rf /tmp/* /var/cache/apk/* /var/tmp/* 

# # Script based packages

# RUN apk add --no-cache graphviz

# Folders for scripts

# SECOND STAGE

FROM alpine:edge AS runner

# ENV INSTALL_ROOT /radare2

# ENV VERSION 4.0.0
# ENV R2_PIPE_PY_VERSION=1.4.2

# # # Get liblarires and bins from builder
ENV DEST_PREFIX /usr/local

COPY --from=builder "$INSTALL_PREFIX" "$INSTALL_PREFIX"
COPY --from=builder /usr/appuser /usr/appuser
# COPY --from=builder "$INSTALL_ROOT/radare2-$VERSION/" "$INSTALL_ROOT/radare2-$VERSION/"
# COPY --from=builder "$INSTALL_ROOT/radare2-$VERSION/binr/" "$INSTALL_ROOT/radare2-$VERSION/binr"
# COPY --from=builder "$INSTALL_ROOT/radare2-$VERSION/libr/" "$INSTALL_ROOT/radare2-$VERSION/libr"
# COPY --from=builder "$INSTALL_ROOT"/bin/ "$INSTALL_ROOT"/bin
# COPY --from=builder "$INSTALL_ROOT"/lib/ /usr/lib
# COPY --from=builder "$INSTALL_ROOT"/include/ /usr/include
# COPY --from=builder "$INSTALL_ROOT"/share/ /usr/share

RUN mkdir -p /r2/samples && \
    mkdir -p /r2/results && \
    chown -R appuser:appuser /r2/results && \
    chown -R appuser:appuser /r2/samples/


USER appuser
# Optional r2dec r2frida

COPY entrypoint.sh "$SOURCE_ROOT"/entrypoint.sh
COPY scripts "$SOURCE_ROOT"/scripts


# RUN du -sh /radare2 && du -sh /home/appuser/.local/share/radare2/

# Used by wrapper script
ENV R2_HOME="$INSTALL_PREFIX"/bin
ENV R2_SCRIPTS="$SOURCE_ROOT"/scripts



# COPY --from=builder /home/appuser/.local/share/radare2/ /home/appuser/.local/share/radare2

# # Plugin manager configuration
# ENV R2PM_PLUGDIR=/home/appuser/.local/share/radare2/plugins
# ENV R2PM_BINDIR=/home/appuser/.local/share/radare2/prefix/bin
# ENV R2PM_DBDIR=/home/appuser/.local/share/radare2/r2pm/db
# ENV R2PM_GITDIR=/home/appuser/.local/share/radare2/r2pm/git/

# Remove .git directory
# RUN rm -rf /home/appuser/.local/share/radare2/r2pm/git/

# RUN addgroup -S appuser && \
#     adduser -s /sbin/nologin --disabled-password -G appuser appuser

# USER appuser

WORKDIR /home/appuser

USER root

# ENTRYPOINT ["sh", "/radare2/entrypoint.sh"]
