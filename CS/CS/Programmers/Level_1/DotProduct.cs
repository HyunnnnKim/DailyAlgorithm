using System;

namespace CS.Programmers.Level_1
{
    public class DotProduct
    {
        private int _result = 0;

        public DotProduct(int[] a, int[] b)
        {
            if (a.Length == b.Length)
            {
                for (int i = 0; i < a.Length; i++)
                {
                    _result += a[i] * b[i];
                }
            }
        }

        public int GetResult => _result;
    }
}
