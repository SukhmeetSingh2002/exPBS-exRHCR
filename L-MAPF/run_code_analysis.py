import subprocess

benchmark = 'WAREHOUSE'  # 'WAREHOUSE'

num_agents = [220, 200, 180, 160, 140, 120, 100].reverse()  # warehouse
# num_agents = [100]  # warehouse
# num_agents = [, 450, 400, 350, 300, 250, 200, 150, 100]  # sorting

# deltas = [0, 1, 2]
deltas = [1]

# ells = [2, 5, 10, 20, 50, 1000]
ells = [10]

hs = [5]  # : warehouse-
# deltas_per_h = {3: [0, 3, 4, 5, 6, 7], 10: [1, 2, 3]}
# hs = [2, 3]  # : warehouse-
# deltas_per_h = {2: [2, 3, 4, 5, 6], 4: [0, 1, 2, 3, 4]}
priority = 2  # total priority = 3, PBS regular = 2
if priority == 3:
    deltas = [0]
if priority not in [2, 3]:
    ValueError('priority should be 2 (regular PBS) or 3 (total priority)')

# queries = [9]
queries = range(1)

for a in num_agents:
    print(f'%%%%%%%%%%%%%%%%\n num_agents={a}\n%%%%%%%%%%%%%%%%')
    for i in queries:  # create new 36
        for h in hs:
            # deltas = deltas_per_h[h]
            for d in deltas:
                for l in ells:
                    create_and_save = 1 if d == 0 else 0
                    # create_and_save = 0

                    print('-----------------------------------------------------------------------------------------\n'
                          '-----------------------------------------------------------------------------------------')
                    if benchmark == 'WAREHOUSE':
                        run_str = f'python3 ./run_windowed_L-MAPF_test_kiva_warehouse.py -a {a} ' \
                                  f'-c {create_and_save} -d {d} -t {i} -l {l} -r {h} -p {priority}'
                    elif benchmark == 'SORTING':
                        run_str = f'python3 ./run_windowed_L-MAPF_test_sorting_center.py -a {a} ' \
                                  f'-c {create_and_save} -d {d} -t {i} -l {l} -r {h} -p {priority}'
                    else:
                        ValueError('illegal benchmark name')
                    print(run_str)
                    print('-----------------------------------------------------------------------------------------\n'
                          '-----------------------------------------------------------------------------------------\n')
                    # input(f'run?')
                    status = subprocess.call(run_str, shell=True)  # if d>0 else 0

                    # run also total priority
                    if d == 0:
                        if benchmark == 'WAREHOUSE':
                            run_str_tot = f'python3 ./run_windowed_L-MAPF_test_kiva_warehouse.py -a {a} ' \
                                          f'-c 0 -d 0 -t {i} -l {l} -r {h} -p 3'
                        elif benchmark == 'SORTING':
                            run_str_tot = f'python3 ./run_windowed_L-MAPF_test_sorting_center.py -a {a} ' \
                                          f'-c 0 -d 0 -t {i} -l {l} -r {h} -p 3'
                        else:
                            ValueError('illegal benchmark name')

                        print(
                            "**************************************\n" + run_str_tot + "\n**************************************\n")
                        status = subprocess.call(run_str_tot, shell=True)


    # now read the success_rate.csv file and print the success rate
    # Example of the file:
    #   94   │ success rate,1,experience,1
    #   95   │ success rate,1,experience,1
    file_data = []
    with open(f'./success_rate.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            file_data.append(line.split(','))

    # for each agent, calculate the success rate and store it in a file
    num_agents = a
    success_rate = 0
    success_rate_with_experience = 0
    total_num_of_experiments = 0
    total_num_of_experiments_with_experience = 0
    file_len = len(file_data)
    for i in range(file_len):
        if len(file_data[i]) < 4:
            continue
        success_rate += int(file_data[i][1])
        total_num_of_experiments += 1
        if file_data[i][3] == '1\n':
            success_rate_with_experience += int(file_data[i][1])
            total_num_of_experiments_with_experience += 1
            
    output_file_name = f'./success_rate_{benchmark}_agents_{num_agents}.csv'
    with open(output_file_name, 'a') as f:
        if total_num_of_experiments>0:
            f.write(f'Average success rate,{(success_rate / total_num_of_experiments) * 100}\n')
        else:
            f.write(f'Average success rate,{0 * 100}\n')
        if total_num_of_experiments_with_experience>0:
            f.write(f'Average success rate with experience,{(success_rate_with_experience / total_num_of_experiments_with_experience) * 100}\n')
        else:
            f.write(f'Average success rate with experience,{0 * 100}\n')

        f.write(f'Success count,{success_rate}\n')
        f.write(f'Total number of experiments,{total_num_of_experiments}\n')


        f.write(f'Success count with experience,{success_rate_with_experience}\n')
        f.write(f'Total number of experiments with experience,{total_num_of_experiments_with_experience}\n')

        f.write(f'Number of agents,{num_agents}\n')
        f.write(f'Number of queries,{len(queries)}\n')
        f.write(f'Number of deltas,{len(deltas)}\n')
        f.write(f'Number of ells,{len(ells)}\n')
        f.write(f'Number of hs,{len(hs)}\n')
        
    # empty the success_rate.csv file
    with open(f'./success_rate.csv', 'w') as f:
        f.write('')

