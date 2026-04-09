---
displayName: [==[For re-creating the "forPrefix"]==]
---

## For re-creating the "forPrefix"
```space-lua
--- priority: 10
schuit = schuit or {}
schuit.utilities = schuit.utilities or {}

-- based on createPageFromTemplate but return the string
local function returnPageFromTemplate(templatePage, vars)
  print("Using template: ", templatePage)
  print("With Vars:",vars)
  local tpl, fm = template.fromPage(templatePage)
  local initialText = ""
  if fm.frontmatter then
    initialText = "---\n"
      .. string.trim(template.new(fm.frontmatter)())
      .. "\n---\n"
  end
  return initialText .. tpl(vars)
end

-- Cache the last created page
forprefix_latest_page = ""

-- Create event handler for all page templates with a forPrefix key in frontmatter
for pt in query[[
    from index.tag "meta/template/page"
    where _.tag == "page" and _.forPrefix
    order by _.priority desc
  ]] do
  print("adding listener for:",pt.name)
  event.listen {
    name = "editor:pageCreating",
    run = function(e)
      print("pageCreating:",e.data.name)
      vars = schuit.utilities.getPageVars(e.data.name)
      if e.data.name:startsWith(pt.forPrefix) then
        forprefix_latest_page = e.data.name
        return {
          text = returnPageFromTemplate(pt.name, vars)
        }
      end
    end
  }
end
event.listen {
  name = "editor:pageLoaded",
  run = function(e)
    local nav_to = e.data[1]
    if nav_to == forprefix_latest_page then
      forprefix_latest_page = ""
      local page_text = editor.getText()
      local cursor_idx, _ = string.find(page_text, "|^|", 1, true)
      if cursor_idx then
        cursor_idx = cursor_idx - 1
        editor.replaceRange(cursor_idx, cursor_idx+3, "")
        editor.moveCursor(cursor_idx, true)
      end
    end
  end
}
```
