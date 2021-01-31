using System;
using System.Collections.Generic;
using System.Linq;

namespace DailyAlgorithm.Level_1
{
    public class AddTwo
    {
        private HashSet<int> temp = null;
        private int[] answer = null;

        public AddTwo(int[] numbers)
        {
            AddTwoFunc(numbers, ref answer);
        }

        private void AddTwoFunc(int[] numbers, ref int[] result)
        {
            temp = new HashSet<int>();

            for (int i = 0; i < numbers.Length - 1; i++)
            {
                for (int j = i + 1; j < numbers.Length; j++)
                {
                    temp.Add(numbers[i] + numbers[j]);
                }
            }
            result = temp.ToArray();
            Array.Sort(result);
        }

        public void GetResult()
        {
            for (int i = 0; i < answer.Length; i++)
            {
                Console.Write(answer[i] + " ");
            }
        }
    }
}
