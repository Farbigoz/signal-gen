cdef extern from "./cpp/blackfin/fract_typedef.h":
    ctypedef short fract16
    ctypedef long  fract32

cdef extern from "./cpp/types.h":
    ctypedef unsigned char      uint8
    ctypedef unsigned short     uint16
    ctypedef unsigned long int  uint32
    ctypedef unsigned long long uint64

cdef extern from "./cpp/KRLgen.hpp":
    cppclass KRLgen:
        bint Init(uint32)
        bint SetCarrier(uint8)
        void SetCode(uint8)
        bint SetLevel(fract16)
        uint8 OutCarrier()
        fract16 OutLevel()
        fract16 Out()


# Api for CPP SinusGenerator
cdef class CPPKrlGen:
    cdef KRLgen genKRL

    def __cinit__(self, uint32 samplerate):
        self.genKRL.Init(samplerate)

    cpdef bint SetCarrier(self, uint8 carrier):
        self.genKRL.SetCarrier(carrier)

    cpdef void SetAmp(self, fract16 amp):
        self.genKRL.SetLevel(amp)

    cpdef void SetCode(self, uint8 code):
        self.genKRL.SetCode(code)

    cpdef fract16 Out(self):
        return self.genKRL.Out()
