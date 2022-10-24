from elevator_system.elevator import Elevator, ElevatorStatus


def test_check_if_the_elevator_is_on_floor_zero():
    elevator = Elevator()
    assert elevator.current_floor == 0


def test_check_if_the_door_is_open():
    elevator = Elevator()
    assert elevator.door_is_open is False


def test_check_the_elevator_status():
    elevator = Elevator()
    assert elevator._status == ElevatorStatus.STOPPED


def test_move_the_elevator_up():
    elevator = Elevator()
    destination_floor = 5
    elevator.move_up(destination_floor)
    assert elevator.door_is_open is False
    assert elevator._status == ElevatorStatus.GOING_UP
    assert elevator.current_floor == destination_floor


def test_move_the_elevator_down():
    elevator = Elevator()
    destination_floor = 5
    elevator.move_down(destination_floor)
    assert elevator.door_is_open is False
    assert elevator._status == ElevatorStatus.GOING_DOWN
    assert elevator.current_floor == destination_floor


def test_move_the_elevator_to_the_same_floor():
    elevator = Elevator()
    destination_floor = 0
    elevator.move(destination_floor)
    assert elevator.door_is_open is True
    assert elevator._status == ElevatorStatus.STOPPED
    assert elevator.current_floor == destination_floor
