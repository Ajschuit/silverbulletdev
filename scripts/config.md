---
displayName: "Shared config"
---


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
