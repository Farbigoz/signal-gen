#ifndef __FILTER_DEFINED
#define __FILTER_DEFINED

#include "fract_math.h"


typedef struct
{
    fract16 *coeffs;            /*  filter coefficients            */
    fract16 *delay;             /*  start of delay line            */
    fract16 *p;                 /*  read/write pointer             */
    unsigned short length;      /*  number of coefficients         */
    unsigned short index;       /*  interpolation/decimation index */
} _fir_fr16_state;



typedef _fir_fr16_state fir_state_fr16;



void fir_fr16(const fract16 *input, fract16 *output, unsigned short length, fir_state_fr16 *filter_state) {
    fract16 acc = 0;
    unsigned short indx;

    for (unsigned short i=0; i < length; i++){
        filter_state->delay[filter_state->index] = input[0];

        filter_state->index = filter_state->index + 1;
        if (filter_state->index == filter_state->length) {
            filter_state->index = 0;
        }
    }

    indx = filter_state->index;

    for (unsigned short i=0; i < filter_state->length; i++){
        acc += multr_fr1x16(filter_state->delay[indx], filter_state->coeffs[i]);

        indx++;
        if (indx == filter_state->length){
            indx = 0;
        }
    }

    *output = acc;
}


#endif