# File related scripts

## rename.py
### usage
<kbd>rename</kbd> <kbd>directory</kbd> <kbd>number-prefix</kbd> <kbd>execute-flag</kbd>

Renames files in a directory which have a numeric extension in the filename.
The <kbd>filename1.json</kbd> will be renamed into <kbd>filename number-prefix-1.json</kbd>

Example:
rename /a/b/miwelcome/deploy/pona/data/communication_method_email 1 1

- this call will add 1- to the filename
- filename before: communication_method_email1.json
- filename after:  communication_method_email1-1.json

