Triggers for data cleansing
1.
Lat, Long not null, not "-1"
DISTRICT not null
DANGER not null
2.
distinct "CODE" in "offense_codes.csv", keep the one with a longer "NAME"
3.
change [Monday, Tuesday,...,Sunday] into [1:1:7]
4.
natual join MLdata M, offense_codes O where M.OFFENSE_CODE = O.CODE
5.
DISTRICT [A1,A15,A7,B2,B3,C11,C6,D14,D4,E13,E18,E5]into [1,12]
6.
if shooting = "T" then new.DANGER = "3"
