import os, asyncio, humanize, logging
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode, ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
    try:
        # Attempt to create a new invite link
        invite_link_obj = await app.create_chat_invite_link(chat_id=channel_id, creates_join_request=True)
        if invite_link_obj and invite_link_obj.invite_link:
            return invite_link_obj.invite_link
        logger.error(f"No invite link created for channel {channel_id}.")
        return None
    except Exception as e:
        logger.error(f"Could not create invite link for channel {channel_id}: {e}")
        return None


async def check_subscription(client, user_id):
    """asyncio.run(main())
