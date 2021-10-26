import snap7
client = snap7.client.Client()
client.connect("127.0.0.1", 0, 0, 1012)
print(client.get_connected())