# josm-validator-rules
Custom and MAYBE DANGEROUS validator rules. Targeted for use by advanced mappers. They may save you some typing. Review each suggestion and DO NOT mass edit without care.

Each rule file has an overpass query that represents the set of input data that it is specifically designed to work on. This helps reduce the chance of side effects but is not perfect.

Currently all rules are written targeting edits within the United States but they may be useful in other contexts.

![image](https://github.com/watmildon/josm-validator-rules/assets/118567155/57f90333-7455-41b8-859c-3b185b152696)

# Contributing
Happy to host rules and mapstyles here. Each rule file should have:

* Good descriptive file name
* Overpass query showing the data it expects to work well on including region boundary
* Rule that works at a very high but not infallable rate for that overpass query

The validator rules and map style syntax are documented [here](https://josm.openstreetmap.de/wiki/Help/Validator/MapCSSTagChecker) and [here](https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation).

If you are editing in VS Code and you'd like to get some syntax highlighting, one can be found [here](https://marketplace.visualstudio.com/items?itemName=whammo.mapcss-syntax).
