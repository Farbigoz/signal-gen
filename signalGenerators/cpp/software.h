#ifndef __SOFTWARE_H__
#define __SOFTWARE_H__

#include "./types.h"


/// Частота выборок АЦП		(Используется в генераторе синусоиды)
#define ADC_SAMPLERATE              16000
/// Частота демодулятора
#define DEMODULATOR_SAMPLERATE      2000
/// Частота декодера
#define DECODER_SAMPLERATE          50

/// Константа дециматора для декодера
#define DECODER_DECIM_INDX			DEMODULATOR_SAMPLERATE/DECODER_SAMPLERATE

/// Величина буфера усреднения децимации
#define DECIM_BUFF_SIZE				50

/// Время срабатывания компаратора в мс
#define COMPARATOR_DELAY			250



/// Количество несущих частот ТРЦ3
#define CARRIER_FREQ_NUM_TRC3	5

/// Частоты КРЛ ТРЦ 3
typedef enum
{
    F_420_HZ,
    F_480_HZ,
    F_565_HZ,
    F_720_HZ,
    F_780_HZ,
} T_TRC3freqNum;

uint16 T_TRC3freq[CARRIER_FREQ_NUM_TRC3] = {420, 480, 565, 720, 780};

/// Количество частот модуляции
#define MODULATION_FREQ_NUM_TRC3 2

/// Частоты модуляции ТРЦ 3
typedef enum
{
    F_8_HZ,
    F_12_HZ
} T_TRC3modFreqNum;


/// Анализатор спектра
#define TWOPI   6.283185307179586

#define ARS_SPECTRUM_SAMPLERATE     2000
#define ARS_SPECTRUM_WINDOW_SIZE    80
#define ARS_SPECTRUM_BINS_COUNT     6
uint16 ARSspectrumBins[ARS_SPECTRUM_BINS_COUNT] = {3, 5, 7, 9, 11, 13};


/// КРЛ
typedef enum
{
    F_475_HZ,
    F_525_HZ,
    F_575_HZ,
    F_625_HZ,
    F_675_HZ,
    F_725_HZ,
    F_775_HZ,
    F_825_HZ,
    F_875_HZ,
    F_925_HZ
} T_KRLfreqNum;

#define BODES_PER_SECOND_KRL    12.987                                  ///< Бодовая скорость сигнала КРЛ


#endif