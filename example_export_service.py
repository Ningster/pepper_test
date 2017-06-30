
# coding: utf-8

# In[ ]:

import qi
import sys

class Foo:

    def bar(self):
        print("bar")

if __name__ == "__main__":
    app = qi.Application(sys.argv)

    # start the session
    app.start()

    app.session.registerService("foo", Foo())

    app.run()   # will exit when the connection is over

