---
suggestedName: 'Journal/Day/${os.date("%Y/%m/%d")}'
confirmName: false
openIfExists: true
displayName: "My Daily Journal"
description: "My daily journal template"
forPrefix: "Journal/Day/"
tags: "meta/template/page"
command: "Journal: Daily"
key: "Alt-Shift-d"
frontmatter: |
 tags: "journal daily"
 body:
  sleep:
  emotion:
  weight:
 habit:
  medication:
   adderall: 
   multivitamin:
   vitamin-d:
   allertec:
  breakfast: 
  lunch: 
  dinner: 
  steps: 0
 description: ""
---

${nav or ""}
# ${header or "No value provided for header"}

${"$"}{schuit.snippets.tasklist()}
 
# Today's log
- Journal page created ${os.date("%I:%M %p")} #meta
- |^|






[[^Library/schuit/templates/page/Daily Journal|¤]]
