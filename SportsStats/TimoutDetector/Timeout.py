import time
import concurrent.futures


class Timeout:
    def __init__(self, func, timeout):
        self.func = func
        self.timeout = timeout
        self.current_time = 0

    def timer(self):
        while self.current_time < self.timeout:
            time.sleep(1)
            self.current_time += 1

    def run(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            timer = executor.submit(self.timer)
            function_future = executor.submit(self.func)
            if self.current_time >= self.timeout:
                print("[-] Method timed out.")
                function_future.cancel()
                return "TIMEOUT"
            else:
                return function_future.result()
