---
displayName: "Add GPS location support"
tags: meta/scripts
---

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
