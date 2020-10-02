class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        
    def __repr__(self):
        return f"Ticket({self.source}, {self.destination})"


def reconstruct_trip(tickets, length):
    itinerary = []
    middle = {}
    
    for ticket in tickets:
        if ticket.source == "NONE":
            itinerary.insert(0, ticket.destination)
        elif ticket.destination == "NONE":
            itinerary.insert(length-1, ticket.source) 
        else:
            pass
    return itinerary

tickets = [
    Ticket("PIT",  "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket( "SFO",  "BHM" ),
    Ticket( "FLG",  "XNA" ),
    Ticket("NONE",  "LAX" ),
    Ticket ("LAX",  "SFO" ),
    Ticket ("CID",  "SLC" ),
    Ticket ("ORD",  "NONE" ),
    Ticket("SLC",  "PIT" ),
    Ticket("BHM",  "FLG" )
]
print(reconstruct_trip(tickets, len(tickets)))

# expected = ["PDX", "DCA", "NONE"]
