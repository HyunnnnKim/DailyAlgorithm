using System;

namespace CS.Baekjoon
{
    public class BlackJack
    {
        private int M = 0;
        private int[] nums = null;

        public BlackJack()
        {
            HandleInput();
            CalculateClosest();
        }

        private void HandleInput()
        {
            var dealer = Array.ConvertAll(Console.ReadLine().Split(' '), n => int.Parse(n));
            var i = dealer[0]; M = dealer[1];
            var cards = Array.ConvertAll(Console.ReadLine().Split(' '), n => int.Parse(n));
            if (cards.Length == i)
            {
                nums = cards;
            }
        }

        private void CalculateClosest()
        {

        }

        public void GetResult()
        {
            Console.WriteLine();
        }
    }
}
