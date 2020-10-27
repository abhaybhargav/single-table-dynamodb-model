# Single Table Model - Version Managed Dataset with DynamoDB

## Attributes

* image_name => string
* image_id => int
* configuration => string
* created_on => int

## Access Patterns

### Select - Querying the DB

* Get the latest version of a given image name => pk("image"), sk("v0#app-abc")
* Get the list of all image names in the system => pk("image"), sk.begins_with("v0#")
* Get an existing image by name => pk("image"), sk("v2#app-abc")

### Prototype

[Model Prototype - Google Sheets](https://docs.google.com/spreadsheets/d/1JhhLbVnZ5_JzqjfkB8KWX90-2HklK2R_csSnHpI5vZI/edit?usp=sharing)