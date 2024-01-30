from random import randint, choice
from attribs import get_attr
from variables import insults

MY_ID = "@1061655101015588885"
PREFIX = ","


def get_response(user_input, username, usermention, channel):
    MY_NAME = "VENO.M"
    lowered = user_input.lower()
    username = username.upper()

    if lowered.startswith(PREFIX + "roll"):
        return f"{usermention} rolled: {randint(1, 6)}"
    # elif lowered.startswith(PREFIX + "google"):
    #     webbrowser.open("https://www.google.com/search?q=" + user_input[7:])
    elif lowered.startswith(PREFIX + "insult"):
        return f"{usermention} {choice(insults)}"
    elif lowered.startswith(PREFIX + "attr"):
        return get_attr(user_input[6:], usermention, channel, username)
    elif lowered.startswith(PREFIX + "fight"):
        if username == MY_NAME:
            return choice(
                [
                    f"\\*tangles with {usermention}\\*",
                    f"\\*throws a punch but {usermention} blocks it\\*",
                    f"\\*throws {usermention} through the wall\\*",
                ]
            )
        else:
            return choice(
                [
                    f"\\*eats {usermention}'s head\\*",
                    f"\\*considers using {usermention} as their next host, then decides they would be too weak and eats them\\*",
                    f"Puny human {usermention}",
                ]
            )
    elif lowered.startswith(PREFIX + "greatest"):
        if username == MY_NAME:
            return f"{usermention} is the greatest! All hail venom!"
        else:
            return f"Sorry {usermention}, it's still venom."
    # elif "wee" in lowered:
    #   return "That schlaaag weebootz"
    elif lowered.startswith(PREFIX + "help markdown"):
        return f"## {usermention} [Here's a guide to markdown in Discord](https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-)"
    elif lowered.startswith(PREFIX + "help commands"):
        return """
# __Carnage Commands__
- , (comma) = The prefix for all commands. E.g, ,roll
- roll = Pick a random number between 1 and 6, like a dice.
- fight = Fight Carnage for a random outcome.
- greatest = Find out who is the greatest.
- attr = Find out what % of an attribute you are. ",attr help" will list all attributes.
- insult = Get a random insult.
=================================================
- help commands = show this text.
- help markdown = Show a link to Discord's markdown reference.
"""
    else:
        return ""  # "and theeeeeeen............"
    #    return choice(
    #        [
    #            "I do not understand...",
    #            "What are you talking about?",
    #            "Do you mind rephrasing that?",
    #        ]
    #    )
