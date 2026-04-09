---
name: "Library/ajschuit/shared-config"
tags: meta/library
files:
- templates/page/daily-journal.md
- templates-page-daily-journal.md
---

This is all config values for silverbullet that I want to share between my work space and personal space. This way, my "setup" can be the same between the two.

# Scripts 

## Journal page functions (WIP)
```space-lua
-- priority: 55
schuit = schuit or {}
schuit.journal = schuit.journal or {}

schuit.journal.parseJournalPageName = function(pagename)
  print("getting date from journal page ", pagename )
  journalCheck, jType, y, m, d = table.unpack(string.split(pagename,"/"))
  -- make sure we're actually checking a Journal page
  if journalCheck != "Journal" then
    error("This function only for validating/parsing Journal page names")
  end

  -- Parse the year for yearly pages
  if jType == "Year" then 
    if (y == nil or y:find("^%d%d%d%d$") == nil) then
      error("Yearly journal path detected, but no year detected for "..pagename)
    end
    -- Here we've got a Yearly Journal with a valid year. Do the thing. #TODO: update
    return {
      pageType = "Year",
      year = y
    }
  end
  -- parse the Year and Week for weekly
  if jType == "Week" then
    if (y == nil or y:find("^%d%d%d%d$") == nil) and (m == nil or m:find("^%d%d$") == nil) then
      error("Weekly journal path detected, but no year or week detected for "..pagename)
    end
    if (y == nil or y:find("^%d%d%d%d$") == nil) then
      error("Weekly journal path detected, but no year detected for "..pagename)
    end
    if (m == nil or m:find("^%d%d$") == nil) then
      error("Weekly journal path detected, but no week detected for "..pagename)
    end
    return {
      pageType = "Week",
      year = y,
      week = m 
    }
  end
  -- parse the year and month for monthly
  if jType == "Month" then
      if (y == nil or y:find("^%d%d%d%d$") == nil) and (m == nil or m:find("^%d%d$") == nil) then
        error("Monthly journal path detected, but no year or month detected for "..pageName)
      end
      if (y == nil or y:find("^%d%d%d%d$") == nil) then
        error("Monthly journal path detected, but no year detected for "..pageName)
      end
      if (m == nil or m:find("^%d%d$") == nil) then
        error("Monthly journal path detected, but no month detected for "..pageName)
      end
      return {
        pageType = "Week",
        year = y,
        month = m 
      }
  end
  if jType == "Day" then
    if (y == nil or y:find("^%d%d%d%d$") == nil) and (m == nil or m:find("^%d%d$") == nil) and (d == nil or d:find("^%d%d$") == nil) then
      error("Daily journal path detected, but no year, month, or day detected for "..pageName)
    end
    if (y == nil or y:find("^%d%d%d%d$") == nil) and (m == nil or m:find("^%d%d$") == nil) then
      error("Daily journal path detected, but no year or month detected for "..pageName)
    end
    if (y == nil or y:find("^%d%d%d%d$") == nil) and (d == nil or d:find("^%d%d$") == nil) then
      error("Daily journal path detected, but no year or day detected for "..pageName)
    end
    if (m == nil or m:find("^%d%d$") == nil) and (d == nil or d:find("^%d%d$") == nil) then
      error("Daily journal path detected, but no month or day detected for "..pageName)
    end
    if (y == nil or y:find("^%d%d%d%d$") == nil) then
      error("Daily journal path detected, but no year detected for "..pageName)
    end
    if (m == nil or m:find("^%d%d$") == nil) then
      error("Daily journal path detected, but no month detected for "..pageName)
    end
    if (d == nil or d:find("^%d%d$") == nil) then
      error("Daily journal path detected, but no day detected for "..pageName)
    end
    return {
      pageType = "Day",
      year = y,
      month = m ,
      day = d
    }
  end
  error("No matching journal type found for "..pageName)
end

schuit.journal.getVars = function(e)
  jDate = schuit.journal.parseJournalPageName(e)
  if jDate then
    if jDate.pageType == "Day" then
      --------------------------
      --------------------------
      -- Here we've got a Daily Journal with a valid year, month & day. Do the thing.
      currday = os.time({year=jDate.year,month=jDate.month,day=jDate.day})
      dayVals = os.date("*t", currday)
      prevday = os.date("%Y/%m/%d", os.time({year=y,month=m,day=d-1}))
      nextday = os.date("%Y/%m/%d", os.time({year=y,month=m,day=d+1}))    
      yearWeek = math.floor((dayVals.yday-(((dayVals.wday+5) % 7) + 1 )+10)/7)
      weekYear = dayVals.year
      if yearWeek == 0 then
        pYE = os.date("*t",os.time({year=dayVals.year-1,month=12,day=31}))
        yearWeek = math.floor((pYE.yday-(((pYE.wday+5) % 7) + 1)+10)/7)
        weekYear = pYE.year
      end
      prevweekday = ""
      nextweekday = ""
      if dayVals.wday <= 2 or dayVals.wday > 6 then
        prevfriday = os.date("%Y/%m/%d", os.time({year=y,month=m,day=d-3}))  
        prevweekday = "[[Journal/Day/" .. prevfriday .. "|Friday]] "
      end
      if dayVals.wday < 2 or dayVals.wday >= 6 then
        nextmonday = os.date("%Y/%m/%d", os.time({year=y,month=m,day=d+3}))  
        nextweekday = " [[Journal/Day/" .. nextmonday .. "|Monday]]"
      end

      nav =  prevweekday .. [==[ << [[Journal/Day/]==] .. prevday .. [==[|Yesterday]] || [[Journal/Year/]==] .. dayVals.year .. [==[|]==] .. dayVals.year .. [==[]] [[Journal/Month/]==] .. dayVals.year .. [==[/]==] .. dayVals.month .. [==[|]==] .. dayVals.month .. [==[]] [[Journal/Week/]==] .. weekYear .. [==[/]==] .. yearWeek .. [==[|W]==] .. yearWeek .. [==[]] || [[Journal/Day/]==] .. nextday .. [==[|Tomorrow]] >> ]==] .. nextweekday
      header = os.date("%A %b %d, %Y",currday)

      
      return {
          currday = currday,
          dayVals = dayVals,
          prevday = prevday,
          nextday = nextday,
          yearWeek = yearWeek,
          weekYear = weekYear,
          prevweekday = prevweekday,
          nextweekday = nextweekday,
          header = header,
          nav = nav
          }
        --------------------------
        --------------------------
      --elseif jDate.pageType == "Year" -- Need to implement these
      else
        error("No template implemented yet for " .. jDate.type)
      end
    else
      print("This should hopefully never be reached?")
    end
  end


--event.listen {
--    name = "editor:pageCreating",
--    run = function(e)
--      --print("pageCreating: ", e.data)
--      if e.data.name:startsWith("Journal/") then
--        --print("Journal pageCreating:",e.data.name)
--        print(schuit.templates)
--        return {
--          text = schuit.templates.journaltemplate(e.data.name)
--        }
--      end
--    end
--  }  
```


