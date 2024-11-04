#pip install twisted
# 
from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        # This function is called whenever data is received from a client
        print("Received data:", data)
        self.transport.write(data)  # Echoes the data back to the client

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

# Start the server on port 8000
reactor.listenTCP(8000, EchoFactory())
reactor.run()
