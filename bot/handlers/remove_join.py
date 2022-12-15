from aiogram import Router, F
from aiogram.types import Message, ContentType

router = Router()


@router.message(~F.content_type(ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER))
async def remove_join(message: Message):
    await message.delete()
    await message.answer(
        "<a href='tg://user?id={user_id}'>{user_name}</a> sizni ko'rib turganimizdan xursandmiz.".format(
            user_id=message.from_user.id, user_name=message.from_user.full_name))
