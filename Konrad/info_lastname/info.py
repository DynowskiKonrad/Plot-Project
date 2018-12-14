def info(last_name, *names, title=None):
    """

    :rtype: object
    """
    return (title, last_name, names)


print(info("Dynowski", "Konrad", "Jarosław", title="Technik"))
