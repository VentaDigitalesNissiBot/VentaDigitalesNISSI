from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

menu_principal = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎬 YouTube Premium"),
            KeyboardButton(text="🎵 Spotify Premium"),
        ],
        [
            KeyboardButton(text="🍿 Crunchyroll Mega Fan"),
            KeyboardButton(text="👑 Crunchyroll Ultimate Fan"),
        ],
        [
            KeyboardButton(text="📺 Stella TV"),
            KeyboardButton(text="🌊 Oleada TV"),
        ],
        [
            KeyboardButton(text="💳 Métodos de Pago"),
            KeyboardButton(text="👨‍💻 Soporte"),
        ],
        [
            KeyboardButton(text="🕒 Horario"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Selecciona un servicio 👇",
)


def boton_comprar():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛒 Comprar ahora",
                    url="https://t.me/soportenissi",
                )
            ]
        ]
    )