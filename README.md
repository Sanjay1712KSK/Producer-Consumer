Buffer: The buffer is implemented as a Queue with a maximum size (BUFFER_SIZE), simulating a fixed-size buffer.
Producer: Generates random items and puts them in the buffer. If the buffer is full, the put() method will block until space becomes available.
Consumer: Consumes items from the buffer. If the buffer is empty, the get() method will block until an item is available.
Threads: Two threads, one for the producer and one for the consumer, run in parallel.
Sleep: The time.sleep() function simulates production and consumption times.
