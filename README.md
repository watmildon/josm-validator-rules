# josm-validator-rules
Custom and maybe dangerous validator rules


## Overpass query for validator
Here's an overpass query for all of the name suffixes the validator knows to look for. You'll want to change the search area to something more managable ex: "Oregon, United States".
```
[out:json][timeout:300];
{{geocodeArea:"Washington State,United States of America"}}->.a;
(
  wr[highway][highway!=platform][amenity=shelter][!bus][name~" Arc$| Av$| Ave$| Blf$| Blvd$| Bnd$| Br$| Brg$| Byp$| Cir$| Cres$| Cswy$| Ct$| Ctr$| Cv$| Dr$| Expy$| Expwy$| Flds$| Fmrd$| Fwy$| Gd$| Grv$| Hbr$| Holw$| Hw$| Hwy$| Ln$| Lndg$| Lp$| Mal$| Mtwy$| Ovps$| Pky$| Pkwy$| Pl$| Plz$| Rd$| Rdg$| Rmrd$| Rte$| Skwy$| Sq$| St$| Ter$| Tfwy$| Thfr$| Thwy$| Tl$| Tpke$| Trce$| Trl$| Tunl$| Unp$| Vw$| Wkwy$| Wy$| Xing$"](area.a);
);
out body;
>;
out skel qt;
```
