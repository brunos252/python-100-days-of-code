"""
read from file, create birthday invitations for names in file
"""
with open("Input/Letters/starting_letter.txt") as f:
    template = f.read()

with open("./Input/Names/invited_names.txt") as f:
    for name in f.readlines():
        name = name.strip()
        mail = template.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}_invitation.txt", "w") as out:
            out.write(mail)
