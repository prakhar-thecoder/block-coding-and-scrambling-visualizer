import plot
import plot

def B8ZS(pattern):
    new_pattern = []
    last_non_zero = -1

    i = 0
    while i < (len(pattern)):
        if pattern[i] == "1":
            new_pattern.append(1 if last_non_zero == -1 else -1)
            last_non_zero = 1 if last_non_zero == -1 else -1
        else:
            count = 0
            for j in range(i, len(pattern)):
                if pattern[j] == "0" and count < 8:
                    count += 1
                else:
                    break
            
            if count != 8:
                new_pattern.append(0)
            else:
                v = last_non_zero
                b = 1 if v == -1 else -1
                new_pattern.extend([0, 0, 0, v, b, 0, b, v])
                i += 8
                continue
        i += 1

    img = plot.plot_graph(new_pattern, text=pattern)
    return (pattern, new_pattern, img)

def HDB3(pattern):
    new_pattern = []
    last_non_zero = -1
    non_zero_count = 0

    i = 0
    while i < (len(pattern)):
        if pattern[i] == "1":
            new_pattern.append(1 if last_non_zero == -1 else -1)
            last_non_zero = 1 if last_non_zero == -1 else -1
            non_zero_count += 1
        else:
            count = 0
            for j in range(i, len(pattern)):
                if pattern[j] == "0" and count < 4:
                    count += 1
                else:
                    break
            
            if count != 4:
                new_pattern.append(0)
            else:
                v = last_non_zero
                b = 1 if v == -1 else -1

                if non_zero_count % 2 == 0:
                    new_pattern.extend([b, 0, 0, b])
                    last_non_zero = b
                else:
                    new_pattern.extend([0, 0, 0, v])
                    last_non_zero = v
                
                non_zero_count = 0
                i += 4
                continue
        i += 1

    img = plot.plot_graph(new_pattern, text=pattern)
    return (pattern, new_pattern, img)


if __name__ == '__main__':
    data = "11001000001100011100"
    print(HDB3(data))