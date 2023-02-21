from string import Template

my_email = '''Dear ${first_name} ${last_name},
I am pleased to offer you our new Platinum Plus Rewards card
at a special introductory APR of 47.99%. ${first_name}, an offer
like this does not come along every day, so I urge you to call
now toll-free at 1-800-314-1592. We cannot offer such a low
rate for long, ${first_name}, so call right away.'''


def generate_email(first_name, last_name, email_text):
    t = Template(email_text)
    return t.substitute(first_name=first_name, last_name=last_name)


print(generate_email("Anna", "Kort", my_email))
