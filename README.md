## PyJsonDB

![img](https://github.com/pranavbaburaj/pyjsondb/blob/main/logo.png)

### **How to use it?**
```python
import pyjsondb as db

db.init("database")
```
*Create a table*

```python
table = db.Table("table_name")

# set the different fields
table.set_fields(["name", "age", "etc"])
```
*adding item*

```python

table.add(["pyjsondb", 13, "python"])
```

*Remove item*

```python
table.remove_by_id(1)

# filtering
delete_item = table.filter_by({"age" : 13})
table.delete(delete_item)
```
