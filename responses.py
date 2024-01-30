from random import randint, choice
from attribs import get_attr
import webbrowser

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
        return choice(
            [
                f"{usermention} The closest you'll come to a brainstorm is a light drizzle.",
                f"{usermention} Honestly, I'm just impressed you could read this.",
                f"{usermention} Your family tree didn't have enough branches.",
                f"{usermention} Your face just made me agnostic.",
                f"{usermention} I'm still deciding whether you're the weakest link or the missing link.",
                f"{usermention} I have neither the time nor the crayons necessary to explain this to you.",
                f"{usermention} You are an oxygen bandit.",
                f"{usermention} I've had bowel movements more attractive than you.",
                f'{usermention} You look like a "before" picture.',
                f"{usermention} You could have been an extra in Chernobyl.",
                f"{usermention} What doesn't kill you disappoints the rest of us.",
                f"{usermention} Did you develop your personality in car a crash?",
                f"{usermention} I smell smoke. Were you thinking too hard again?",
                f"{usermention} Being bitter won't make you prettier.",
                f"{usermention} Out of all the sperm to win the race...",
                f"{usermention} You'll go far someday. And I hope you stay there.",
                f"{usermention} Your gene pool needs more chlorine.",
                f"{usermention} I will not have a battle of wits with an unarmed ,opponent.",
                f"{usermention} It's impossible to underestimate you.",
                f"{usermention} The only time you're not as dumb as you look is when I close my eyes.",
                f"{usermention} Imagine how many crises would have been averted if your parents bothered to use a condom.",
                f"{usermention} You look like someone fed you after midnight.",
                f"{usermention} Even Bob Ross would call you a mistake.",
                f"{usermention} If I gave you a penny for your thoughts, I'd get change back.",
                f'{usermention} Our parents told us we could be anything, and you chose "disappointment".',
                f"{usermention} Your birth control of choice appears to be your personality.",
                f"{usermention} If you’re going to be two-faced, at least make one of them cute.",
                f"{usermention} If your IQ were just a little higher you could be an idiot.",
                f"{usermention} You're not the dumbest person alive, but you better hope they're taking vitamins.",
                f"{usermention} I'd love to help you out. Which way did you get in?",
                f"{usermention} Light travels faster than sound, which is why you seemed bright until you spoke.",
                f"{usermention} You're as bright as beige.",
                f"{usermention} You look like something I drew with my left hand.",
            ]
        )
    elif lowered.startswith(PREFIX + "attr"):
        return get_attr(user_input[6:], usermention, channel)
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
