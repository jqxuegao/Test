class People():
    # 构造方法
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(People):
    # 继承People构造方法，并构造一个新的变量achievement
    def __init__(self,name,age,achievement):
        People.__init__(self,name,age)
        self.achievement = achievement

class Skill():
    # 构造方法
    def __init__(self,haveSkill):
        self.haveSkill = haveSkill

class Worker(Student,Skill):
    # 继承student构造方法（包括people类的构造方法），并构造一个新的变量haveSkill
    def __init__(self,name,age,achievement,haveSkill):
        Student.__init__(self,name,age,achievement)
        Skill.__init__(self,haveSkill)
    # 新建一个方法，去验证上面继承有没有作用
    def test(self):
        print('姓名，年龄，成绩，技能：',self.name,self.age,self.achievement,self.haveSkill)

# 实例化，并传所需参数
test = Worker('陈建齐','27','100','学习py')
# 调用类中方法
test.test()
