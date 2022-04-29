from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, CMD_HANDLER, bot
from userbot.utils import skyzu_cmd


@skyzu_cmd(pattern="hentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@nHentaiBot"
    await event.edit("```Processing```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=424466890)
            )
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @nHentaiBot and try again```")
            return
        if response.text.startswith("**Sorry I couldn't get manga from**"):
            await event.edit("```I think this is not the right link```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "hentai": "`.hentai` <link / code> \
\nUsage: view nhentai in telegra.ph XD\n"
    }
)
