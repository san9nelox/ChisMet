namespace Lab2
{
    class Program
    {
        private static double _epsilon = 5 * Math.Pow(10, -5);

        public static void Main()
        {
            Jacobi();
            GaussSeidel();
        }

        private static void Jacobi()
        {
            var x1Prev = 0.0;
            var x2Prev = 0.0;
            var x3Prev = 0.0;
            var x1 = 1.39;
            var x2 = 1.63;
            var x3 = 2.6;
            var n = 0;
            while (Math.Abs(x1 - x1Prev) > _epsilon &&
                   Math.Abs(x2 - x2Prev) > _epsilon &&
                   Math.Abs(x3 - x3Prev) > _epsilon)
            {
                n++;
                x1Prev = x1;
                x2Prev = x2;
                x3Prev = x3;
                x1 = (1.39 + 0.2 * x2Prev - 0.1 * x3Prev) / 1.49;
                x2 = 1.63 + 0.1 * x1Prev + 0.1 * x3Prev;
                x3 = 2.6 - 0.4 * x1Prev + 0.4 * x2Prev;
            }

            Console.WriteLine(x1);
            Console.WriteLine(x2);
            Console.WriteLine(x3);
            Console.WriteLine(n);
        }

        private static void GaussSeidel()
        {
            var x1Prev = 0.0;
            var x2Prev = 0.0;
            var x3Prev = 0.0;
            var x1 = 1.39;
            var x2 = 1.63;
            var x3 = 2.6;
            var n = 0;
            while (Math.Abs(x1 - x1Prev) > _epsilon &&
                   Math.Abs(x2 - x2Prev) > _epsilon &&
                   Math.Abs(x3 - x3Prev) > _epsilon)
            {
                n++;
                x1Prev = x1;
                x2Prev = x2;
                x3Prev = x3;
                x1 = (1.39 + 0.2 * x2Prev - 0.1 * x3Prev) / 1.49;
                x2 = 1.63 + 0.1 * x1 + 0.1 * x3;
                x3 = 2.6 - 0.4 * x1 + 0.4 * x2;
            }

            Console.WriteLine(x1);
            Console.WriteLine(x2);
            Console.WriteLine(x3);
            Console.WriteLine(n);
        }
    }
}