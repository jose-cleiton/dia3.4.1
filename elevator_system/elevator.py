from enum import Enum


class Elevator:
    def __init__(self) -> None:
        self.current_floor = 0
        self.door_is_open = False
        self._status = ElevatorStatus.STOPPED

    def move_up(self, destination_floor: int) -> None:
        self.door_is_open = False
        self._status = ElevatorStatus.GOING_UP
        self.current_floor = destination_floor

    def move_down(self, destination_floor: int) -> None:
        self.door_is_open = False
        self._status = ElevatorStatus.GOING_DOWN
        self.current_floor = destination_floor

    def move(self, destination_floor: int) -> None:
        if self.current_floor == destination_floor:
            self.door_is_open = True
            self._status = ElevatorStatus.STOPPED
            return

        if destination_floor > self.current_floor:
            self.move_up(destination_floor)
        else:
            self.move_down(destination_floor)


class ElevatorStatus(Enum):
    STOPPED = 0
    GOING_UP = 1
    GOING_DOWN = 2
    LOCKED = 3
