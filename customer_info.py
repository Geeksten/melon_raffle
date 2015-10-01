from customer import Customer


def organize_customer_data(customer_file_path):
    """Read customer file and return list of customer objects.

    Read file at customer_file_path and create a customer object containing
        customer information.

    """
    #create an empty list called customers
    customers = []

    #using the open(file_path) command opens the file
    #giving the output as lines
    #customer-name | email | street | city | zipcode
    #iterate through eah line in the file strip the spaces at the end
    #and split at the pipes

    # Process a file like:
    #
    #   customer-name | email | street | city | zipcode

    customer_file = open(customer_file_path)

    for line in customer_file:
        customer_data = line.strip().split("|")
        name, email, street, city, zipcode = customer_data

        new_customer = Customer(name, email, street, city, zipcode)
        customers.append(new_customer)

    return customers
