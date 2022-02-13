Stores SSH connections so that you can easily connect to them, allows removing previous connections or add new ones.

---
### Requirements
You need to install the `simple_term_menu` and `pathlib` package :
```
pip3 install simple_term_menu
pip3 install pathlib
```
In the beggining of the file update `json_path` to the place where you want the json file to be stored
<br >*Note: The path needs to end in conn_data.json in order to work.*
### Example

```
Koce@ ~:python3 sshcon.py
SSH Connection Manager ver 2.0
Please select a desired connection:
> Beating Light
  MushyMyce
  Oktks
  Add New
  Remove connection
  
Connecting to "Beating Light"...
Koce@gnld****.siteground.biz in ~:
```
