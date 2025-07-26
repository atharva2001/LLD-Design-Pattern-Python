class APIGateway:
    def redirect(self, endpoint, query):
        print(f"Redirected {query} to {endpoint}")


class Client:
    def __init__(self, endpoint, gateway: APIGateway):
        self.endpoint = endpoint
        self.gateway = gateway
    
    def send_quey(self, query="Get Method"):
        self.gateway.redirect(self.endpoint, query)


gateway = APIGateway()

client1 = Client("/login", gateway)
client2 = Client("/about-us", gateway)

client1.send_quey("credentials")
client2.send_quey()

        
