# Desafio das Oito Rainhas

O desafio das 8 rainhas é um quebra-cabeça lógico que envolve posicionar oito rainhas em um tabuleiro de xadrez 8x8 de forma que nenhuma delas possa atacar outra. Isso significa que nenhuma rainha pode compartilhar a mesma linha, coluna ou diagonal com outra rainha, evitando assim que fiquem em "xeque".

<img width="189" alt="image" src="https://github.com/mayumi1982/eight_queen/assets/70608757/5fd915bd-8019-476d-8a90-ff3469ec3c49">

Neste desafio, a tarefa proposta é completar a função nQueen(), que recebe 'n' como parâmetro de entrada e retorna uma lista contendo todas as configurações possíveis do tabuleiro de xadrez, organizadas em ordem de classificação. Se não houver solução, a função deve retornar uma lista vazia.

Foi realizado um aprimoramento implementando uma interface gráfica em Python usando o Tkinter. O objetivo dessa aplicação é coletar a entrada do usuário, que deve ser um número de 1 a 8, e exibir a solução em um tabuleiro de xadrez 8x8. Cada número é associado a uma cor para melhorar a visualização.

## Lógica Utilizada

Para resolver este problema, foi aplicada a lógica computacional de Backtracking. Essencialmente, é um método que realiza uma busca exaustiva, ou seja, explora todas as possíveis soluções de um problema por meio de "tentativa e erro". No contexto das 8 rainhas, o algoritmo de backtracking tenta posicionar cada rainha em uma coluna, verificando se pode ser colocada sem atacar outras rainhas já posicionadas.

Se a rainha atual não puder ser colocada em uma posição válida na coluna atual, o algoritmo retrocede para a coluna anterior e tenta posicionar a rainha em outro local. Esse processo continua até que todas as rainhas estejam posicionadas de modo que nenhuma delas ataque outra.

#### Verificação de Segurança para Posicionar uma Rainha em uma Posição Específica:

<img width="296" alt="image" src="https://github.com/mayumi1982/eight_queen/assets/70608757/84cda7b8-011e-40f6-8d9b-1a8985ef5e37">

#### Resolução do Problema das N Rainhas usando Backtracking:

<img width="337" alt="image" src="https://github.com/mayumi1982/eight_queen/assets/70608757/e6a3c337-436e-4945-a894-91274fba8488">

#### Encontrando Todas as Soluções do Problema das N Rainhas:

<img width="359" alt="image" src="https://github.com/mayumi1982/eight_queen/assets/70608757/4c0c9a79-b7c4-49c4-aa69-ac9d898532b7">

#### Exibição da solução da interface gráfica com a função n_queens():

<img width="404" alt="image" src="https://github.com/mayumi1982/eight_queen/assets/70608757/ac1cc70d-6dda-4aa1-b961-132d0dad987d">




