def get_combo_operand(operand: int, register: list[int]):
    assert operand != 7
    if operand <= 3:
        return operand
    
    return register[operand%4]

def adv(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    register[0] = int(str(register[0] / pow(2, get_combo_operand(operand, register))).split(".")[0])
    return (instruction_pointer + 2, False, None)

def bxl(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    register[1] = register[1] ^ operand
    return (instruction_pointer + 2, False, None)

def bst(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    register[1] = get_combo_operand(operand, register) % 8
    return (instruction_pointer + 2, False, None)

def jnz(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    if register[0] == 0:
        return (instruction_pointer + (0 if jumped else 2), False, None)
    return (operand, True, None)

def bxc(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    register[1] = register[1] ^ register[2]
    return (instruction_pointer + 2, False, None)

def out(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    return (instruction_pointer + 2, False, get_combo_operand(operand, register) % 8)

def bdv(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    register[1] = int(str(register[0] / pow(2, get_combo_operand(operand, register))).split(".")[0])
    return (instruction_pointer + 2, False, None)

def cdv(operand: int, register: list[int], instruction_pointer: int, jumped: bool) -> tuple[int,bool,str]:
    register[2] = int(str(register[0] / pow(2, get_combo_operand(operand, register))).split(".")[0])
    return (instruction_pointer + 2, False, None)

operations = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}