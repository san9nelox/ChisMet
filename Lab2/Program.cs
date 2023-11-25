namespace Lab2
{
    class Program
    {
        private const double E = Math.E;
        private static double a = 1;
        private static double b = 2;
        private static double _epsilon = 5 * Math.Pow(10, -6);
        public static void Main()
        {
            Dichotomy(a, b);
            Newton(b);
            NewtonModified(b);
            Chords(a, b);
            ChordsMovable(a, b);
            MPI(b);
        }

        private static double Func(double x)
        {
            return Math.Pow(E, -x) - 1.7 + Math.Pow(x, 2);
        }

        private static double FuncDerivative(double x)
        {
            return -Math.Pow(E, -x) + 2 * x;
        }
        private static void Dichotomy(double x, double y)
        {
            var n = 0;
            var k = (y - x) / 2;
            while (k > _epsilon)
            {
                n++;
                k /= 2;
                var x0 = (x + y) / 2;
                if (Func(x) * Func(x0) < 0)
                    y = x0;
                else
                    x = x0;
            }
            Console.WriteLine(x);
            Console.WriteLine(n);
        }

        private static void Newton(double x)
        {
            var n = 0;
            while (Math.Abs(Func(x) / FuncDerivative(x)) > _epsilon)
            {
                n++;
                x -= Func(x) / FuncDerivative(x);
            }
            Console.WriteLine(x);
            Console.WriteLine(n);
        }
        
        private static void NewtonModified(double x)
        {
            var n = 0;
            while (Math.Abs(Func(x) / FuncDerivative(2)) > _epsilon)
            {
                n++;
                x -= Func(x) / FuncDerivative(2);
            }
            Console.WriteLine(x);
            Console.WriteLine(n);
        }
        
        private static void Chords(double x, double y)
        {
            var n = 0;
            var f = Func(y);
            while (Math.Abs(Func(x) / FuncDerivative(x)) > _epsilon)
            {
                n++;
                x -= Func(x) / (Func(x) - f) * (x - y);
            }
            Console.WriteLine(x);
            Console.WriteLine(n);
        }
        
        private static void ChordsMovable(double x, double y)
        {
            var n = 0;
            while (Math.Abs(Func(x) / FuncDerivative(x)) > _epsilon)
            {
                var temp = x;
                n++;
                x -= Func(x) / (Func(x) - Func(y)) * (x - y);
                y = temp;
            }
            Console.WriteLine(x);
            Console.WriteLine(n);
        }

        private static double FuncMPI(double x)
        {
            return Math.Sqrt(1.7 - Math.Pow(E, -x));
        }

        private static double FuncMPIDerivative(double x)
        {
            return Math.Pow(E, -x) / (2 * FuncMPI(x));
        }
        
        private static void MPI(double x)
        {
            var n = 0;
            while (Math.Abs(Func(x) / FuncDerivative(x)) > _epsilon)
            { 
                n++;
                x = FuncMPI(x);
            }
            Console.WriteLine(x);
            Console.WriteLine(n);
        }
    }
}