## Add GPS location support
```space-lua
-- priority: 40
function awaitCallback(fn)
  return js.new(js.window.Promise, fn)
end

function currentGpsCoords()
  local result = awaitCallback(function(resolve, reject)
    js.window.navigator.geolocation.getCurrentPosition(resolve, reject, { timeout = 3000 })
  end)
  local coords = result.coords
  return { lat = coords.latitude, lon = coords.longitude }
end

```


## Initial config set up
```space-lua
-- priority: 2
config.set({
  actionButtons = {
      {
        icon = "home",
        description = "Go to the home page",
        priority = 10,
        run = function()
          editor.invokeCommand "Navigate: Home"
        end
      }
   },
  smartQuotes = {
    enabled = false
  }
})
```

## Adding additional menu buttons
```space-lua
-- priority: 1
--actionButton.define(
--    {
--      icon="home",
--      priority=99,
--      description="Go to the home page",
--      run = function()
--        editor.invokeCommand "Navigate: Home"
--      end
--    }
--)
actionButton.define(    
    {
      icon="calendar",
      description="Go to today's journal page",
      run = function()
        --editor.invokeCommand  "Journal: Daily"
        editor.navigate("Journal/Day/" .. os.date("%Y/%m/%d") )
      end
    }
)
actionButton.define(
  {
      icon="book",
      description="Open Page",
      run = function()
        editor.invokeCommand "Navigate: Page Picker"
      end
    }
)
actionButton.define(
    {
      icon="terminal",
      description="Run Command",
      run = function()
        editor.invokeCommand "Open Command Palette"
      end
    }
)
actionButton.define(
    {
      icon="sidebar",
      description="Toggle Tree View",
      run = function()
        editor.invokeCommand "Tree View: Toggle"
      end
    }
)
actionButton.define(
    {
      icon="arrow-left",
      description="Go back",
      run = function()
        editor.invokeCommand "Navigate: Back in History"
      end,
      mobile=true
    }
)
actionButton.define(
    {
      icon="arrow-right",
      description="Go forward",
      run = function()
        editor.invokeCommand "Navigate: Forward in History"
      end,
      mobile=true
    }
)
```

