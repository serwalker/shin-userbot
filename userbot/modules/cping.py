""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import random

from userbot import DEVS
from userbot.events import register

cping = [
    "**Hadir bang shin** `𓆩79.08𓆪` ",
    "**Bang shin ganteng** `𓆩99.65𓆪` ",
    "**bang shin mau ucerbot 😖** `𓆩76.89𓆪` ",
    "**sungkem dulu sama tuan shin** `𓆩72.69𓆪` ",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=1966035463, pattern=r"^.cping$")
async def _(shin):
    await shin.reply(random.choice(cping))
