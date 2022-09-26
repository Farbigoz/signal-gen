/// \author ������� �������� ����������
/// \file KRLgen.hpp
/// \brief ����� ���������� ������� ���.

#ifndef __KRL_GEN_HPP__
#define __KRL_GEN_HPP__

#include "SinusGen.hpp"
#include "software.h"
#include "types.h"

/// \brief ����� ���������� �������� ���
class KRLgen
{
  private:
    SinusGenerator	SinGen;												///< ��������� ������ ���������� ������
    bool            enableBit;                                      	///< ���� ����������� ����������
    bool			workDev;											///< ������� ��������� ����������
    uint8			code;												///< ���
    uint8			trCode;												///< ������������ ���
    T_KRLfreqNum	filterNum;											///< ����� ������� �������
    float			fHi;												///< ������� 1
    float			fLo;												///< ������� 0
    int32			currentSample;										///< ������� ������
    uint16			currentBit;											///< ������� ����� ����

    uint32          samplerate;
    uint16          samplesPerBode;
    
    
  public:
	/// \brief ������������� ������ ���������� �� ��������� ���������� ����������
	/// \param pObFRAM - ��������� �� ��������� ���������� ����������.
	/// \param newChannel - ������������ ����� ��� ��������.
    /// \return 0 - ������ �������������, 1 - ��������� ���������������
	bool Init(uint32 a_samplerate)
    {
		enableBit = false;
		workDev = false;                                    			//��-��������� ��������� ��������

        samplerate = a_samplerate;

		samplesPerBode = samplerate / BODES_PER_SECOND_KRL;

		//��������� ����� �������
		SetCarrier(F_475_HZ);
        SinGen.Init(fHi, samplerate);                                   //��������� �������

		//��������� ���������
		SetLevel(0);

        currentSample = 0;                                        		//������� ������ = 0;
        currentBit = 0;                                            		//������� ��� = 0;

        code = 0x00;

        enableBit = true;

        On();

        return true;
    }


    /// \brief ��������� ��������� ������� ���.
    void On(void)
    {
    	if (!workDev) SinGen.SetX(0);

    	if(enableBit)
    	{
			workDev = true;
			currentSample = 0;                                        	//������� ������ = 0;
			currentBit = 0;                                            	//������� ��� = 0;
    	}
    }
    

    /// \brief ���������� ��������� ������� ���.
    void Off(void)
    {
    	workDev = false;
    }
    

    /// \brief ��������� ������� ������� ������� ���.
	/// \param newFilterNum - ����� ��������������� ������� �������.
	/// \return true - ������� �����������, false - ������� �� ���� ����������� (�������� ���������������� ��������) � �������� �������.
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


    /// \brief ������� ������� ����� ������� �������.
    /// \return ���������� ����� ������������� ������� �������.
    uint8 OutCarrier(void)
    {
    	return (uint8)filterNum;
    }


    /// \brief ������ �������� ��������� ���������� ���.
	/// \return true - ��������� ��������, false - ��������� ��������.
    bool OutState(void)
    {
        return workDev;
    }


    /// \brief ��������� ������������� ����.
	/// \param newCode - ��������������� ������������ ���.
    void SetCode(uint8 newCode)
    {
        code = newCode;
    }
    

    /// \brief ������ �������� ������������ ����.
	/// \return ������� ����������� ���.
    uint8 OutCode(void)
    {
    	return code;
    }
    

    /// \brief ��������� ��������� ������� ���.
	/// \param amplitude - ��������������� ����������� �������� �������.
	/// \return true - ��������� �����������, false - ��������� �� ���� ����������� (���� �������� ������������� ��������) � �������� �������.
    bool SetLevel(fract16 amplitude)
    {
    	if(amplitude >= 0 && amplitude <= 0x7FFF)
    	{
    		SinGen.SetAmp(amplitude);
    		return true;
    	}

    	return false;
    }
    

    /// \brief ������ ������� ��������� �������.
	/// \return �������� ������������� ��������� �������.
    fract16 OutLevel(void)
    {
        return SinGen.OutAmp();
    }


    /// \brief ������ ���������� ������� ������� ���.
	/// \return ������ ������������� ������� ���.

	fract16 _out;


    fract16 Out(void)
    {
        if(!workDev)
        {    //��������� ��������
            return 0;
        }
        
        if(!currentSample--)
        {    //������� ��� �������
            currentSample = samplesPerBode;                		//������� �������� ������������� ����
            
            if(!currentBit--)
            {    //�������� ��� ����
                currentBit = 7;                                    		//������� ������������ ���
                trCode = code;
            }

            //��������� ������������ �������
            SinGen.SetFreq((trCode & 0x80) ? fHi : fLo, samplerate);

            //_out = (trCode & 0x80) ? 0x7fff : 0x0000;
            
            trCode <<= 1;
        }

        //return _out;
        return SinGen.Out();
    }
};

#endif
