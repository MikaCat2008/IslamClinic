import typing as t, collections as c

from database import Database


class Model:
    database: Database
    listeners: c.defaultdict[str, list[t.Callable]]

    def __init_subclass__(cls) -> None:
        cls.listeners = c.defaultdict(list)
        
        return cls

    def get_data(self) -> dict[str, object]:
        return {}

    @classmethod
    def init(cls) -> None:
        ...

    @classmethod
    def reset(cls) -> None:
        cls.listeners = c.defaultdict(list)

    @classmethod
    def emit(cls, event: str, data: dict[str, object]) -> None:
        for listener in cls.listeners[event]:
            listener(**data)

    @classmethod
    def add_listener(cls, event: str, listener: t.Callable) -> None:
        cls.listeners[event].append(listener)

    def __eq__(self, model: 'Model') -> bool:
        return self.get_data() == model.get_data()