## Utilties
```space-lua
-- priority: 11
schuit = schuit or {}
schuit.utilities = schuit.utilities or {}

schuit.utilities.getPageVars = function (pagename)
  if pagename:startsWith("Journal") then
    return schuit.journal.getVars(pagename)
  end
  
  -- nothing else
  return {}
end
```

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
## Tasklist snippet
```space-lua
-- priority: 9

schuit = schuit or {}
schuit.snippets = schuit.snippets or {}

schuit.snippets.tasklist = function()
  local pagename = editor.getCurrentPage()
  if pagename:startsWith("Journal") then
    local dateparts = schuit.journal.parseJournalPageName(pagename)
    if dateparts.year and dateparts.month and dateparts.day then
      local jDate = os.time({
          year=dateparts.year,
          month=dateparts.month, 
          day=dateparts.day
        })

      -- all fields:
      --|ref|tag|pos|toPos|range|name|text|page|state|done|priority|itags|type|links|ilinks|startdate|duedate|orig_ref|orig_tag|orig_name|orig_page|orig_pos|orig_toPos|orig_done|orig_startdate|orig_deadline|orig_itags|parent|orig_links|orig_ilinks|orig_priority|due|orig_state|orig_completedDate|orig_parent|deadline|orig_tags|orig_due|tags|orig_series|completed|
      q = query[[from t = index.tag "task" where not done and t.page:startsWith("Journal") and (not t.startdate or t.startdate<=pagename) limit 5 order by t.priority nulls last]]
      if #q then
        return q
      else
        return "no results"
      end
    end    
    
    return "parsed dateparts: " .. dateparts
  end
  return "default: " .. os.date("%Y/%m/%d")
end
```

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




# Styles

