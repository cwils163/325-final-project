import pandas as pd

# CHANGE AS NEEDED
dataset_name = 'AO3_1'

done_ids = []
with open(f'{dataset_name}.txt', mode='r', encoding='utf-8') as inf:
    for line in inf:
        done_ids.append(line.replace('\n', ''))

all_ids = []
with open(f'./acl23_trigger_warning_assignment/resources/splits/{dataset_name}.txt', mode='r') as inf:
    for line in inf:
        all_ids.append(line.replace('\n', ''))
print(all_ids[0])
    
with open(f'new_{dataset_name}.txt', 'w') as f: #CHANGE IN HYDRATE
    for i in range(all_ids.index(done_ids[len(done_ids) - 1]) + 1, len(all_ids)):
        f.write(f'{all_ids[i]}\n')