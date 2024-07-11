import pandas

df = pandas.read_csv('hotels.csv', dtype={"id": str})
df_cards = pandas.read_csv('cards.csv', dtype=str).to_dict(orient="records")
df_card_security = pandas.read_csv('card_security.csv', dtype=str)


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self,expiration, cvc, holder):
        card_dict = {"number": self.number, "expiration": expiration, "cvc": cvc, "holder": holder}
        if card_dict in df_cards:
            return True
        else:
            return False


class SecurityCreditCard(CreditCard):
    def authenticate(self, given_psw):
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if password == given_psw:
            return True
        else:
            return False


print(df)
hotel_ID = input("Enter the hotel ID:")
hotel = Hotel(hotel_ID)
if hotel.available():
    card_no = input("Enter the card number:")
    card_expiry = input("Enter the card expiry date:")
    card_cvc = input("Enter the card CVC:")
    card_holder = input("Enter the card holder name:")
    credit_card = SecurityCreditCard(card_no)
    card_validity = credit_card.validate(card_expiry, card_cvc, card_holder)
    if card_validity:
        psw = input("Enter the password:")
        card_authenticated = credit_card.authenticate(psw)
        if card_authenticated:
            hotel.book_hotel()
            name = input("Enter your name...")
            reserve_ticket = ReservationTicket(name, hotel)
            print(reserve_ticket.generate_ticket())
        else:
            print("Card authentication failed....")
    else:
        print("Card validation failed....")
else:
    print("The hotel is not available for booking...")
