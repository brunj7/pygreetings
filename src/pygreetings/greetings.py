"""
A module that says hi to a friend in different ways.
"""

def hello(name):
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
    >>> hello("Sophia")
    "Hello 👋 Sophia!"
    >>> hello("Eliott Brun")
    "Hello 👋 Eliott Brun!"

    """
    import random
    # List of emojis 
    emoji_list = ["👋", "😀", "🎉", "🔥", "🚀", "✨", "💫", "🤩"]
    
    # Randomly select the emoji to use
    random_emoji = random.choice(emoji_list)

    # Construct the final text
    return "Hello "+ random_emoji + " " + name + "!"