## Custom Admonitions
```space-style
/* priority: 10 */
.sb-admonition[admonition="today"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>');
  --admonition-color: green;
}

.sb-admonition[admonition="abstract"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-text" viewBox="0 0 16 16"><path d="M5 4a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1zm-.5 2.5A.5.5 0 0 1 5 6h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5M5 8a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1zm0 2a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1z"/><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1"/></svg>'); 
  --admonition-color: dodgerblue;
}
.sb-admonition[admonition="info"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-info-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/><path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0"/></svg>'); 
  --admonition-color: turquoise;
}

.sb-admonition[admonition="tip"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16"><path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16m0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15"/></svg>'); 
  --admonition-color: #00bfa5;
}

.sb-admonition[admonition="success"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16"><path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425z"/></svg>'); 
  --admonition-color: #00c853;
}

.sb-admonition[admonition="question"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-question-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286m1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94"/></svg>'); 
  --admonition-color: #64dd17;
}

.sb-admonition[admonition="failure"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/></svg>'); 
  --admonition-color: #ff5252;
}

.sb-admonition[admonition="bug"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bug" viewBox="0 0 16 16"><path d="M4.355.522a.5.5 0 0 1 .623.333l.291.956A5 5 0 0 1 8 1c1.007 0 1.946.298 2.731.811l.29-.956a.5.5 0 1 1 .957.29l-.41 1.352A5 5 0 0 1 13 6h.5a.5.5 0 0 0 .5-.5V5a.5.5 0 0 1 1 0v.5A1.5 1.5 0 0 1 13.5 7H13v1h1.5a.5.5 0 0 1 0 1H13v1h.5a1.5 1.5 0 0 1 1.5 1.5v.5a.5.5 0 1 1-1 0v-.5a.5.5 0 0 0-.5-.5H13a5 5 0 0 1-10 0h-.5a.5.5 0 0 0-.5.5v.5a.5.5 0 1 1-1 0v-.5A1.5 1.5 0 0 1 2.5 10H3V9H1.5a.5.5 0 0 1 0-1H3V7h-.5A1.5 1.5 0 0 1 1 5.5V5a.5.5 0 0 1 1 0v.5a.5.5 0 0 0 .5.5H3c0-1.364.547-2.601 1.432-3.503l-.41-1.352a.5.5 0 0 1 .333-.623M4 7v4a4 4 0 0 0 3.5 3.97V7zm4.5 0v7.97A4 4 0 0 0 12 11V7zM12 6a4 4 0 0 0-1.334-2.982A3.98 3.98 0 0 0 8 2a3.98 3.98 0 0 0-2.667 1.018A4 4 0 0 0 4 6z"/></svg>'); 
  --admonition-color: #f50057;
}

.sb-admonition[admonition="example"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-vector-pen" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M10.646.646a.5.5 0 0 1 .708 0l4 4a.5.5 0 0 1 0 .708l-1.902 1.902-.829 3.313a1.5 1.5 0 0 1-1.024 1.073L1.254 14.746 4.358 4.4A1.5 1.5 0 0 1 5.43 3.377l3.313-.828zm-1.8 2.908-3.173.793a.5.5 0 0 0-.358.342l-2.57 8.565 8.567-2.57a.5.5 0 0 0 .34-.357l.794-3.174-3.6-3.6z"/><path fill-rule="evenodd" d="M2.832 13.228 8 9a1 1 0 1 0-1-1l-4.228 5.168-.026.086z"/></svg>'); 
  --admonition-color: #7c4dff;
}

.sb-admonition[admonition="quote"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-quote" viewBox="0 0 16 16"><path d="M12 12a1 1 0 0 0 1-1V8.558a1 1 0 0 0-1-1h-1.388q0-.527.062-1.054.093-.558.31-.992t.559-.683q.34-.279.868-.279V3q-.868 0-1.52.372a3.3 3.3 0 0 0-1.085.992 4.9 4.9 0 0 0-.62 1.458A7.7 7.7 0 0 0 9 7.558V11a1 1 0 0 0 1 1zm-6 0a1 1 0 0 0 1-1V8.558a1 1 0 0 0-1-1H4.612q0-.527.062-1.054.094-.558.31-.992.217-.434.559-.683.34-.279.868-.279V3q-.868 0-1.52.372a3.3 3.3 0 0 0-1.085.992 4.9 4.9 0 0 0-.62 1.458A7.7 7.7 0 0 0 3 7.558V11a1 1 0 0 0 1 1z"/></svg>'); 
  --admonition-color: #9e9e9e;
}

.sb-admonition[admonition="danger"] {
  .sb-admonition-type * { display: none; }
  --admonition-icon: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightning-fill" viewBox="0 0 16 16"><path d="M5.52.359A.5.5 0 0 1 6 0h4a.5.5 0 0 1 .474.658L8.694 6H12.5a.5.5 0 0 1 .395.807l-7 9a.5.5 0 0 1-.873-.454L6.823 9.5H3.5a.5.5 0 0 1-.48-.641z"/></svg>'); 
  --admonition-color: #ff1744;
}
```

## '@import's
```space-style
/* priority: 1000 */
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&display=swap');
```

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


