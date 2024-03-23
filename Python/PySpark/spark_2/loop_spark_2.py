import csv
import time
from multiprocessing import Process

start_time = time.perf_counter()

def run_spark(command: str):
    import os
    os.system(command)

file2 = 'test_data4.csv'

print("===================== Loop Spark : Read CSV ===============================")
with open(file2, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count = True
    header = None
    counter = 0
    processes = []

    for row in spamreader:
        counter = counter + 1

        if count:
            header = row
            count = False
        else:
            print("===================== CSV Values Start ===============================")
            print(type(row), " = ", row)
            print(type(', '.join(row)), " = ", ', '.join(row))
            print("===================== CSV Values End ================================")

            dct = dict(zip(header, row))

            cmd_name = "spark-submit"
            file_name = "spark_df_size_2.py"
            col_name = ' & '.join(header)
            values =  ' & '.join(row)
            final_cmd = f"{cmd_name} {file_name} {col_name} {values} {counter}"

            process = Process(target=run_spark, args=(final_cmd,))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()

            

end_time = time.perf_counter()
print(f"Multi Spark Session : Total run time is {end_time - start_time} seconds")

