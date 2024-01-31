from random import randint
from variables import attributes, attributes_nsfw
import pandas as pd
from tabulate import tabulate


def write_top100(username, user_input):
    with open("top100.csv", "a") as file:
        file.writelines(f"{username}; {user_input}")
    return


def get_attr(user_input, usermention, channel, username):
    # Convert discord module objects to strings.
    user_input = str(user_input)
    channel = str(channel)
    username = str(username)
    attributes.sort()
    attributes_nsfw.sort()
    attr_list = ", ".join(attributes)
    attr_nsfw_list = ", ".join(attributes_nsfw)

    if user_input == "help" and channel.startswith("nsfw"):
        return f"""# __Carnage Commands__ (attr)
        Here is the full list of currently available attributes **({len(attributes)})**:
        {attr_list}

        NSFW attributes 😈 **({len(attributes_nsfw)})**:
        {attr_nsfw_list}
        """
    elif user_input == "help":
        attributes.sort()
        attributes_nsfw.sort()
        return f"""# __Carnage Commands__ (attr)
        Here is the full list of currently available attributes **({len(attributes)})**:
        {attr_list}
        """
    elif user_input == "top":
        df = pd.read_csv("top100.csv", sep=";")
        return tabulate(
            df, headers=["Username", "Attribute"], tablefmt="simple", showindex=False
        )
        # top = ""
        # for index, row in enumerate(df):
        #     top = f"{top}\n{index + 1}. {row}"
        # return top

    if (
        channel.startswith("nsfw")
        and user_input in attributes
        or user_input in attr_nsfw_list
    ):
        return f"{usermention} is {randint(0, 100)}% {user_input} 😈"
    elif user_input in attributes:
        percentage = randint(0, 100)

        if percentage == 100:
            write_top100(username, user_input)
            return f"# Congratulations!!!\n{usermention} is {percentage}% {user_input} and has been added to our TOP 100 hall of fame"
        else:
            return f"{usermention} is {percentage}% {user_input}"
    else:
        return f"{usermention} '{user_input}' is not a valid attribute. To view a current list of valid attributes ,type `,attr help`"
