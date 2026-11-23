# Padrão de feed Vexter (regra permanente definida por Lucas em 21/10/2026)

Objetivo: feed limpo, premium e técnico, reconhecível mesmo em miniatura na grade do perfil.

## 1. Uma série, um layout
- Posts publicados em sequência (1, 2 ou 3) usam exatamente o mesmo layout, grade, margens, cabeçalho, rodapé e escala tipográfica.
- Os slides se completam: mesma linha visual, numeração e, quando fizer sentido, elemento que atravessa os posts (como o panorama da logo).
- Antes de entregar, gerar a miniatura em grade 3 colunas (`make_grid`, sai como `_grade.png`) e conferir se o conjunto parece de uma só marca.

## 2. Tudo centralizado
- Logo oficial transparente centralizada no topo, sempre no mesmo tamanho (altura 150 px em 1080x1350).
- Kicker, título, texto e CTA centralizados no eixo vertical e horizontal da área segura. Margens laterais 90 px.
- Densidade: no máximo 5 itens por slide de lista; se o script reduzir o texto abaixo de 85%, encurtar em vez de aceitar letra pequena.
- Rodapé centralizado: @somosvexter · n/total e barra de progresso.

## 3. Cores: um tema por série
Temas definidos (usar tokens de `scripts/feed_template.py`):
- **escuro:** fundo preto #000000 com brilho dourado sutil, texto branco, acento #C8A34D. Institucional e impacto.
- **grafite:** fundo #1B1B1B, texto branco, acento #C8A34D. Dashboards, dados, técnico.
- **claro:** fundo branco/#F5F5F5, texto preto, acento dourado escurecido #A8832F. Leitura longa, análises, educativo.
Regras: nunca misturar temas dentro de uma sequência de posts; alternar tema só entre séries e de forma planejada. Outras cores só como acento pontual, definido nos tokens e igual em toda a série. Evitar acentos soltos (vermelho, selos coloridos) que quebram a grade.

## 4. Tipografia
Somente Poppins (títulos, 600/700) e Inter (corpo), embutidas pelo script a partir de `assets/fonts`. Nunca serifa, nunca mistura por post. Títulos em caixa normal, destaque de 1 a 3 palavras em dourado.

## 5. Logo
Somente os arquivos de `assets/`, sem recriar nem aplicar filtros. Mesmo cabeçalho em todos os posts (não alternar entre texto, selo "V" e logo).

## 6. Legendas no mesmo padrão
Estrutura fixa, sem travessões:
1. Abertura = Situação SPIN (1 frase com o gancho ou dado).
2. Contexto = Problema e Implicação SPIN (2 a 3 frases).
3. CTA = Necessidade de solução SPIN, coerente com o estágio (salvar, enviar ao time, comentar palavra-chave, chamar no direct).
4. Fonte e data (quando houver notícia ou norma) e ressalva técnica curta.
5. Hashtags: de 4 a 6, específicas.
Mesmo tom das artes (técnico, consultivo, direto), mesma terminologia e mesmos títulos usados nos slides.

## 7. Checklist antes de enviar
[ ] Mesmo tema e mesmo layout em todos os slides da série
[ ] Tudo centralizado e dentro da área segura
[ ] Logo oficial transparente, mesmo tamanho e posição
[ ] Só Poppins e Inter
[ ] Miniatura em grade 3x3 coerente
[ ] Legenda no padrão e coerente com as artes
[ ] Sequência SPIN completa (S, P, I, N) nas artes e na legenda
[ ] Sem travessões; fontes e datas conferidas
[ ] Conteúdo tributário/normativo validado por um sócio antes de publicar
