from random import choice

Quotes_list = [
    "for every complex problem there is an answer that is clear, simple, and wrong.",
    "you can't be successful in business without taking risks. It's really that simple",
    "Only great minds can afford a simple style.",
]


def get_quotes():
    return "\n".join(Quotes_list)


def add_quotes(quote):
    if isinstance(quote, str):
        Quotes_list.append(quote)
    else:
        return "qoute must be string."


def get_random_choice():
    return choice(Quotes_list)


# do this for run the following code only when run this file as code file
# and dot't run the following code when import this file as module
if __name__ == "__main__":
    add_quotes("you must be strong when you fill, wakeup and walk again don't stop ")
    print(get_quotes())
    print(get_random_choice())
