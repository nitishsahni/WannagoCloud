def save_both(user, model, first_name, last_name, email):
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.username = email
    user.save()
    model.user = user
    model.save()


def get_names(contact_name):
    if ' ' in contact_name:
        names = contact_name.split(' ')
        return names[0], names[1]
    else:
        return contact_name, " "