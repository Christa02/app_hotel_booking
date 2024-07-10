import pandas


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book_hotel(self):
        """Books hotel by making 'available' as 'no'"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv",index=False)

    def available(self):
        """Checks whether a hotel is available for booking"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, cust_name, hotel_id):
        self.cust_name = cust_name
        self.hotel_id = hotel_id

    def generate_ticket(self):
        content = f"""
            Thank you for your reservation!
            Here is your booking data:
            Name : {self.cust_name}
            Hotel Name : {self.hotel_id.name}
        """
        return content


df = pandas.read_csv('hotels.csv', dtype={"id": str})
print(df)
hotel_ID = input("Enter the hotel ID:")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book_hotel()
    name = input("Enter your name...")
    reserve_ticket = ReservationTicket(name, hotel)
    print(reserve_ticket.generate_ticket())
