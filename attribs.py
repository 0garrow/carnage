from random import randint

attributes =  ['happy', 'bastard', 'mischievous', 'bashful', 'cute', 
'sexy', 'bitch', 'devil', 'enviable', 'sarcastic', "saddo", "crazy",
'beautiful', 'sleepy', 'grumpy', 'horny', 'curious', 'positive', 
'cynical', 'boring', 'vain', 'stupid', 'greedy', 'passionate', 
'evil', 'dopey', 'caring', 'arrogant', 'rude', 'lazy', 'flirt',
'outgoing', 'cool', 'daring', 'engaging', 'honest', 'cheap', 
'fussy', 'jealous', 'perfectionist', 'smug', 'reliable', 'devilish'
'witty', 'funny', 'sad', 'angry', 'enamoured', 'angel', 'nurturing']

attributes_nsfw = ['kinky', 'sub', 'dom', 'switch', 'tabboo', 
'slut', 'spankable', 'daddy', 'boss', 'mistress', 'sir', 'master', 
'tied', 'stimulated', 'orgasmic', 'sensual']

def get_attr(user_input, usermention, channel):
    user_input = str(user_input)
    channel = str(channel)
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
    elif user_input == "help" :
        attributes.sort()
        attributes_nsfw.sort()
        return f"""# __Carnage Commands__ (attr)
        Here is the full list of currently available attributes **({len(attributes)})**:
        {attr_list}
        """

    if channel.startswith("nsfw") and user_input in attributes or user_input in attr_nsfw_list:
        return f"{usermention} is {randint(0, 100)}% {user_input} 😈"
    elif user_input in attributes:
        return f"{usermention} is {randint(0, 100)}% {user_input}"
    else:
        return f"{usermention} that is not a valid attribute"



