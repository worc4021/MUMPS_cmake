#!/bin/bash

# Record the environment variables before running the script
for var in $(compgen -v); do
    eval "before_$var=\"\$$var\""
done

# Run the script
LATEST_VERSION=$(ls -1 /opt/intel/oneapi/compiler/ | grep -v latest | sort | tail -1)
source /opt/intel/oneapi/compiler/"$LATEST_VERSION"/env/vars.sh

# Compare and echo the environment variables that are new or have changed
for var in $(compgen -v); do
    before_var="before_$var"
    if [[ "$var" != before_* ]] && [ "${!before_var}" != "${!var}" ]; then
        echo "$var=${!var}" >> "$GITHUB_ENV"
    fi
done

