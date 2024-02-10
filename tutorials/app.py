# пишу абсолютно никуда не подглядывая, просто что есть в памяти
# почему код сильный или чистый?
# 1. Он максимально использует библиотеки python, где уже всё прописано (т.е. использует исходный код, который претерпел уже не один релиз, от того является надёжным)
# 2. Даёт описание функции, что она делает
# 3. С помощью библиотек, колбек функции максимально сокращает код
# 4. class описывает максимально полно функционал работы с окнами, это сокращает количество классов которые нужно запомнить программисту

# Что данный код делает?
# До конца понять не смог, думаю что управляет окнами. Все функции, точно не перечислю так как не смог их прочитать

# Роман: class создавал лишь однажды, и четно говоря не помню, для чего он (есть мысль, того что она создаётся для каких-то однотипных объектов).
# Роман: объявляем функцию, далее называем её, у неё два параметра.
class WindowSet(MutableSet):
    def __init__(self, app: App):  # Роман: не знаю что обозначает в параметре app значение App
        """A collection of windows managed by an app.

        A window is automatically added to the app when it is created, and removed when
        it is closed. Adding a window to an App's window set automatically sets the
        :attr:`~toga.Window.app` property of the Window.
        """
        self.app = app  # Роман: не понимаю
        # Роман: по идее должна выполниться некая функция set(), что перед ней не знаю
        self.elements = set()

    def add(self, window: Window) -> None:  # Роман: здесь по идее колбек функции, как в javascript (но я данную тему = колбек функций не понял, хотя она вроде как призвана сократить код)
        # Роман: условие, но корректно почитать его не могу
        if not isinstance(window, Window):
            # Роман: не понимаю
            raise TypeError("Can only add objects of type toga.Window")
        # Silently not add if duplicate
        if window not in self.elements:
            self.elements.add(window)
            window.app = self.app

    def discard(self, window: Window) -> None:
        if not isinstance(window, Window):
            raise TypeError("Can only discard objects of type toga.Window")
        if window not in self.elements:
            # Роман: здесь используется f строка, которая позволяет запускать функции, или склеивать что-то с чем-то
            raise ValueError(f"{window!r} is not part of this app")
        self.elements.remove(window)

    ######################################################################
    # 2023-10: Backwards compatibility
    ######################################################################

    def __iadd__(self, window: Window) -> None:
        # The standard set type does not have a += operator.
        warn(
            "Windows are automatically associated with the app; += is not required",
            DeprecationWarning,
            stacklevel=2,
        )
        return self  # Роман: return окончание функции

    def __isub__(self, other: Window) -> None:
        # The standard set type does have a -= operator, but it takes sets rather than
        # individual items.
        warn(
            "Windows are automatically removed from the app; -= is not required",
            DeprecationWarning,
            stacklevel=2,
        )
        return self

    ######################################################################
    # End backwards compatibility
    ######################################################################

    def __iter__(self) -> Iterator:
        return iter(self.elements)

    def __contains__(self, value: Window) -> bool:
        return value in self.elements

    def __len__(self) -> int:
        return len(self.elements)
