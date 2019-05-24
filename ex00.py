class CSV:
    def __init__(self,filename,postfix,is_head,path):
        self.filename=filename
        self.postfix=postfix
        self.is_head=is_head
        self.path=path

    def is_csv(self):
         import os.path
         name=os.path.splitext(self.path)[1]
         if name==".csv":
             return True
         else:
             return False

    def is_head(self):
        csvfile=open(self.filename,'r')
        a=csvfile.read()
        global arr
        arr=a.split()
        b=arr[0]
        n=["Name","Age","No"]
        if len(a and n) > 0:
            return True
        else:
            return False

    def read(self):
        if self.is_csv:
            if self.is_head:
                global arr
                for a in arr:
                    print(t)
            else:
                print("只能处理带头部文件")
        else:
            print("只能处理.csv后缀文件")

csv=CSV("ex0_sample.csv","csv",True,"C:/Users/ASUS/ex0_sample.csv")
csv.read()
