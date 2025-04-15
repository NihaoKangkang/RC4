s_box = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
         58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
         86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
         111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132,
         133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154,
         155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176,
         177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198,
         199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
         221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242,
         243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]

def stream_key_generator(i, j, length):
    k = []
    for r in range(0, length):
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        t = (s_box[i] + s_box[j]) % 256
        k.append(s_box[t])
    return i, j, k


def rc4(seed_key):
    k = []
    # 计算有多少byte
    lenthOfKey = len(seed_key) // 2
    # 种子密钥填充
    for i in range(0 ,256):
        seed_key_hex = seed_key[(i % lenthOfKey) * 2 : (i % lenthOfKey) * 2 + 2]
        k.append(int(seed_key_hex, 16))
    # s表置换
    j = 0
    for i in range(0, 256):
        j = (j + s_box[i] + k[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    # 持续生成流密钥
    i, j = 0, 0
    input_data = input('input data with hex format:')
    while input_data:
        byte_data = bytes.fromhex(input_data)
        lengthOfData = len(byte_data)
        # 保存i，j供持续使用当前轮密钥
        i, j, stream_key = stream_key_generator(i, j, lengthOfData)
        result = b''
        for t in range(0, lengthOfData):
            result += format((stream_key[t] ^ byte_data[t]), '02x').encode()
        print(f"seed_key: {seed_key}, result: {result}")
        # demo演示 收到数据方传递来的16进制加密数据，实时解密为字符串
        # print(f"演示用，方便直接看结果，result: {bytes.fromhex(result.decode())}")
        input_data = input('input data:')