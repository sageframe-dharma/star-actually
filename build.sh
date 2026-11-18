#!/usr/bin/env bash
# Rebuild public/ — the homepage plus every star, static, into the deploy tree.
# Each star pins the star-actually engine by git tag (see its pyproject.toml).
set -euo pipefail
cd "$(dirname "$0")"

rm -rf public
mkdir -p public
cp homepage/index.html homepage/style.css public/

# Each star resolves the engine from the tag pinned in its own pyproject.toml,
# NOT from any local working tree. A star left on a stale pin builds a stale
# site silently — which is exactly how engine v0.5.0's chain index sat unbuilt
# for four months. So every build announces the version it actually resolved;
# a pin that has fallen behind is then visible here instead of invisible. The
# same string ships as engine-version.txt so the LIVE site can be checked too.
for star in stars/*/; do
  name="$(basename "$star")"
  echo "→ building $name"
  ( cd "$star" && uv sync && uv run star-actually build )
  engine="$( cd "$star" && uv run python -c \
    'from importlib.metadata import version; print(version("star-actually"))' )"
  echo "  engine: v$engine"
  rm -rf "public/$name"
  cp -R "$star/dist" "public/$name"
  echo "$engine" > "public/$name/engine-version.txt"
done

echo "built public/: $(ls public)"
