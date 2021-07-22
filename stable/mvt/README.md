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
JSON, text, .apk
```

## Example usage

Commands `mvt-ios` and `mvt-android` have been provided with wrapper script.

***Method 1. use Docker CLI***

Example use with Docker for iOS filesystem dump:

```
docker run -v /dump:/dump quay.io/cincan/mvt mvt-ios check-fs /dump
```

Example use with ADB bridge for Android devices.
Device is shared into the container with `--device` parameter.
JSON output stored into shared volume `/dump`.

```
docker run --device /dev/bus/usb -v /dump:/dump quay.io/cincan/mvt mvt-android check-adb -o /dump
```

***Method 2. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. 

To analyse filesystem dump

```
cincan run cincan/mvt mvt-ios check-fs /dump
```

ADB is not currently supported with `cincan` tool. Device cannot be shared into container.

## License

MVT is released under an adaptation of Mozilla Public License v2.0. This modified license includes a new clause 3.0, "Consensual Use Restriction" which permits the use of the licensed software (and any "Larger Work" derived from it) exclusively with the explicit consent of the person/s whose data is being extracted and/or analysed ("Data Owner").

## Project Home

Tool is developed on https://github.com/mvt-project/mvt
