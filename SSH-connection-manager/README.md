Stores SSH connections so that you can easily connect to them, allows removing previous connections or add new ones.

---
### Requirements
You need to install the `simple_term_menu` package :
```
pip3 install simple_term_menu
```
In the same directory as the script create two txt files called `labels.txt` and `connections.txt`, finally update the exact paths to the files so that you can execute the script from any location.

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