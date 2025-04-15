from rc4 import *

if __name__ == "__main__":


    inputKey = input(
        'Input 5 to 256 bytes seed key in hex (like \'0123456789abcdef\', input nothing to abort): ')

    try:
        # 输入密钥必须满足5 - 256 整数 字节
        if len(inputKey) >= 10 and len(inputKey) <= 512 and (len(inputKey) % 2 == 0):
            print('DES decode result: ', rc4(inputKey))
        else:
            print("Check input data.")
    except ValueError:
        print("Check input data.")
    # if len(inputKey) >= 10 and len(inputKey) <= 512:
    #     print('DES decode result: ', rc4(inputKey))
    # else:
    #     print("Check input data.")
    # if inputData and (len(inputKey) == 14 or len(inputKey) == 16):
    #     encodeFlag = input("Do you want to encode(y)/decode(n) this data?(Y/n): ")
    #     if encodeFlag == 'y' or encodeFlag == 'Y' or encodeFlag == '':
    #         result = des_encode(inputData, int(inputKey, 16), len(inputKey))
    #         print('DES encode result: ', result.hex() if isinstance(result, bytes) else result)
    #     else:
    #         print('DES decode result: ', des_decode(inputData, int(inputKey, 16), len(inputKey)))
    # else:
    #     print("Check input data.")
