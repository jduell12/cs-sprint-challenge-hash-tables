class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        
    def __repr__(self):
        return f"Ticket({self.source}, {self.destination})"


def reconstruct_trip(tickets, length):
    itinerary = []
    flights = {}
    
    for ticket in tickets:
        flights[ticket.source] = ticket.destination
    
    itinerary.insert(0, flights['NONE'])
    
    for i in range(length-1):
        itinerary.append(flights[itinerary[i]])
    
    return itinerary


