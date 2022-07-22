"""
Authors: Ali Mokhtari
Created on Jan. 07, 2021.

Description:

"""
# from etc_generator import gamma
import random
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

class ExecutionTime:
    # Here, the execution time of task type on a specific machine type
    # is read from the dataset. Then, an execution time is sampled and
    # return as estimated or real execution time. 

    def __init__(self):        
        self.execution_times = None
    
    
           

    def sample(self, task_type_id, machine_type, size):
        # Here, the execution time of task type on a specific machine type
        # is read from the dataset. This function returns a list that 
        # contains the execution times.
        # the file name of the dataset must be in the format of 
        # <task_type_id>-<machine_type>.csv (e.g. 1-CPU.csv)
            
        path_to_file =f"./workload/execution_times/{task_type_id}-{machine_type.name}.csv"
        data = pd.read_csv(path_to_file)
        self.execution_times = np.random.choice(data['execution_time'].values, size)
        self.execution_times = [round(x, 3) for x in self.execution_times]    
       
        return self.execution_times
    
    def synthesize(self, task_type_id, machine_type,interval, size):
        low = interval[0]
        high = interval[1]
        self.execution_times = np.random.uniform(low, high, size)        
        self.execution_times = [round(x, 3) for x in self.execution_times]
        df = pd.DataFrame(data=self.execution_times, columns=['execution_time'])
        df.to_csv(f'../workload/execution_times/{task_type_id}-{machine_type}.csv', index= False)

        return self.execution_times




# =============================================================================
# v_task = 0.1
# mu_machine = 3.0
# v_machine = 0.9
# 
# v_exe = 0.1
# 
# no_of_machines = 4
# no_of_tasks = 4
#     
# etc  = gamma(mu_machine, v_machine, v_task, no_of_machines, no_of_tasks)
# etc.to_csv('../workload/execution_times/etc.csv')
# 
# for t_id in range(no_of_tasks):
#     for m_id in range(no_of_machines):
#         print(f'Task:{t_id}  Machine:{m_id}')
#         et = ExecutionTime()
#         mu_exe = etc.loc[f'T{t_id}',f'M{m_id}']
#         lower = mu_exe*(1-v_exe*np.sqrt(3))
#         upper = 2*mu_exe - lower
#         execution_times = et.synthesize(t_id+1,f'm{m_id+1}',[lower,upper],1000)
#         plt.figure()
#         plt.hist(execution_times, 50, density=True)
#         plt.title(f'Task: {t_id+1} Machine:{m_id+1}')
# =============================================================================
        

