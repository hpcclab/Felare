import pandas as pd



path = '../workload/execution_times'
no_of_tasks = 2
no_of_machines = 2
slack_factor = 1.2

et_all = pd.DataFrame(data=None, columns =['execution_time'])
avg_tt = pd.DataFrame(columns=[f'T{i}' for i in range(1, 1 + no_of_tasks)], index= [0])
deadlines = pd.DataFrame(columns=[f'T{i}' for i in range(1, 1 + no_of_tasks)], index= [0])

for tt in range(1, 1 + no_of_tasks):
    et_tt = pd.DataFrame(data=None, columns =['execution_time'])    
    
    for m in range(1, 1+no_of_machines):
        if m==1:
            machine ='cpu'
        else:
            machine = 'gpu'
         
        data = pd.read_csv(f'{path}/{tt}-{machine}.csv')
        # data = pd.read_csv(f'{path}/{tt}-m{m}.csv')
        et_tt = et_tt.append(data, ignore_index=True)
        et_all = et_all.append(data, ignore_index=True)
        
    avg_tt.loc[0,f'T{tt}'] = et_tt['execution_time'].mean()
    
avg_all = et_all['execution_time'].mean()

for tt in range(1, 1 + no_of_tasks):
   
    delta = avg_tt.loc[0,f'T{tt}'] + slack_factor * avg_all
    delta = round(delta, 1)
    deadlines.loc[0,f'T{tt}'] = delta
#deadlines.to_csv('../workload/execution_times/deadlines.csv',index = False)