---
displayName: "Journal page functions"
status: "WIP"
blurb: "This script creates a a bunch of functions that help with things I do frequently in my Journal pages."
tags: meta/scripts
---

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
