from hello import hello

def test_hello_default():
   assert hello() == "Hello, world!"

def test_hello_argument():
   assert hello("alix") == "Hello, alix!"
