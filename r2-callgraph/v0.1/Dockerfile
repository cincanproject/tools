# USAGE
# 1. Clone the repository
# git clone https://gitlab.com/CinCan/dockerfiles
# cd dockerfiles/r2-callgraph/v0.1/
# 2. Build the docker image
# docker build . -t r2-callgraph:0.1
# 3. Create directory and add samples to it
# mkdir ./samples
# cp /path/to/samples/* ./samples
# 4. Run the docker container
# docker run --rm -it -v $(pwd):/r2 cincan/r2-callgraph:0.1
# 3. List the results
# ls ./results

FROM radare/radare2:latest

RUN apt-get update && apt-get install -y \
	graphviz \
     && rm -rf /var/lib/apt/lists/*

VOLUME ["/r2"]

ENTRYPOINT ["/r2/script/r2_callgraph.sh"]
