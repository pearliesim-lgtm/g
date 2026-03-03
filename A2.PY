class person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)

class emp(person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,id)

obj=emp('disha',1652,600,"office Employee")
obj.display()
print(obj.salary)
print(obj.post)