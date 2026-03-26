import pandas as pd
import mlflow 

data = [{'king':'saikiran', 'profession': 'datascientist', 'pay':'10000000'}]
df = pd.DataFrame(data)
df.to_csv("data/data.csv")

def f(a,b,op):
    if op == 'add':
        return a+b
    elif op == 'sub':
        return a-b
    elif op == 'mul':
        return a*b
    elif op == 'div':
        return a/b
    
if __name__ == "__main__":
     a =1
     b = 2
     op = 'add'
     with mlflow.start_run():
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param('op',op)
        mlflow.log_param('result',f(a,b,op))
     op = 'sub'
     with mlflow.start_run():
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param('op',op)
        mlflow.log_param('result',f(a,b,op))