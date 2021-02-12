using System;
using System.Collections.Generic;

namespace CS.Programmers.Level_1
{
    public class TernaryFlip
    {
        private int result = 0;

        public TernaryFlip(int decimalNum)
        {
            result = Flip(decimalNum);
        }

        private int Flip(int num)
        {
            List<int> temp = new List<int>();
            int total = 0;

            while (0 <= num)
            {
                temp.Add(num % 3);
                num /= 3;
            }

            temp.Reverse();
            for (int i = 0; i < temp.Count; i++)
            {
                total += (int)(temp[i] * Math.Pow(3, i));
            }

            return total;
        }

        public void GetResult()
        {
            Console.WriteLine(result);
        }
    }
}
