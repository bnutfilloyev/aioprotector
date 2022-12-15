from aiogram import F, Router
from aiogram.types import ContentType, Message

router = Router()
router.message.filter(F.chat.type == "group")


@router.message(
    ~F.content_type(ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER)
)
async def remove_join(message: Message):
    await message.delete()
    if message.content_type == ContentType.NEW_CHAT_MEMBERS:
        text = "Assalomu alaykum, {}! aiogram[uz] kommunityga xush kelibsiz!".format(
            message.from_user.full_name
        )
        await message.answer(text)
