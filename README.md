# star-actually — production

The public home of **`*, Actually`** and the built star sites. This repo is what
Cloudflare Pages serves.

## Layout

```
public/            ← the deployable static site — Pages serves this (committed)
  index.html         the project homepage
  ssh-actually/      SSH, Actually
  ho-actually/       Ho System, Actually
homepage/          ← homepage source (index.html + style.css)
stars/             ← the content of each star (nodes/ + site.yaml); the engine builds these
build.sh           ← rebuild public/ from source
```

## Deploy

Push. Point Cloudflare Pages at this repo with **output directory `public/`** and
**no build command**. It's static — just files. Done.

## Rebuild

The build engine is the domain-blind
[`star-actually`](https://github.com/sageframe-no-kaji/star-actually) package. Each
star declares its `base_path` in `site.yaml` (e.g. `/ssh-actually`) so its links
work under the subfolder. Run:

```
./build.sh
```

It builds the homepage and every star into `public/`. The LLM receptionist is
deferred — everything here is static.
