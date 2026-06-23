def ValidateEmail(email):
    if "@" not in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or not domain:
        return False
    if ".." in email or " " in email:
        return False
    if email.startswith("@") or email.endswith("@"):
        return False
    if len(email) > 254 or len(local) > 64:
        return False
    if domain.startswith("-") or domain.endswith("-"):
        return False
    if "." not in domain:
        return False
    return True

with open("input.txt", "r") as file:
    emails = file.readlines()

with open("output.txt", "w") as out:
    for email in emails:
        email = email.strip()
        result = "VALID" if ValidateEmail(email) else "INVALID"
        out.write(f"{result} -- {email}\n")