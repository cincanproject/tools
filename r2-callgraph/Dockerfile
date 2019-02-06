# usage: cp interesting.exe /mydir/binary;
#        docker run --rm -it -v /mydir:/io <imagename>
#        ls /mydir/output.dot

FROM radare/radare2:latest
ENTRYPOINT r2 -c 'aa; agCd > /io/output.dot' /io/binary < /dev/null
