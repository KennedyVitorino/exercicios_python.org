# 16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

def fibonacci_ate_500_while():
    termo_atual = 0
    termo_anterior = 1
    while termo_atual < 500:
        print(termo_atual)
        proximo_termo = termo_atual + termo_anterior
        termo_anterior = termo_atual
        termo_atual = proximo_termo
  
    
def main():
    fibonacci_ate_500_while()
    
    
if __name__ == '__main__':
    main()
    