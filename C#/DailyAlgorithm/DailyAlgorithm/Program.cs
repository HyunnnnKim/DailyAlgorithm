using System;
using DailyAlgorithm.Level_1;

namespace DailyAlgorithm
{
    class Program
    {
        static void Main(string[] args)
        {
            //string sNums = Console.ReadLine();
            //int[] iNums = Array.ConvertAll(sNums.Split(' '), n => int.Parse(n));
            //AddTwo addTwo = new AddTwo(iNums);
            //addTwo.GetResult();

            int num = Convert.ToInt32(Console.ReadLine());
            TernaryFlip ternaryFlip = new TernaryFlip(num);
            ternaryFlip.GetResult();
        }
    }
}