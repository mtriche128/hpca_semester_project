/***************************************************************************\\**
 * @file   libcbm.c
 * @brief  This file defines C functions which will serve as benchmarks.
 * @author Matthew Triche
 * 
 * "C Benchmark Library"
 * Within this source file, various functions are implemented which shall be
 * used for performance testing. This source file is written such that it shall
 * be compiled to a shared object.
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights 
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
 * copies of the Software, and to permit persons to whom the Software is 
 * furnished to do so, subject to the following conditions:
 * 
 * The above permission notice shall be included in all copies or substantial 
 * portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
 * SOFTWARE.
 ******************************************************************************/

#include <limits.h>
#include <stdint.h>

/* -------------------------------------------------------------------------- *
 * Define Macros and Constants                                                *
 * -------------------------------------------------------------------------- */

/* 
 * EXPORT
 * This prefix should be used in the declaration/definition of any function
 * intended to be called from outside the shared object.
 */

#define EXPORT extern

/* -------------------------------------------------------------------------- *
 * Declare Exported Functions                                                 *
 * -------------------------------------------------------------------------- */

EXPORT void popcnt32n(uint32_t *p_in, uint32_t *p_out, uint32_t size);
EXPORT void bitrev32n(uint32_t *p_in, uint32_t *p_out, uint32_t size);
EXPORT void lib_free(void);

/* -------------------------------------------------------------------------- *
 * Define Exported Functions                                                  *
 * -------------------------------------------------------------------------- */

/**
 * @brief Element-wise population count of a buffer composed of 32-bit values.
 * 
 * @param[in]  p_in  Pointer to the input buffer.
 * @param[out] p_out Pointer to the output buffer.
 */

EXPORT void popcnt32n(uint32_t *p_in, uint32_t *p_out, uint32_t size)
{
	uint32_t sum;
	uint32_t val;
	
	while(size--)
	{
		val = *(p_in++);
		for(sum=0; val; sum++)
		{
			val &= val - 1;
		}
		*(p_out++) = sum;
	}
}

/**
 * @brief Element-wise bit reversal of a buffer composed of 32-bit values.
 * 
 * @param[in]  p_in  Pointer to the input buffer.
 * @param[out] p_out Pointer to the output buffer.
 */

EXPORT void bitrev32n(uint32_t *p_in, uint32_t *p_out, uint32_t size)
{
	uint32_t bits;
	uint32_t word_in;
	uint32_t word_out;
	
	while(size--)
	{
		bits     = CHAR_BIT*sizeof(uint32_t) - 1;
		word_in  = *(p_in++);
		word_out = word_in;
		
		for (word_in >>= 1; word_in; word_in >>= 1)
		{   
			word_out <<= 1;
			word_out |= word_in & 1;
			bits--;
		}
		word_out <<= bits; 
		
		*(p_out++) = word_out;
	}
}

/**
 * @brief Free any memory allocated within the shared-object.
 */

EXPORT void lib_free(void)
{
	/* 
	 * TODO: If memory is allocated anywhere within the shared object, ensure
	 *       it's freed within this function. This function will be called by
	 *       the python interface's destructor.
	 */
}
