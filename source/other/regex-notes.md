# Regex notes

## letter & digits
- `\D+`: Matching all non digits, then  grouping

# match any using `.`

## the `.` match all chars, except \r or \n
example:
regexp: `r".+"`

It will match anything as long as there is at least one character present. no empty string such ""
