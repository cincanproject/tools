# ADD2GIT-LFS

# GUI service for CinCan pipelines



## Supported tags and respective `Dockerfile` links

* `latest` ([*add2git-lfs/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/add2git-lfs))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/add2git-lfs/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/add2git-lfs
docker pull cincan/add2git-lfs
```

***3. Run the docker container***


Example:  


`$ docker run --rm -v $(pwd):/samples --net build_cincan --ip 172.20.0.7 -p 12358:12358 cincan/add2git-fs -branch pdf-source -folder .`  



***Options***
```  

Usage of /add2git-lfs/add2git-lfs:
  -branch string
    	branch (default "master")
  -email string
    	user.email for commit
  -folder string
    	folder to upload (default "sample-files")
  -remote string
    	remote (default "origin")
  -token string
    	personal access token (https)
  -user string
    	user.name for commit
```


## Project homepage

[https://github.com/saguywalker/add2git-lfs](https://github.com/saguywalker/add2git-lfs)
