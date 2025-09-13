
class JediOrder:
    def __init__(self, jedis):
        self._jedis = jedis

    def __len__(self):
        """
        The sequence protocol:
        Returns the number of jedis in the order.
        """
        return len(self._jedis)

    def __getitem__(self, index):
        """
        The sequence protocol:
        Allows access to a jedi by index.
        It also enables slicing, like jedi_order[0:2].
        """
        return self._jedis[index]





# --- Demonstration ---

jedis = ["Luke Skywalker", "Obi-Wan Kenobi", "Yoda"]
jedi_order = JediOrder(jedis)

print("Accessing jedi by index:")
print(f"The first jedi is: {jedi_order[0]}")
print(f"The last jedi is: {jedi_order[-1]}")

print("\nLooping with the sequence protocol:")
for jedi in jedi_order:
    print(f"- {jedi} is in the Order.")