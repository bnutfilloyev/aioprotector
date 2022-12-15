from aiogram import F, Router
from aiogram.types import ContentType, Message

router = Router()


@router.message(
    F.content_type.in_({ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER})
)
async def remove_join(message: Message):
    await message.delete()
    if message.content_type == ContentType.NEW_CHAT_MEMBERS:
        text = f"Assalomu alaykum {message.from_user.mention_html()}, aiogram[uz] kommunityga xush kelibsiz!"
        await message.answer(text)
