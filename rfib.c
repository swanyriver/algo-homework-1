#ifdef rec
int fib(int n){
  if(n == 0) return 0;
  if(n == 1) return 1;
  return fib(n-1) + fib(n-2);
}

#else
int fib(int n){
  int fib = 0;
  int a = 1;
  int t = 0;

  for(int i=0;i<n;++i){
    t = fib + a;
    a = fib;
    fib = t;
  }
}
#endif

int main(int argc, char const *argv[])
{
  
  if(argc < 2){
    printf("%s\n", "must supply n term");
    return 1;
  }

  printf("fibinaci[%s] = %d\n", argv[1], fib(atoi(argv[1])));


  return 0;
}