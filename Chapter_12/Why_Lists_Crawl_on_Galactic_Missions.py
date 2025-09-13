

import random
import time

readings = [random.uniform(0.1, 10.0) for _ in range(10_000_000)]
scaled_readings = []


start_time = time.time()
for reading in readings:
    scaled_readings.append(reading * 1.5)
end_time = time.time()

print(f"List processing time: {end_time - start_time:.4f} seconds")