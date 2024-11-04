def encode_24(temp: float, hum: int, dir: str) -> bytes:
    dir_case = {'N': 0, 'NO': 1, 'O': 2, 'SO': 3, 'S': 4, 'SE': 5, 'E': 6, 'NE': 7}
    dir_int = dir_case[dir]
    
    temp_int = int(temp // 1)
    temp_dec = int((temp % 1) * 100)
    
    hum <<= 3
    temp_dec <<= 10
    temp_int <<= 17
    
    result_bits = bin(temp_int | temp_dec | hum | dir_int)[2:]
    result_bits = result_bits.zfill(24)
    
    result_bytes = int(result_bits, 2).to_bytes(3, 'big')

    return result_bytes

def decode_24(msg: bytes) -> tuple:
    dir_int_case = {0: 'N', 1: 'NO', 2: 'O', 3: 'SO', 4: 'S', 5: 'SE', 6: 'E', 7: 'NE'}
    msg_bin = bin(int.from_bytes(msg, 'big'))[2:].zfill(24)
    
    temp_int = int(msg_bin[:7], 2)
    temp_dec = int(msg_bin[7:14], 2)
    
    hum = int(msg_bin[14:21], 2)
    
    dir = int(msg_bin[21:], 2)
    
    return (temp_int + (temp_dec / 100), hum, dir_int_case[dir])

# Este if permite que el código se ejecute solo si se ejecuta directamente
if __name__ == '__main__':
    msg = encode_24(54.35, 44, 'E')
    temp, hum, dir = decode_24(msg)
    print(f"Temperature: {temp}°C, Humidity: {hum}%, Direction: {dir}")
