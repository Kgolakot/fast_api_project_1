from multiprocessing import Process
from multiprocessing import Value, cpu_count, current_process, parent_process
import multiprocessing
from time import sleep

class CustomProcess(Process):

    def __init__(self):
        Process.__init__(self)
        self.data = Value('i',0)

    def run(self):
        sleep(1)

        self.data.value = 99
        func_process = current_process()
        print(f"current process that is being executed {func_process}")


        print("This is coming from another process")
        print(f"Child Stored: {self.data.value}")
    

if __name__ == "__main__":
    process = CustomProcess()

    start_methods = multiprocessing.get_all_start_methods()

    print(f"All start methods {start_methods}")

    current_start_method = multiprocessing.get_start_method()

    print(f"Current start method {current_start_method}")

    process.start()

    print(f".... waiting for the process: {process.name} to start")

    print(f"Is current process daemon: {process.daemon}")
    print(f"Child process pid {process.pid}")
    num_cores = cpu_count()
    print(f"the number of cores available in this cpu {num_cores}")

    process.join()

    main_process = parent_process()
    print(f"the current main process {main_process}")

    print(f"Parent got: {process.data.value}")