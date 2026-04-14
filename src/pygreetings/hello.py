"""
A module that says hi to a friend in different ways.
"""

def greetings(name):
    """
    Say hi to the name provided

    Parameters
    ----------
    name : str
        The name you want to say hi to

    Returns
    -------
    str
        A sentence greeting the provided name

    Examples
    --------
    >>> greetings("Sophia")
    "Hello 👋 Sophia!"
    >>> greetings("Eliott Brun")
    "Hello 👋 Eliott Brun!"

    """

    return "Hello 👋 " + name + "!"
