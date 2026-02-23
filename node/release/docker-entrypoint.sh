#!/bin/sh
set -e

# If the first argument looks like a flag or a Node.js script, prepend node
if [ "${1#-}" != "${1}" ] || [ -f "${1}" ]; then
  set -- node "$@"
fi

exec "$@"
