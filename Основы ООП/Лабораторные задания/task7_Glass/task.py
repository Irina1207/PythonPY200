from typing import Union


#  создать класс Glass
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]) -> None:
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if not occupied_volume > 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water ()

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)


К ранее созданному классу `Glass`, добавьте методы `add_water`, `remove_water`.
Обязательно проверяйте типы (`TypeError`) и значения переменных (`ValueError`).

Если количество добавляемой воды больше свободного места или
объем выливаемой воды больше имеющейся воды,
то должна быть сгенерирована ошибка `ValueError`.

Вызовите методы `add_water` и `remove_water`.
Убедитесь, что методы правильно изменяют атрибут `occupied_volume`.
