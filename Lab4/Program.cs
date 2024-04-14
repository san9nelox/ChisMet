namespace Lab4
{
    class Program
    {
        private const int A = 2;
        private const int B = 3;
        private static double[] _steps = new[] { 0.1, 0.05, 0.025 };

        public static void Main()
        {
            Console.WriteLine("Метод трапеций");
            foreach (var step in _steps)
            {
                Console.WriteLine($"Шаг: {step}, Результат: {Trapezoids(step)}");
            }

            Console.WriteLine();
            Console.WriteLine("Метод 3/8");

            foreach (var step in _steps)
            {
                Console.WriteLine($"Шаг: {step}, Результат: {Formula38(step)}");
            }
        }

        //Функция из условия
        private static double Func(double x)
        {
            return Math.Cos(x) / (x + 1);
        }

        //Метод трапеций
        private static double Trapezoids(double h)
        {
            var result = 0.0;
            var x = (double)A;
            var m = (int)((B - A) / h);
            for (var i = 0; i < m; i++)
            {
                result += Func(x) + Func(x + h);
                x += h;
            }

            return result * h / 2;
        }

        private static double Formula38(double h)
        {
            var result = 0.0;
            var m = (int)((B - A) / h);
            var x = (double)A;

            for (var i = 0; i < m; i++)
            {
                result += Func(x) + 3 * Func((3 * x + h) / 3) + 3 * Func((3 * x + 2 * h) / 3) +Func(x + h);
                x += h;
            }

            return result * h / 8;
        }
    }
}