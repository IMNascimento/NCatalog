# NCatalog
Desenvolvimento de um pequeno exemplo de catalogo.
<h1 align="center">
  <br>
  <a href="#"><img src="https://github.com/IMNascimento/DVR/assets/28989407/84028706-5a9e-4d00-af2c-2935e5604035" alt="Nascimento" width="200"></a>
  <br>
  Nascimento
  <br>
</h1>

# Catalogo Nascimento
<p>Esse exemplo é exclusivamente desenvolvido para estudos academicos não há nenhuma responsabilidade de uso indevidos do mesmo. Para o desenvolvimento do mesmo foi usado template no frontend para economizar tempo no desenvolvimento. O projeto em si trata-se de um catalogo podendo ser integrado em qualquer sistema, contando com um sistema de autenticação para cadastrar a foto. O mesmo deve realizar o login para cadastro de pessoas e de imagens. Tendo um crud completo. Foi inserido um sistema de like e deslike nas fotos para deixar como uma opnião não valida do publico de cada imagem, semelhante a do facebook porém sem validações.</p>
<h4>Bibliotecas:</h4>
<p>Algumas bibliotecas foram usadas utilize o pip freeze para instalar todas.</p>

<h4>Build:</h4>
<p>Baixe os arquivos altere as configurações no settings.py  e ligue o seu banco de dados, salve as alterações e depois execute:
</p>

```python
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
<h4>Semeando:</h4>
<p>Para semearmos dados já pre definidos vamos usar o seed:
Primeiro vamos fazer a execução da nossa fixture
</p>
<ul>
    <li>Vamos na pasta do nosso projeto para executarmos o manage.py</li>
    <li>Depois passe o caminho completo do fixture igual iremos mostrar a seguir.</li>
</ul>

```bash
python3 .\manage.py loaddata .\catalogo\fixtures\catalogo.json
```
<p>Depois dessa execução ele vai gerar os dados no banco de dados ai basta iniciar o servidor novamente como o "runserver"</p>


<hr>