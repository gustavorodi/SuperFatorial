# SuperFatorial

- Regras do código

  Solucione o problema do super fatorial de um número N sabendo que ele é definido pelo produto dos N primeiros fatoriais de N. Assim, o super fatorial de 4 é sf(4) = 1! _ 2! _ 3! \* 4! = 288.

  Sua solução deve evitar recalculos desnecessários, ou seja, armazenar em disco/banco de dados/banco chave valor (redis) resultados já calculados para garantir reuso. A solução mais elegante é usar um banco chave valor como o Redis mas você pode inclusive armazenar em um arquivo texto.
