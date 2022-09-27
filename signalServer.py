import time
import numpy
import socket
import struct
import threading


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


class _ClientHandler:
    def __init__(self, conn):
        self.conn = conn

        self.data = b""
        self.sendFlag = [False]

        self.clientOk = [True]

        threading.Thread(target=self._run).start()

    def _run(self):
        while 1:
            time.sleep(0.001)

            if self.sendFlag[0]:
                self.sendFlag[0] = False

                try:
                    self.conn.send(self.data)
                except:
                    print("Client close connection")
                    self.clientOk[0] = False
                    return

    def setData(self, data: bytes):
        #print("Client set data:", self.conn)

        self.data = data
        self.sendFlag[0] = True

    def isOk(self) -> bool:
        return self.clientOk[0]


class SignalServer:
    def __init__(self, serverPort: int):
        self.port = serverPort
        
        self.clients = []

        self.sock = socket.socket()
        self.sock.bind(('', self.port))
        self.sock.listen(16)

    def start(self):
        threading.Thread(target=self._run).start()
        threading.Thread(target=self._close).start()

    def _close(self):
        while threading._main_thread.is_alive():
            time.sleep(0.1)

        self.sock.close()

    def _run(self):
        while 1:
            try:
                conn, addr = self.sock.accept()
            except:
                return

            print("New client:", addr)

            client = _ClientHandler(conn)
            self.clients.append(client)

    def putSamples(self, sampleRate: int, sampleBuff: list, sampleNumType):
        #print("Put samples:", len(sampleBuff))

        samplesLength = len(sampleBuff)

        data: bytes = b""

        sampleNumTypeChar = TypeToChar(sampleNumType)
        
        # Make header
        data += struct.pack("<LLB", *(sampleRate, samplesLength, sampleNumTypeChar.encode()[0]))

        # Put samples buff
        data += struct.pack("<" + sampleNumTypeChar*samplesLength, *sampleBuff)

        client: _ClientHandler
        for client in self.clients:
            if client.isOk():
                client.setData(data)
