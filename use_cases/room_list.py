def room_list_use_case(repo):
    return repo.list()

def compute_total_use_case(repo):
    return repo.total

def calculate_total_interest(total_amount, percent):
    if percent < 0:
        raise ValueError("Percentage rate cannot be negative")

    interest = (total_amount * percent) / 100
    return interest