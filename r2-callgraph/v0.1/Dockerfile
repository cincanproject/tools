FROM radare/radare2:latest

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
	graphviz \
     && rm -rf /var/lib/apt/lists/*

VOLUME ["/r2"]

ENTRYPOINT ["/r2/script/r2_callgraph.sh"]
