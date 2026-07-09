#!/usr/bin/env bash
# Rebuild public/ — the homepage plus every star, static, into the deploy tree.
# Each star pins the star-actually engine by git tag (see its pyproject.toml).
set -euo pipefail
cd "$(dirname "$0")"

rm -rf public
mkdir -p public
cp homepage/index.html homepage/style.css public/

for star in stars/*/; do
  name="$(basename "$star")"
  echo "→ building $name"
  ( cd "$star" && uv sync && uv run star-actually build )
  rm -rf "public/$name"
  cp -R "$star/dist" "public/$name"
done

echo "built public/: $(ls public)"
