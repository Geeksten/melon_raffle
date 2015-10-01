from customer_info import organize_customer_data
from random import choice


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print "Contact {name} at {email} to notify them they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )


customers = organize_customer_data("customers.txt")

print customers

pick_winner(customers)
