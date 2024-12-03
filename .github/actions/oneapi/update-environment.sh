#!/bin/bash

# Record the environment variables before running the script
for var in $(compgen -v); do
    eval "before_$var=\"\$$var\""
done

# Run the script
source /opt/intel/oneapi/setvars.sh

# Compare and echo the environment variables that are new or have changed
for var in $(compgen -v); do
    before_var="before_$var"
    if [[ "$var" != before_* ]] && [ "${!before_var}" != "${!var}" ]; then
        echo "$var=${!var}" >> "$GITHUB_ENV"
    fi
done

