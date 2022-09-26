/// \author Семенов Владимир Евгеньевич
/// \file SinusGen.hpp
/// \brief Класс формирователя синуса.

#ifndef _SINUS_GEN_HPP
#define _SINUS_GEN_HPP

#include "./blackfin/fract_math.h"
#include "./types.h"
#include "./software.h"


/// \brief Класс генератора синуса.
///
/// Аргументы шаблона: шаг угла, вычисляемый по формуле:
/// dX = (65536 * 256) / Fd (Гц) * f (Гц)
/// Синус вычисляется по формуле:
/// sin(x) = 3.140625x + 0.02026367 * x^2 - 5.325196 * x^3 + 0.5446778 * x^4 + 1.800293 * x^5.
class SinusGenerator
{
  private:
    fract16 X;															///< Текущее значение угла.
    fract16 amp;														///< Амплитуда сигнала.
    uint32 iX;															///< Текущее значение угла.
    uint32 dX;															///< Приращение шага угла.
    
      
  public:
    /// \brief Инициализация генератора синуса.
    /// \param freq - частота генерируемого сигнала.
    void Init(float freq)
    {
        Init(freq, ADC_SAMPLERATE);
    }
    

    /// \brief Инициализация генератора синуса.
    /// \param freq - частота генерируемого сигнала.
    /// \param samplerate - частота вызова генератора синусоиды
    void Init(float freq, uint32 samplerate) {
        X = 0;
        iX = 0;
        SetFreq(freq, samplerate);
        amp = 0x7FFF;                                                   //Максимально возможная амплитуда сигнала
    }
    
    
    /// \brief Установка значения приращения угла.
    /// \param deltaX - значение приращения. Один градус равен 0x1000000/360.
    void SetDeltaX(uint32 deltaX)
    {
        dX = deltaX;
    }
    
    
    /// \brief Установка значения угла.
    /// \param newX - значение угла. Один градус равен 0x1000000/360.
    void SetX(fract16 newX)
    {
    	iX = newX << 8;
    	X = newX;
    }

    void SetAngle(uint16 angle){
        if (angle >= 0 & angle <= 180){
            SetX(0x7fff * angle / 180);
        } else if (angle > 180 & angle <= 360){
            //SetX();
        }
    }


    /// \brief Установка частоты генератора.
    /// \param freq - частота генерируемого сигнала
    /// \param samplerate - частота вызова генератора синусоиды
    void SetFreq(float freq, uint32 samplerate)
    {
        dX = (0x1000000 * freq) / samplerate;
    }
    
    
    /// \brief Установка амплитуды сигнала.
    /// \param amplitude - устанавливаемая амплитуда сигнала.
    void SetAmp(fract16 amplitude)
    {
        amp = amplitude;
    }
    
    
    /// \brief Запрос установленной амплитуды сигнала.
    /// \return Возвращает установленную амплитуду сигнала.
    fract16 OutAmp(void)
    {
        return amp;
    }
    
    
    /// \brief Получение очередного отсчета формируемого синуса с максимальной амплитудой.
    /// \return Отсчёт генерируемого сигнала с максимально-возможной амплитудой.
    fract16 OutMax()
    {
        // Вычисляем значение синуса для текущего угла.
        // sin(X)  = sin(180 - X), sin(-X) = -sin(X).
        fract16 x = (((X & 0x4000) != 0) ? (negate_fr1x16(X)) : (X)) & 0x7fff;
        fract16 nx = multr_fr1x16(x, x);
        fract32 y = mult_fr1x32(0x3240, x);
        y = add_fr1x32(y, mult_fr1x32(0x0053, nx)); nx = multr_fr1x16(nx, x);
        y = add_fr1x32(y, mult_fr1x32(0xaacc, nx)); nx = multr_fr1x16(nx, x);
        y = add_fr1x32(y, mult_fr1x32(0x08b7, nx)); nx = multr_fr1x16(nx, x);
        y = add_fr1x32(y, mult_fr1x32(0x1cce, nx));
        // Приводим к формату 1.16 (коэфф.были уменьшены в 8 раз) и насыщаем.
        y = shr_fr1x32(y, 16 - 3);

        if((fract16)y < 0)
        {
            y = 0x7fff;
        }
        
        // Если X был отрицательный - Y так-же отрицательный.
        if(X < 0)
        {
            y = negate_fr1x16((fract16)y);
        }
        
        // Увеличиваем значение угла.
        iX += dX;
        X = iX >> 8;
        return (fract16)y;
    }
    
    
    /// \brief Выдача очередного отсчёта с заданной амплитудой amp.
    /// \return Отсчёт генерируемого сигнала с установленной амплитудой.
    fract16 Out()
    {
        return multr_fr1x16(OutMax(), amp);
    }
    
    
    /// \brief Выдача очередного отсчёта с фазовым скачком deltaX и максимальной амплитудой.
    /// \param deltaX - фазовый скачок, приращение фазы.
    /// \return Отсчёт генерируемого сигнала максимальной амплитуды после изменения фазы.
    fract16 OutMax(uint32 deltaX)
    {
        uint32 dXtemp = dX;                                         	//Сохраняем значение dX
        
        dX = deltaX;                                                	//Новое значение dX
        fract16 result = OutMax();                                  	//Вычисление отсчёта с новым dX
        dX = dXtemp;                                                	//Восстанавливаем dX
        
        return result;
    }
    
    
    /// \brief Метод получения очередного отсчёта с фазовым скачком deltaX и амплитутой amp.
    /// \param deltaX - фазовый скачок, приращение фазы.
    /// \return Отсчёт генерируемого сигнала установленного уровня после изменения фазы.
    fract16 Out(uint32 deltaX)
    {
        uint32 dXtemp = dX;                                         	//Сохраняем значение dX
        
        dX = deltaX;                                                	//Новое значение dX
        fract16 result = Out();                                     	//Вычисление отсчёта с новым dX
        dX = dXtemp;                                                	//Восстанавливаем dX
        
        return result;
    }
};

#endif
