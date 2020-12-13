from rich import print


def values():

    with open("input.txt") as f:
        my_input = f.read().splitlines()

    return my_input

def puzzle1():

    data = values()

    accumulator = 0
    position = 0
    instruction_history = []

    while position not in instruction_history:
        if data[position].startswith('nop'):
            instruction_history.append(position)
            position += 1

        if data[position].startswith('acc'):
            instruction_history.append(position)
            accumulator += int(data[position].split()[1])
            position += 1

        if data[position].startswith('jmp'):
            instruction_history.append(position)
            position += int(data[position].split()[1])
    else:
        pass

    return accumulator

def puzzle2():

    data = values()
    
    accumulator = 0
    position = 0
    instruction_history = []
    num_instruction = len(data)

    counter = 0

    nops = [i for i, x in enumerate(data) if x.startswith('nop')]
    jmps = [i for i, x in enumerate(data) if x.startswith('jmp')]


    for jmp in jmps:
        data = values()
        data[jmp] = 'nop ' + data[jmp].split()[1]
        print(data[jmp])
        if counter > 800:
            print(counter)
            pass
        else:
            while position <= num_instruction:
                if data[position].startswith('nop'):
                    instruction_history.append(position)
                    position += 1

                if data[position].startswith('acc'):
                    instruction_history.append(position)
                    accumulator += int(data[position].split()[1])
                    position += 1

                if data[position].startswith('jmp'):
                    instruction_history.append(position)
                    position += int(data[position].split()[1])

            else:
                print(accumulator)

            counter += 1

    # instruction_history = []
# 
    # for nop in nops:
    #     data = values()
    #     data[nop] = 'jmp ' + data[nop].split()[1]
    #     print(data[nop])
# 
    #     while position <= num_instruction:
    #         if position in instruction_history:
    #             break
# 
    #         if data[position].startswith('nop'):
    #             instruction_history.append(position)
    #             position += 1
# 
    #         if data[position].startswith('acc'):
    #             instruction_history.append(position)
    #             accumulator += int(data[position].split()[1])
    #             position += 1
# 
    #         if data[position].startswith('jmp'):
    #             instruction_history.append(position)
    #             position += int(data[position].split()[1])
# 
    #     else:
    #         print(accumulator)


    
    






if __name__ == "__main__":

    puzzle2()
    # print(puzzle1())