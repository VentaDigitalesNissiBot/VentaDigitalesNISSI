import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN, SOPORTE, HORARIO, PAGOS
from keyboards import menu_principal, boton_comprar


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🛍️ <b>VENTA DIGITALES NISSI</b>\n\n"
        "⚡ El más rápido y confiable en ventas digitales.\n\n"
        "✅ Entrega inmediata\n"
        "🔒 Servicio seguro\n"
        "⚡ Atención rápida\n\n"
        "👇 Selecciona una opción del menú:",
        parse_mode="HTML",
        reply_markup=menu_principal,
    )


@dp.message(F.text == "🎬 YouTube Premium")
async def youtube(message: Message):
    await message.answer(
        "🎬 <b>YouTube Premium Individual</b>\n\n"
        "💵 Precio: <b>US$3.50</b>\n"
        "⚡ Entrega inmediata\n"
        "🔒 Servicio seguro",
        parse_mode="HTML",
        reply_markup=boton_comprar(),
    )


@dp.message(F.text == "🎵 Spotify Premium")
async def spotify(message: Message):
    await message.answer(
        "🎵 <b>Spotify Premium Individual</b>\n\n"
        "💵 Precio: <b>US$3.50</b>\n"
        "⚡ Entrega inmediata\n"
        "🔒 Servicio seguro",
        parse_mode="HTML",
        reply_markup=boton_comprar(),
    )


@dp.message(F.text == "🍿 Crunchyroll Mega Fan")
async def crunchyroll_mega(message: Message):
    await message.answer(
        "🍿 <b>Crunchyroll Mega Fan</b>\n\n"
        "💵 Precio: <b>US$3.50</b>\n"
        "⚡ Entrega inmediata",
        parse_mode="HTML",
        reply_markup=boton_comprar(),
    )


@dp.message(F.text == "👑 Crunchyroll Ultimate Fan")
async def crunchyroll_ultimate(message: Message):
    await message.answer(
        "👑 <b>Crunchyroll Ultimate Fan</b>\n\n"
        "💵 Precio: <b>US$7.00</b>\n"
        "⚡ Entrega inmediata",
        parse_mode="HTML",
        reply_markup=boton_comprar(),
    )


@dp.message(F.text == "📺 Stella TV")
async def stella(message: Message):
    await message.answer(
        "📺 <b>Stella TV</b>\n\n"
        "💵 Precio: <b>US$5.00</b>\n"
        "⚡ Entrega inmediata",
        parse_mode="HTML",
        reply_markup=boton_comprar(),
    )


@dp.message(F.text == "🌊 Oleada TV")
async def oleada(message: Message):
    await message.answer(
        "🌊 <b>Oleada TV</b>\n\n"
        "💵 Precio: <b>US$4.00</b>\n"
        "⚡ Entrega inmediata",
        parse_mode="HTML",
        reply_markup=boton_comprar(),
    )


@dp.message(F.text == "💳 Métodos de Pago")
async def metodos_pago(message: Message):
    lista_pagos = "\n".join(f"• {pago}" for pago in PAGOS)

    await message.answer(
        "💳 <b>MÉTODOS DE PAGO</b>\n\n"
        f"{lista_pagos}\n\n"
        f"👨‍💻 Para realizar tu pago contacta: {SOPORTE}",
        parse_mode="HTML",
    )


@dp.message(F.text == "👨‍💻 Soporte")
async def soporte(message: Message):
    await message.answer(
        "👨‍💻 <b>SOPORTE NISSI</b>\n\n"
        f"📲 Contacto: {SOPORTE}\n\n"
        "⚡ Atención rápida y segura.",
        parse_mode="HTML",
        reply_markup=boton_comprar(),
    )


@dp.message(F.text == "🕒 Horario")
async def horario(message: Message):
    await message.answer(
        "🕒 <b>HORARIO DE ATENCIÓN</b>\n\n"
        "🇺🇸 Hora del Este (ET)\n"
        "📅 Lunes a Domingo\n"
        f"⏰ {HORARIO}",
        parse_mode="HTML",
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())