---
title: "My Quartz 4.0 Cliff Notes"
---

## Quartz 4.0 - Documentation Snippets & Notes

Disclaimer: these notes are just some of my snippets and are not intended, in any way, to substitute for the actual project documentation!

## Run the dev server

```npx quartz build --serve```

The server runs on port 8080.

## Supported frontmatter fields

- `title`: Title of the page. If it isn't provided, Quartz will use the name of the file as the title.
- `description`: Description of the page used for link previews.
- `permalink`: A custom URL for the page that will remain constant even if the path to the file changes.
- `aliases`: Other names for this note. This is a list of strings.
- `tags`: Tags for this note.
- `draft`: Whether to publish the page or not. This is one way to make [[private pages|pages private]] in Quartz.
- `date`: A string representing the day the note was published. Normally uses `YYYY-MM-DD` format.

## The main config file

It's called

`quartz.config.ts`

An example of where the fonts are configured:

```

    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Lato",
        code: "IBM Plex Mono",
      },
      color
```