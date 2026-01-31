# Reading Guide Webfont Usage

## Quick Start

1. Copy `ReadingGuide-Regular.woff2` and `ReadingGuide-Regular.woff` to your project
2. Add the CSS below to your stylesheet
3. Apply the font-family to your elements

## CSS

```css
@font-face {
  font-family: "ReadingGuide";
  src:
    url("./ReadingGuide-Regular.woff2") format("woff2"),
    url("./ReadingGuide-Regular.woff") format("woff");
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: "ReadingGuide", Georgia, "Times New Roman", serif;
}
```

## Minimal HTML Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reading Guide Font Demo</title>
  <style>
    @font-face {
      font-family: "ReadingGuide";
      src:
        url("./ReadingGuide-Regular.woff2") format("woff2"),
        url("./ReadingGuide-Regular.woff") format("woff");
      font-weight: normal;
      font-style: normal;
      font-display: swap;
    }
    body {
      font-family: "ReadingGuide", Georgia, "Times New Roman", serif;
      font-size: 18px;
      line-height: 1.6;
      max-width: 65ch;
      margin: 2rem auto;
      padding: 0 1rem;
    }
  </style>
</head>
<body>
  <h1>Reading Guide Font</h1>
  <p>This text is rendered using the Reading Guide webfont.</p>
</body>
</html>
```

## Testing Locally

```bash
# From the web-example directory
python3 -m http.server 8000
# Open http://localhost:8000
```

## Performance Tips

Add a preload hint in your HTML `<head>` for faster font loading:

```html
<link rel="preload"
      href="./ReadingGuide-Regular.woff2"
      as="font"
      type="font/woff2"
      crossorigin>
```
