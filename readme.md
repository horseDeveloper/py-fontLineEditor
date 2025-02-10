# Script info
## Script summary:
1) This script can search for 'namerecord nameID' and/or 'target index'. 
2) After the first match, line by line, you can (keep/delete/edit) the line.

## Script notes
### Why edit here? 
Fonts can be very big and Notepad does not handle scrolling/editing very well.
    
### Why edit `namerecord`? 
So that your custom font has the appropriate `Copyright/Author/...`

 ### Why remove lines after a certain `lookup index`? 
So you can freeze just the alternative features (glyphs) you want and remove the other substitutions of the (lookup index) set.

# WorkFlows using this code
## WF01: 
.ttf => .ttx ;; py-fontLineEditor ;; .ttx ⇒ .ttf ;; (pyftfeatfreeze)

# Status check
```
✅ Script working on Python 3.11.2 as of 2025-02-05. 
🛑EDIT_HERE🛑 occurrences: 0
```

# Copyright
Line finder and editor for big .ttx files.

Copyright (C) 2025 Nicolò Arrigo

SPDX-License-Identifier: AGPL-3.0-only

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
