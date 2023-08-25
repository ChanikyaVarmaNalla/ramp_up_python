import threading
import time
import random
import queue

class ProducerConsumer:
    def __init__(self, num_producers, num_consumers):
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.shared_queue = queue.Queue(maxsize=5)

    def producer(self):
        item = f"Item from Producer {threading.current_thread().name.split()[0].split('-')[-1]}"
        self.shared_queue.put(item, block=True)
        print(f"Producing {item}")
        time.sleep(random.uniform(0.1, 0.5))

    def consumer(self):
        while True:
            try:
                item = self.shared_queue.get(timeout=1)
                print(f"Consuming {item} by Consumer {threading.current_thread().name.split()[0].split('-')[-1]}")
                self.shared_queue.task_done()
                break
            except queue.Empty:
                break

    def run(self):
        producer_threads = [threading.Thread(target=self.producer) for _ in range(self.num_producers)]
        consumer_threads = [threading.Thread(target=self.consumer) for _ in range(self.num_consumers)]

        for thread in producer_threads:
            thread.start()

        for thread in consumer_threads:
            thread.start()

        for thread in producer_threads:
            thread.join()

        for thread in consumer_threads:
            thread.join()

if __name__ == "__main__":

    num_producers = int(input("Number of producers: "))
    num_consumers = int(input("Number of consumers: "))

    producer_consumer = ProducerConsumer(num_producers, num_consumers)
    producer_consumer.run()
