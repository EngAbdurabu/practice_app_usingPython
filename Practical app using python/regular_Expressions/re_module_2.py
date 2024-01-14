import re
# sub:  use to replace string by other string
text = "I am Abudrabu Mohammed , I am  Engineer "
replace = re.sub(r"\s", "-", text, 3)
print(replace)
print("----------------------------------------")
# --------------------------------------------------------------
# split: use to divide the string depend on  the regular expressions
new_text = re.split(r"\s", text, 3)
print(new_text)
print("----------------------------------------")
# ---------------------------------------------------------------
# test
link = "استبدال-وتقطيع-النصوص-عبر-دوال-الوحدة"
replace = re.sub(r"-", " ", link)
print(replace)
