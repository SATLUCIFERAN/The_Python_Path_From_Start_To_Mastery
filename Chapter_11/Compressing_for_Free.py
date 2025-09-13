
import json
import gzip

# Let's write the data again, but this time to a compressed file
data_to_compress = [
    {'event': 'Galactic Senate vote', 'outcome': 'Failed'},
    {'event': 'Speeder chase', 'outcome': 'Successful'}
]

# The 'wt' mode tells gzip to write text

print("Compressing a new log into a tiny data cube...")
with gzip.open('compressed_log.ndjson.gz', 'wt', encoding='utf-8') as compressed_file:
    for data in data_to_compress:
        json_line = json.dumps(data)
        compressed_file.write(json_line + '\n')

# And now, let's decompress and read it just as easily

print("Decompressing and reading the data cube...")
read_data = []
with gzip.open('compressed_log.ndjson.gz', 'rt', encoding='utf-8') as compressed_file:
    for line in compressed_file:
        obj = json.loads(line.strip())
        read_data.append(obj)

print("Data successfully retrieved!")
print(f"Decoded data: {read_data}")