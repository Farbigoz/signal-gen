#ifndef _FRACT_MATH_H
#define _FRACT_MATH_H

#include "fract_typedef.h"

static fract16 negate_fr1x16(fract16 x) {
    return 0xffff-x;
}

static fract16 multr_fr1x16(fract16 a, fract16 b) {
  fract16 rval = (fract16)(((fract32)a * (fract32)b) >> 15);
  return rval;
}

static fract16 add_fr1x16(fract16 a, fract32 b) {
    fract32 rval = a + b;
    
    if (rval < 0x8000) {
        return rval;
    } else {
        return -0xffff - rval;
    }
}

static fract32 mult_fr1x32(fract16 a, fract16 b) {
  fract32 rval = (((fract32)a * (fract32)b) << 1);
  return rval;
}

static fract32 add_fr1x32(fract32 a, fract32 b) {
    fract32 rval = a + b;
    
    if (rval < 0x80000000) {
        return rval;
    } else {
        return -0xffffffff - rval;
    }
}

static fract32 shr_fr1x32(fract32  a, short  b) {
  fract32 rval = a >> b;
  return rval;
}

#endif