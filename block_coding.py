import plot


def map_4B5B(pattern):
    mapping_table = {
        '0000': '11110',
        '0001': '01001',
        '0010': '10100',
        '0011': '10101',
        '0100': '01010',
        '0101': '01011',
        '0110': '01110',
        '0111': '01111',
        '1000': '10010',
        '1001': '10011',
        '1010': '10110',
        '1011': '10111',
        '1100': '11010',
        '1101': '11011',
        '1110': '11100',
        '1111': '11101'
    }

    if (len(pattern) % 4) != 0:
        pattern += '0' * (4 - (len(pattern) % 4))

    chunks = [pattern[i:i+4] for i in range(0, len(pattern), 4)]
    mapped = [mapping_table[chunk] for chunk in chunks]
    mapped = ''.join(mapped)
    mapped = [int(bit) for bit in mapped]
    
    img = plot.plot_graph(mapped, ylim=[-0.1, 1.5], text=mapped)
    return (mapped, mapped, img)


if __name__ == '__main__':
    print(map_4B5B("0000000"))