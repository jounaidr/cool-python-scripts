import random

def spongebob_text(input):
    char_list = list(input)
    # loop through each char
    for i in range(0, len(char_list)):
        # check char is a letter
        if str.isalpha(char_list[i]):
            if random.choice([0, 1]) < 0.5:
                # 50% chance to either cap or uncap
                char_list[i] = char_list[i].swapcase()

    return "".join(char_list)

print(spongebob_text("ahahahahahahahahahaahahahahaha"))