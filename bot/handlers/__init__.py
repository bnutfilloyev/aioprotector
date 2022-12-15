from aiogram import Router


def setup_routers() -> Router:
    from . import test
    from . import remove_join

    router = Router()
    router.include_router(remove_join.router)
    router.include_router(test.router)

    return router
