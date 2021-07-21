# MVT - Mobile Verification Toolkit by Amnesty

"Mobile Verification Toolkit (MVT) is a collection of utilities to simplify and automate the process of gathering forensic traces helpful to identify a potential compromise of Android and iOS devices."

Full documentation is available in [here.](https://mvt.readthedocs.io/en/latest/index.html)

## Input

```
Android backup, Android filesystem dump, Android device with adb
iTunes/Finder backup, iOS filesystem dump
```

## Output

```
JSON, text
```

## Example usage

Commands `mvt-ios` and `mvt-android` have been provided with wrapper script.

For example, use with Docker for iOS filesystem dump:

```
docker run -v /dump:/dump quay.io/cincan/mvt mvt-ios check-fs /dump
```

***Method 2. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. 

To get same functionality as above, simply run

```console
cincan run cincan/mvt mvt-ios check-fs /dump
```


## License

MVT is released under an adaptation of Mozilla Public License v2.0. This modified license includes a new clause 3.0, "Consensual Use Restriction" which permits the use of the licensed software (and any "Larger Work" derived from it) exclusively with the explicit consent of the person/s whose data is being extracted and/or analysed ("Data Owner").

## Project Home

Tool is developed on https://github.com/mvt-project/mvt
