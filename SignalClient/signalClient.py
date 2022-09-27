import time
import numpy
import socket
import struct
import threading

from typing import Tuple


def TypeSize(type: numpy.number):
    if type == numpy.int16:
        size = 2
    elif type == numpy.int32:
        size = 4
    elif type == numpy.float16:
        size = 2
    elif type == numpy.float32:
        size = 4
    elif type == numpy.float64:
        size = 8
    else:
        size = 4

    return size


def CharToType(char: str):
    if char == "h":
        type = numpy.int16
    elif char == "i":
        type = numpy.int32
    elif char == "e":
        type = numpy.float16
    elif char == "f":
        type = numpy.float32
    elif char == "d":
        type = numpy.float64
    else:
        type = numpy.int16

    return type


def TypeToChar(type: numpy.number):
    if type == numpy.int16:
        char = "h"
    elif type == numpy.int32:
        char = "i"
    elif type == numpy.float16:
        char = "e"
    elif type == numpy.float32:
        char = "f"
    elif type == numpy.float64:
        char = "d"
    else:
        char = "i"

    return char


def HeaderSize() -> int:
    return struct.calcsize("<LLB")


def DecodeHeader(data) -> Tuple[int, int, numpy.number]:
    sampleRate, samplesLength, sampleNumTypeChar = struct.unpack_from("<LLB", data, 0)
    sampleNumTypeChar = sampleNumTypeChar.to_bytes(1, byteorder="little").decode()

    sampleNumType = CharToType(sampleNumTypeChar)

    return sampleRate, samplesLength, sampleNumType


def SamplesByteSize(samplesLength, sampleNumType):
    return samplesLength * TypeSize(sampleNumType)


def DecodeData(samplesLength: int, sampleNumType, data) -> list:
    sampleNumTypeChar = TypeToChar(sampleNumType)
        
    sampleBuff = struct.unpack_from("<" + sampleNumTypeChar*samplesLength, data)

    return list(sampleBuff)


class SignalClient:
    def __init__(self, serverIp, serverPort):
        self.sock = socket.socket()
        self.sock.connect((serverIp, serverPort))

    def receive(self):
        while 1:
            headerData = self.sock.recv(HeaderSize())

            if (headerData == b""):
                return 0, 0, None, b""

            sampleRate, samplesLength, sampleNumType = DecodeHeader(headerData)

            samplesData = self.sock.recv(SamplesByteSize(samplesLength, sampleNumType))

            yield sampleRate, samplesLength, sampleNumType, samplesData

    def receiveDecodeBuff(self):
        for sampleRate, samplesLength, sampleNumType, samplesData in self.receive():
            if sampleRate == 0:
                return 0, None, []

            sampleBuff = DecodeData(samplesLength, sampleNumType, samplesData)

            yield sampleRate, sampleNumType, sampleBuff

    def close(self):
        self.sock.close()

