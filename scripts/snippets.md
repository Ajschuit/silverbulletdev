---
displayName: Snippets
---
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
