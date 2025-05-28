class Method_Variables:
    a=10   #STATIC VARIABLE
    def __init__(self,x):    #CONSTRUCTOR
        print("This is constructor method ")
        self.x=x     #INSTANCE VARIABLE
    def instance_method(self):
        print("This is instance method ")
        print("Static variable is :",self.a)
        print("Instance variable is :",self.x)
        d="AD"#LOCAL VARIABLE
        print("Local variable is : ",d)
    @classmethod
    def class_method(cls):
        print("This is class level method")
        print("Static variable is :",cls.a)
        d="MO"
        print("Local variable is : ",d)
    @staticmethod
    def static_method():
        print("This is static method ")
        d="ADMO"
        print("Local variable is : ",d)
m=Method_Variables("1223")
m.instance_method()
m.class_method()
m.static_method()