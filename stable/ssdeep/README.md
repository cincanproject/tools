# Ssdeep - For computing context triggered piecewise hashes (CTPH), also called fuzzy hashes.

## Input

```
*
```

## Output

```
CTPH / Fuzzy hash
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*ssdeep/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/ssdeep))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/ssdeep/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/ssdeep
docker pull cincan/ssdeep
```

***3. Run the docker container***

Example 1. Generate hash:

`$ docker run --rm -v $(pwd):/input cincan/ssdeep /input/testfile`


Example 2. Compare files, using the cincan tool:  

`$ cincan run cincan/ssdeep -c file1 file2`



## Project homepage

[https://ssdeep-project.github.io/ssdeep/](https://ssdeep-project.github.io/ssdeep/)


## License  

GNU General Public License:  [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)
