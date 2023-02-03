# Algorítmo de Thomas
## Aula 2 - Anexo 1 (20/01)

---

- É um método algébrico que consiste em uma simplificação da Eliminação de Gauss para resolução de sistemas de equação tridiagonais.
- Uma matriz tridiagonal é uma matriz quadrada onde apenas os elementos da diagonal principal (main), e as que estão diretamente a cima (up) e a baixo (down) a ela são não nulas. Ela pode ser descrita como:

    $$a_i x_i + b_i x_i + c_i x_i = d_i$$

    onde $a_1 = 0$ e $c_n = 0$

- A representação na forma matricial se dá por:

  $$
  
    \left[ {\begin{array}{ccc}
      b_1 & c_1 &  &   & 0 \\
      a_2 & b_2 & c_2 & \\
      & a_3 & b_3 &  \\
      \dots & \dots & \dots & \dots & \dots\\
       & & a_{n-1} & b_{n-1} & c_{n-1}\\
       0 & & & a_{n} & b_n
    \end{array} } \right] 
    \left[ {\begin{array}{c}
      x_1\\
      x_2\\
      x_3\\
      \dots\\
      x_{n-1}\\
      x_{n}\\       
    \end{array} } \right] 
    =
    \left[ {\begin{array}{c}
      d_1\\
      d_2\\
      d_3\\
      \dots\\
      d_{n-1}\\
      d_{n}\\       
    \end{array} } \right] 
  $$

- O primeiro passo do algorítmo de Thomas consiste em alterar os coeficientes da seguinte forma:

    $$\boxed{c_i' = 
    \begin{cases}
        \frac{c_i}{b_i}, i = 1\\
        \frac{c_i}{b_i - c_{i-1}' a_i}, i = 2, 3, \dots, n
    \end{cases}}
    $$
    
    Da mesma forma:

    $$\boxed{d_i' = 
    \begin{cases}
        \frac{d_i}{b_i}, i = 1\\
        \frac{d_i - d_{i-1}' a_i}{b_i - c_{i-1}' a_i}, i = 2, 3, \dots, n
    \end{cases}}
    $$

- Ao final deste primeiro passo, as operações nos $c$'s e $d$'s são feitas ao mesmo tempo, obtendo-se a seguinte matriz:



$$  
    \left[ {\begin{array}{ccc}
      1 & c_1' &  &   & 0 \\
      0 & 1 & c_2' & \\
      & 0 & 1 &  \\
      \dots & \dots & \dots & \dots & \dots\\
       & & 0 & 1 & c_{n-1}'\\
       0 & & & 0 & 1
    \end{array} } \right] 
    \left[ {\begin{array}{c}
      x_1\\
      x_2\\
      x_3\\
      \dots\\
      x_{n-1}\\
      x_{n}\\       
    \end{array} } \right] 
    =
    \left[ {\begin{array}{c}
      d_1'\\
      d_2'\\
      d_3'\\
      \dots\\
      d_{n-1}'\\
      d_{n}'\\       
    \end{array} } \right] 
  $$

  A solução é facilmente obtida pela substituição de volta:

  $$x_n = d_n'$$

  $$x_i = d_i' - c_i' x_{i+1}, i = 1, 2, \dots, n-1$$