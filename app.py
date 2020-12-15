import pyjsondb as p
p.init("Hello")

data = p.Table("kjickqe")
data.set_fields(["name", "age"])

data.add(["hello", 17])
data.add(["hello", 18])
data.add(["hello", 17])


dd = data.filter_by({"age" : 17})

data.delete(dd[0])
print(dd)
