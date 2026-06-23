def ValidateEmail(email):
    if '@' not in email or email.count('@') != 1:
        return "INVALID"
    local, domain = email.split('@')
    if not local or local.startswith('.') or local.endswith('.'):
        return "INVALID"
    if not domain or '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return "INVALID"
    return "VALID"

while True:
    email = input("Enter email address (or 'exit' to quit): ")
    if email.lower() == 'exit':
        break
    print(f"{ValidateEmail(email)} -- {email}")