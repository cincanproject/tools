# A Steganography program - hide data (and extract) in various kinds of image- and audio-files.

## Input

```
JPEG, BMP, WAV, AU
```

## Output

```
JPEG, BMP, WAV, AU, steghide report
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*steghide/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/steghide))


## Usage


Get info about a picture with embedded data using docker command:

`docker run -v $(pwd):/data cincan/steghide info /data/picture.jpg -p passphrase`


Embed message to a picture using the cincan tool:

`cincan run cincan/steghide embed -cf picture.jpg -ef secret.txt -p passphrase`

Extract message:

`cincan run cincan/steghide:dev extract -sf picture.jpg -p passphrase`


## Project homepage

[http://steghide.sourceforge.net/](http://steghide.sourceforge.net/)


## LICENSE

[GNU General public license 3.0](https://www.gnu.org/licenses/gpl-3.0.html)
