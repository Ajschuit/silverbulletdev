---
displayName: Widgets
tags: meta/scripts
---

## Mentions widget override
```space-lua
-- priority: 9
widgets = widgets or {}

local mentionTemplate = template.new [==[
* [[${_.ref}]]: "${_.snippet}"
]==]

function widgets.linkedMentions(pageName)
 pageName = pageName or editor.getCurrentPage()
  if string.startsWith(pageName, 'Journal') then
    return nil
  end
  local linkedMentions = query[[
    from index.tag "link"
    where _.page != pageName and _.toPage == pageName
    order by page
  ]]
  if #linkedMentions > 0 then
    return widget.new {
      markdown = "# Linked Mentions\n"
        .. template.each(linkedMentions, mentionTemplate)
    }
  end
end
```

## Table of Contents override
```space-lua
-- priority: 9 -- overwrites the default one
widgets = widgets or {}

--function widgets.linkedMentions(pageName)
---- overwrites the default one
--end
--local oldtoc = widgets.toc
function widgets.toc(options)
  local pageName = editor.getCurrentPage()
  if string.startsWith(pageName, "Dashboard") then
    return
  elseif string.startsWith(pageName, "Journal/") then
    return
  elseif string.startsWith(pageName, "Templates/") then
    return
  end
  options = options or config.get("std.widgets.toc")
  options.minHeaders = options.minHeaders or 3
  local text = editor.getText()
  local pageName = editor.getCurrentPage()
  local parsedMarkdown = markdown.parseMarkdown(text)
  -- Collect all headers
  local headers = {}
  for topLevelChild in parsedMarkdown.children do
    if topLevelChild.type then
      local headerLevel = string.match(topLevelChild.type, "^ATXHeading(%d+)")
      if headerLevel then
        local text = ""
        table.remove(topLevelChild.children, 1)
        for child in topLevelChild.children do
          text = text .. string.trim(markdown.renderParseTree(child))
        end
        -- Strip link syntax to avoid nested brackets in TOC
        text = string.gsub(text, "%[%[(.-)%]%]", "%1")

        if text != "" then
          table.insert(headers, {
            name = text,
            pos = topLevelChild.from,
            level = tonumber(headerLevel)
          })
        end
      end
    end
  end
  if options.minHeaders and options.minHeaders > #headers then
    return widget.new{}
  end
  -- Find min level
  local minLevel = 6
  for _, header in ipairs(headers) do
    if header.level < minLevel then
      minLevel = header.level
    end
  end
  -- Build up html
  local html = "<details><summary>" .. (options.header or "Table of Contents") .. "</summary>"
  for _, header in ipairs(headers) do
    --print(header)
    if not(options.maxHeader and header.level > options.maxHeader or
           options.minLevel and header.level < options.minLevel) then
      html = html .. string.rep(" ", (header.level - minLevel) * 2) ..
         "* [[" .. pageName .. "@" .. header.pos .. "|" .. header.name .. "]]<br/>"
    end
  end
  html = html .. "</details>"
  
  return widget.new {
    html = html
  }
end
```
