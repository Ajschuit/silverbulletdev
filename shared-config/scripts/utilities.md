---
displayName: Utilities
tags: meta/scripts
---

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
