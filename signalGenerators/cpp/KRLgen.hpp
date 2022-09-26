/// \author Семенов Владимир Евгеньевич
/// \file KRLgen.hpp
/// \brief Класс генератора сигнала КРЛ.

#ifndef __KRL_GEN_HPP__
#define __KRL_GEN_HPP__

#include "SinusGen.hpp"
#include "software.h"
#include "types.h"

/// \brief Класс генератора сигналов КРЛ
class KRLgen
{
  private:
    SinusGenerator	SinGen;												///< Экземпляр класса генератора синуса
    bool            enableBit;                                      	///< Флаг исправности устройства
    bool			workDev;											///< Признак включения генератора
    uint8			code;												///< Код
    uint8			trCode;												///< Передаваемый код
    T_KRLfreqNum	filterNum;											///< Номер несущей частоты
    float			fHi;												///< Частота 1
    float			fLo;												///< Частота 0
    int32			currentSample;										///< Текущий отсчёт
    uint16			currentBit;											///< Текущий номер бита

    uint32          samplerate;
    uint16          samplesPerBode;
    
    
  public:
	/// \brief Инициализация класса значениями из структуры постоянных параметров
	/// \param pObFRAM - указатель на структуру постоянных параметров.
	/// \param newChannel - используемый канал для передачи.
    /// \return 0 - ошибка инициализации, 1 - генератор инициализирован
	bool Init(uint32 a_samplerate)
    {
		enableBit = false;
		workDev = false;                                    			//По-умолчанию генератор выключен

        samplerate = a_samplerate;

		samplesPerBode = samplerate / BODES_PER_SECOND_KRL;

		//Установка новой несущей
		SetCarrier(F_475_HZ);
        SinGen.Init(fHi, samplerate);                                   //Настройка несущей

		//Настройка амплитуды
		SetLevel(0);

        currentSample = 0;                                        		//Текущий отсчёт = 0;
        currentBit = 0;                                            		//Текущий шаг = 0;

        code = 0x00;

        enableBit = true;

        On();

        return true;
    }


    /// \brief Включение генерации сигнала КРЛ.
    void On(void)
    {
    	if (!workDev) SinGen.SetX(0);

    	if(enableBit)
    	{
			workDev = true;
			currentSample = 0;                                        	//Текущий отсчёт = 0;
			currentBit = 0;                                            	//Текущий шаг = 0;
    	}
    }
    

    /// \brief Выключение генерации сигнала КРЛ.
    void Off(void)
    {
    	workDev = false;
    }
    

    /// \brief Установка частоты несущей сигнала КРЛ.
	/// \param newFilterNum - номер устанавливаемой частоты несущей.
	/// \return true - частота установлена, false - частота не была установлена (передано недействительное значение) и осталась прежней.
    bool SetCarrier(uint8 a_newFilterNum)
    {
        T_KRLfreqNum newFilterNum = (T_KRLfreqNum)a_newFilterNum;

    	if(newFilterNum >= F_475_HZ && newFilterNum <= F_925_HZ)
    	{
			filterNum = newFilterNum;
			fHi = 475 + newFilterNum * 50 + 11;
			fLo = 475 + newFilterNum * 50 - 11;
			return true;
    	}

    	return false;
    }


    /// \brief Вернуть текущий номер несущей частоты.
    /// \return Возвращает номер установленной частоты несущей.
    uint8 OutCarrier(void)
    {
    	return (uint8)filterNum;
    }


    /// \brief Запрос текущего состояния генератора КРЛ.
	/// \return true - генератор работает, false - генератор выключен.
    bool OutState(void)
    {
        return workDev;
    }


    /// \brief Установка передаваемого кода.
	/// \param newCode - устанавливаемый передаваемый код.
    void SetCode(uint8 newCode)
    {
        code = newCode;
    }
    

    /// \brief Запрос текущего настроенного кода.
	/// \return Текущий настроенный код.
    uint8 OutCode(void)
    {
    	return code;
    }
    

    /// \brief Установка амплитуды сигнала КРЛ.
	/// \param amplitude - устанавливаемое амплитудное значение сигнала.
	/// \return true - амплитуда установлена, false - амплитуда не была установлена (было передано отрицательное значение) и осталась прежней.
    bool SetLevel(fract16 amplitude)
    {
    	if(amplitude >= 0 && amplitude <= 0x7FFF)
    	{
    		SinGen.SetAmp(amplitude);
    		return true;
    	}

    	return false;
    }
    

    /// \brief Запрос текущей амплитуды сигнала.
	/// \return Значение установленной амплитуды сигнала.
    fract16 OutLevel(void)
    {
        return SinGen.OutAmp();
    }


    /// \brief Выдача очередного отсчёта сигнала КРЛ.
	/// \return отсчёт генерируемого сигнала КРЛ.

	fract16 _out;


    fract16 Out(void)
    {
        if(!workDev)
        {    //Генератор выключен
            return 0;
        }
        
        if(!currentSample--)
        {    //Текущий бит передан
            currentSample = samplesPerBode;                		//Счётчик отсчётов передаваемого бита
            
            if(!currentBit--)
            {    //Переданы все биты
                currentBit = 7;                                    		//Счётчик передаваемых бит
                trCode = code;
            }

            //Установка передаваемой частоты
            SinGen.SetFreq((trCode & 0x80) ? fHi : fLo, samplerate);

            //_out = (trCode & 0x80) ? 0x7fff : 0x0000;
            
            trCode <<= 1;
        }

        //return _out;
        return SinGen.Out();
    }
};

#endif
