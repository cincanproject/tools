#!/bin/sh
# Create a list of available tools using tools' README files,
# and add to README.md

touch temp-windows.md temp-linux.md

find . -mindepth 1 -maxdepth 1 -type d 2>/dev/null |while read -r output; do
	TOOL_NAME="$(echo "${output}" | sed 's/.\///; s/\///')"

	# Add to list if a Dockerfile exists
	if [ -f "$TOOL_NAME"/Dockerfile ]
	then
		if [ -f "$TOOL_NAME"/README.md ]
		then
			DESCRIPTION="$(head -n 1 "$TOOL_NAME"/README.md | sed 's/#//g; s/\"//g';)"
			INPUTS="$(sed -e '1,/Input/d;/Output/,$d;1,/```/d;/```/,$d;' "$TOOL_NAME"/README.md \
				|tr '\n' ' ')"
		else
			DESCRIPTION=""
			INPUTS=""
		fi

		# Sort tools by OS
		if grep -q "windowsservercore" "$TOOL_NAME/Dockerfile"
		then
			echo "| $TOOL_NAME |  $DESCRIPTION | $INPUTS | Windows |" >> temp-windows.md
		else
			echo "| $TOOL_NAME |  $DESCRIPTION | $INPUTS | Linux |" >> temp-linux.md
		fi
	fi
done

# Cut off the old list of tools
sed -i '/## Description*/q' README.md

# Combine tools list from temp-linux and temp-windows files to README.md
cat >> README.md << EOL
### Linux tools

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
EOL

# Sort list by Input column
sort -t "|" -rk4,4 temp-linux.md >> README.md
rm temp-linux.md

cat >> README.md << EOL
### Windows tools

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
EOL

# Sort list by Input column
sort -t "|" -rk4,4 temp-windows.md >> README.md
rm temp-windows.md
