from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneSymbolError(Exception):
    pass


valid_email_domains = ['.com', '.bg', '.org', '.net']
pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
email = input()
while email != 'End':
    try:
        if email.count("@")>1:
            raise MoreThanOneSymbolError("Email should contain only one @")
        elif len(findall(pattern_name, email.split('@')[0])[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        elif findall(pattern_domain, email.split('@')[1])[0] not in valid_email_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        print('Email is valid')
    except IndexError:
        print("Invalid Email")

    email = input()
