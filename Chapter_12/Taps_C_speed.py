
import numpy as np
import random
import time

readings_np = np.array([random.uniform(0.1, 10.0) for _ in range(10_000_000)])

start_time = time.time()
scaled_readings_np = readings_np * 1.5
end_time = time.time()

print(f"NumPy processing time: {end_time - start_time:.4f} seconds")