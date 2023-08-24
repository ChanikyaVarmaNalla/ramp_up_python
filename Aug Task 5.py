import sys
import threading
import time
import random
import queue

class ProducerConsumer:
    def __init__(self, num_producers, num_consumers):
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.shared_queue = queue.Queue()

    def producer(self):
        for i in range(3):  # Produce 5 items
            item = f"Item {i}"
            self.shared_queue.put(item)
            print(f"Producing {item}")
            time.sleep(random.uniform(0.1, 0.5))

    def consumer(self):
        while True:
            try:
                item = self.shared_queue.get(timeout=1)
                print(f"Consuming {item}")
                self.shared_queue.task_done()
                time.sleep(random.uniform(0.1, 0.5))
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
    if len(sys.argv) != 3:
        print("Usage: python program.py <num_producers> <num_consumers>")
        sys.exit(1)

    num_producers, num_consumers = map(int, sys.argv[1:3])

    producer_consumer = ProducerConsumer(num_producers, num_consumers)
    producer_consumer.run()
