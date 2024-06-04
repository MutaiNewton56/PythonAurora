import time

def time_decorator(func):
    def wrapper():
        start_time=time.time() 
        func()
        end_time=time.time()
        diff_time=end_time-start_time
        print(f"Func took {diff_time}")
    return wrapper

def to10():
    for i in range(10):
        print(f"i is {i} ")
        
@time_decorator
def to1000():
    for i in range(1000):
        print(f"i is {i} ")

def to100000():
    for i in range(10000):
        print(f"i is {i} ")

@time_decorator
def to1000000():
    for i in range(1000000):
        print(f"i is {i} ")

to1000000()
# start_time=time.time() 
# to1000000()
# end_time=time.time()
# diff_time=end_time-start_time
# print(f"Func took {diff_time}")



# 1. Project Discovery. <All the members get aquated to what you are doing>.
# 2. Project Documentation. <What we are building, We are building this product>
####### MVP <Minimum Viable Product> 
####### User Stories. <Who are you building this product for?. Juarney>
# 3.DB Design
# 4. UI UX DESIGN. <Figma>
# 5. Technologies <Python>
# 6. Using a project management tool and dividing your <Notion,Jira.>
