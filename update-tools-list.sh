#!/bin/sh
# Create a list of available tools using tools' README files,
# and add to README.md
STABLE_DIR="stable"
DEV_DIR="development"
UNMAINTAINED_DIR="unmaintained"
FILENAME="README.md"


write_tools_on_dir() {

find "$1" -mindepth 1 -maxdepth 1 -type d 2>/dev/null |while read -r TOOL_PATH; do
	TOOL_NAME="$(echo "${TOOL_PATH}" | sed 's:.*/::')"
	echo "$TOOL_NAME"
	# Add to list if a Dockerfile exists
	if [ -f "$TOOL_PATH"/Dockerfile ]
	then
		if [ -f "$TOOL_PATH"/README.md ]
		then
			DESCRIPTION="$(head -n 1 "$TOOL_PATH"/README.md | sed 's/#//g; s/\"//g';)"
			INPUTS="$(sed -e '1,/Input/d;/Output/,$d;1,/```/d;/```/,$d;' "$TOOL_PATH"/README.md \
				|tr '\n' ' ')"
		else
			DESCRIPTION=""
			INPUTS=""
		fi

        echo "| [$TOOL_NAME](https://gitlab.com/CinCan/tools/-/tree/master/$TOOL_PATH) | $DESCRIPTION | $INPUTS | Linux |" >> "$2"
	fi
done
}

touch temp-stable.md temp-dev.md temp-unmaintained.md temp-linux.md

# Stable tools at first
write_tools_on_dir "$STABLE_DIR" "temp-stable.md"

cat >> temp-linux.md << EOL
### Linux tools

### Stable

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
EOL

# Sort list by Input column
sort -t "|" -k2,2 temp-stable.md >> temp-linux.md

# Development tools
write_tools_on_dir "$DEV_DIR" "temp-dev.md"

cat >> temp-linux.md << EOL
### In Development

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
EOL
sort -t "|" -k2,2 temp-dev.md >> temp-linux.md

# Unmaintained tools
write_tools_on_dir "$UNMAINTAINED_DIR" "temp-unmaintained.md"

cat >> temp-linux.md << EOL
### Not maintained anymore

It is very possible that some of these are not working.

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
EOL
sort -t "|" -k2,2 temp-unmaintained.md >> temp-linux.md


# Cut off the old list of tools
sed -i '/## Description*/q' "$FILENAME"
cat temp-linux.md >> "$FILENAME"

rm temp-linux.md temp-stable.md temp-dev.md temp-unmaintained.md