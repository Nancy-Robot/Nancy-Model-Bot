class Script(object):
    START_TXT = """<b>Hello {},
My Name is <a href=https://t.me/{}>{}</a>. A Smart RoBot With Many Amazing Features. I Can Provide Movies & Help You To Manage Your Groups, Just Add Me To Your Group And Enjoy.🥰</b>"""

    HELP_TXT = """<b>Hey {}
Here Is The Help For My Commands.</b>"""

    HACKER_TXT = """<b>Hey {}
Here Is The Help For My Commands.</b>"""

    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ : <a href='https://t.me/Oru_adaar_Robot'>Nᴀɴᴄʏ 🌸</a>
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/Hacker_Jr'>HᴀᴄKᴇʀ Jʀ 🇮🇳 / 🇺🇸</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3</a>
✯ Dᴀᴛᴀ Bᴀsᴇ: <a href='https://cloud.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://heroku.com/'>Hᴇʀᴏᴋᴜ</a>
✯ Bᴜʟʟᴅ Sᴛᴀᴛᴜs: <code>ᴠ1.0.1 [ Bᴇᴛᴀ ]</code></b>"""

    SOURCE_TXT = """Help: <b>Song</b>

<b>Music download modules, for those who love music.</b>

<b>Commands and Usage:</b>
• /song or /mp3 (songname & youtube link) - download song from yt servers.
• /video or /mp4 (songname & youtube link)

<b>YouTube Thumbnail Download</b>
• /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/hth250mmc6k</code>

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    CORONA_TXT ="""Help: <b>Corona</b>

<b>Here is the help for the coron information module</b>

➢ /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

➢ <b>Example</b> : - /covid India

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    STICKER_TXT ="""<b>COMMAND <code>/stickerid</codo>\n\n𝖨𝖿 𝖸𝗈𝗎 𝖭𝖾𝖾𝖽 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 𝖢𝗅𝗂𝖼𝗄 /stickerid 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 (𝖱𝖾𝗉𝗅𝗒 𝖶𝗂𝗍𝗁 𝖲𝗍𝗂𝖼𝗄𝖾𝗋)</b>"""
    
    LINK_TXT = """<b>• If You Want To Get The Requested Movies You Have To Join The Main Channel Given Below.🥰\n\n• ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ താഴെ കൊടുത്തിട്ടുള്ള Main Channel ജോയിൻ ചെയ്യണം.🥰 </b>"""
    
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin:</b>
All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!

<b>Commands & Usage:</b>
◉ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
◉ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""

    MANUALFILTER_TXT = """Help: <b>Manual Filters</b>

- Manual Filter is the feature where users can set automated replies for a particular keyword and bot will respond whenever a keyword is found the message!.

<b>Commands and Usage:</b>
• /filter - add a filter in chat.
• /filters - list all the filters of a chat.
• /del - delete a specific filter in chat.
• /delall - delete the whole filters in a chat (chat owner only).

<b>NOTE:</b>
• Nancy should have admin privillage.
• Only admins can add filters in a chat.
• Alert buttons have a limit of 64 characters."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Nancybot support both url and alert inline buttons.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/kerala_rockers)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Nancy supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format."""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

Auto Filter is the feature to filter and save all the files automatically from channel to group. This mostly used in group to get movies with name!

<b>NOTE:</b>
• Make me the admin of your channel if it's private.
• Make sure that your channel does not contains camrips, porn and fake files.
• Forward the last message to me with quotes or send me the last message link.
• Nancy will save all the files in that channel to db as u can use them in the group."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - connect a particular chat to your PM.
• /disconnect  - disconnect from a chat.
• /connections - list all your connections."""

    JSON_TXT ="""<b>JSON</b>

Bot Send Json For All Replied Messages Using A Simple Command.

<b>Command and Usage:</b>

◉ /json :- Reply To Any Message To Get Json

◉ You Can Use This Command In Pm And Groups."""

    FUN_TXT = """<b>GAMES MODULE</b> 
    
<b>NOTHING MUCH JUST SOME GAMES THINGS</b>
t𝗋𝗒 𝗍𝗁𝗂𝗌 𝖮𝗎𝗍: 

𝟣. /dice - Roll The Dice 
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot"""

    ADDFILE_TXT ="""<b>ADD FILES</b>

<b>Forward me a movie file from any movie channel. I will save those files. 
Make me admin in channel if its private. 
You can also forward all wanted movies to your channel and send last movie file of that channel

Make sure your channel has only movie files!</b>"""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
• /id - get id of a specifed user.
• /info  - get information about a user.
• /json - get the json details of a message.

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• Nancy should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

Make it easy to promote and demote with admin module!

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users.

<b>NOTE:</b>
• Nancy should have admin privillage.
• Only admins can execute these in a chat.
• These commands can be used only in group."""
 
    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
• /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
• Nancy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""


    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 JOIN THIS CHANNEL & TRY AGAIN 👇**"""
    
    URL_SHORTNER_TXT = """Help: <b>Url Shortner</b>
Some URLs is Shortner

<b>Commands and Usage:</b>
• /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/kerala_Rockers</code>

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
• /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
• Nancy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    REPORT_TEXT = """𝖧𝖾𝗅𝗉: <b><u>𝖱𝖾𝗉𝗈𝗋𝗍</u></b>

Report something wrong to group admins for review!

<b><u>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</u></b>
➢ /report [reply] - Report a message to admins for review.
➢ /report [reason] - Report a message to admins with reason.
➢ @admins - Same as report command, but not a command.

<b><u>NOTE:</u></b>
• Nancy should have admin privillage.
• These commands can be used only in group.
• These commands can be used by any group member."""

    AFK_TXT = """Help: <b>AFK</b>

Away From Keyboard is to tell that you're not available!

<b>Commands and Usage:</b>
• /afk - Mark yourself as afk.
• /afk [reason] - Mark yourself as afk with reason.

NOTE:
• Nancy should have admin privillage.
• These commands can be used only in group.
• These commands can be used by any group member."""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
