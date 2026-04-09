## Main Styles
```space-style
/* priority: 15 */
.flexbuttons {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.flexbuttons>button{
  padding: 15px;
  min-width: 200px;
}

html{
  --editor-width: min(1400px,80%) !important;
  font-family: "Courier Prime", monospace;
  font-weight: 400;
  font-style: normal;
}
@media screen and (width <= 800px) {
  html{
    --editor-width: 100% !important;
  }
}
html[data-theme="dark"] {
  --root-background-color: #132525;
}
.courier-prime-regular {
  font-family: "Courier Prime", monospace;
  font-weight: 400;
  font-style: normal;
}

.courier-prime-bold {
  font-family: "Courier Prime", monospace;
  font-weight: 700;
  font-style: normal;
}

.courier-prime-regular-italic {
  font-family: "Courier Prime", monospace;
  font-weight: 400;
  font-style: italic;
}

.courier-prime-bold-italic {
  font-family: "Courier Prime", monospace;
  font-weight: 700;
  font-style: italic;
}
.sb-frontmatter.sb-line-frontmatter-outside:has(+ .sb-frontmatter) ~ .sb-frontmatter {
    display:none;
}
.cm-diagnosticText {
  color: maroon;
}
.sb-line-h1 > a.sb-hashtag{
  background-color: var(--editor-code-background-color);
  color: var(--editor-code-color);
  border: none;
}
.sb-line-h1 > a.sb-hashtag:hover,
.sb-line-h1 > a.sb-hashtag:focus{
  color: var(--editor-color);
  border: 1px, solid var(--top-color);
}
.sb-line-h1 > a.sb-hashtag{
  border: none;
}
.sb-h1.sb-hashtag-text{
  font-size: 0.6em;
}
```
