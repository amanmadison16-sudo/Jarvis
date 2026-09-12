# -*- coding: utf-8 -*-
"""
Jarvis v0.1 — базовый запуск.
Проверяем, что APK собирается и работает.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

Window.clearcolor = (0.0, 0.0, 0.0, 1)


class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical",
                         padding=dp(20),
                         spacing=dp(20), **kwargs)

        # Заголовок
        self.title = Label(
            text="[b]JARVIS[/b]",
            markup=True,
            font_size="42sp",
            color=(0.04, 0.52, 1.0, 1),
            size_hint_y=None,
            height=dp(80),
        )
        self.add_widget(self.title)

        # Статус
        self.status = Label(
            text="Система инициализирована\n\nВерсия 0.1\n\nГотов к работе, сэр.",
            font_size="18sp",
            color=(0.9, 0.9, 0.9, 1),
            halign="center",
        )
        self.add_widget(self.status)

        # Кнопка
        self.btn = Button(
            text="Проверить связь",
            size_hint=(1, None),
            height=dp(60),
            background_normal="",
            background_color=(0.04, 0.52, 1.0, 1),
            font_size="18sp",
            bold=True,
        )
        self.btn.bind(on_release=self.on_click)
        self.add_widget(self.btn)

    def on_click(self, *args):
        self.status.text = "Связь установлена, сэр.\n\nВсе системы работают."


class JarvisApp(App):
    title = "Jarvis"

    def build(self):
        return JarvisUI()


if __name__ == "__main__":
    JarvisApp().run()
