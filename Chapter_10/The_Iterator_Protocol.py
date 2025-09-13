
class JediOrder:
    def __init__(self, jedis):
        self._jedis = jedis

    def __iter__(self):
        """
        The iterator protocol:
        This method makes the JediOrder object iterable.
        It returns an iterator for the internal list of jedis.
        """
        return iter(self._jedis)



# --- Demonstration ---
jedis = ["Luke Skywalker", "Obi-Wan Kenobi", "Yoda"]
jedi_order = JediOrder(jedis)

print("Looping through the Jedi Order with a for loop:")
for jedi in jedi_order:
    print(f"- {jedi} is a member of the Order.")



