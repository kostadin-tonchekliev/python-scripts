Stores SSH connections so that you can easily connect to them, allows removing previous connections or add new ones.

---
### Requirements
You need to install the `simple_term_menu` and `pathlib` package :
```
pip3 install simple_term_menu
pip3 install pathlib
```
In the beggining of the file update `connections_path` and `labels_path` to the path where you want the files to be stored.
<br >*Note: Both paths need to end in the respective file, for example connections.txt and etc.*
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