import pyaudio

from signalClient import SignalClient, TypeSize


client = SignalClient("localhost", 9999)

SAMPLE_RATE, samplesLength, sampleNumType, samplesData = next(client.receive())


# Make sound
if True:
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.get_format_from_width(TypeSize(sampleNumType)),
                    channels=1,
                    rate=SAMPLE_RATE,
                    output=True)

    for sampleRate, samplesLength, sampleNumType, samplesData in client.receive():
        print("Received samples:", samplesLength)
        stream.write(samplesData)

# Print buffer
if False:
    for sampleRate, sampleNumType, sampleBuff in client.receiveDecodeBuff():
        print("Received:", sampleBuff)


stream.close()
client.close()