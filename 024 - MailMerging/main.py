path_names = r"024 - MailMerging\Input\Names\invited_names.txt"
path_template = r"024 - MailMerging\Input\Letters\starting_letter.txt"
path_new_letter = r"024 - MailMerging\Output\ReadyToSend"
placeholde = "[name]"

with open(path_names, mode="r") as file:
    names = file.readlines()

with open(path_template, mode="r") as template:
    for name in names:
        receipient = name.strip()
        template_letter = template.read()
        name_letter = template_letter.replace(placeholde, receipient)
        with open(path_new_letter + f"\{receipient}.txt", mode="w") as letter:
            letter.write(f"{name_letter}")
