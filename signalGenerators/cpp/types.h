/**
\author Семенов Владимир Евгеньевич
\file types.h
\brief Объявления нестандартных типов данных.
*/

#ifndef __TYPES_H__
#define __TYPES_H__

/// Тип беззнакового целого размером в 1 байт.
typedef     unsigned char                   BYTE;
#define     MAX_BYTE                        (BYTE)-1

/// Тип беззнакового целого размером в 2 байта.
typedef     unsigned short int              WORD16;
#define     MAX_WORD16                      (WORD16)-1
#define     LO_BYTE(word)                   BYTE(word)
#define     HI_BYTE(word)                   BYTE((word) >> 8)
#define     MAKE_WORD16(lo_byte, hi_byte)   (((WORD16)(hi_byte) << 8) | lo_byte)

/// Тип беззнакового целого размером в 4 байта.
typedef     unsigned long int               WORD32;
#define     MAX_WORD32                      (WORD32)-1
#define     LO_WORD16(dword)                WORD16(dword)
#define     HI_WORD16(dword)                WORD16((dword) >> 16)
#define     MAKE_WORD32(lo_word, hi_word)   (((WORD32)(hi_word) << 16) | lo_word)

/// Тип индексной переменной размером в 2 байта.
typedef     WORD16                          IDX;
#define     BAD_IDX                         (IDX)-1

/// Макрокоманда определения числа элементов в массиве.
#define     items(T)                        (sizeof(T) / sizeof((T)[0]))

/// Более понятные типы
/// Беззнаковые
typedef     unsigned char       uint8;
typedef     unsigned short      uint16;
typedef     unsigned long int   uint32;
typedef		unsigned long long	uint64;
/// Знаковые
typedef     signed char         int8;
typedef     signed short        int16;
typedef     signed long int     int32;
typedef		signed long long	int64;



/// Тип указатель на функцию обратного вызова
typedef void (*pCALLBACK_FUNC)(void);

/// Максимум двух чисел
#define MAX(a, b)		((a) > (b) ? (a) : (b))

/// Перестановка байт в слове
#define SWAP_BYTE(word)	MAKE_WORD16(HI_BYTE(word), LO_BYTE(word))

#endif
