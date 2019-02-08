# USAGE
# 1. Create directory structure and then move bunch of samples to it
# mkdir ./r2/samples
# cp /path/to/samples/* ./r2/samples
# 2. Run the docker container
# docker run --rm -it -v /r2:/r2 cincan/r2-callgraph:0.1
# 3. List the results
# ls ./r2/results

FROM radare/radare2:latest

RUN apt-get update && apt-get install -y \
	graphviz \
     && rm -rf /var/lib/apt/lists/*

VOLUME ["/r2"]

ENTRYPOINT ["/r2/script/r2_callgraph.sh"]
