
# A safe way to open and read a file.
# The `as` keyword assigns the open file to the variable `file_handle`.
with open("ship_core/logs/engine_room/log_01.dat", "r") as file_handle:
    # Everything in this block has access to the open file.
    log_content = file_handle.read()
    print("\n--- Engine Log Snippet ---")
    # For demonstration, we'll assume the file exists and has content
    #(I have manually put some data inside already! )
    print(log_content[:50])

# Outside this block, the airlock is automatically closed.
# The file is secure and the system is stable.