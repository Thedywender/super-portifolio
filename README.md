<summary>🧑‍💻 O que foi desenvolvido neste Projeto?</summary><br>
<p>Neste projeto, foi desenvolvido conhecimentos em Django e Django Rest Framework. Foi criada uma API para gerenciamento de dados de perfil e projetos em um super portfólio.</p>
<details>
    <summary>📝 Habilidades que foram desenvolvidas:</summary><br>
        <li>Foi utilizado o Django REST Framework para criar endpoints com entidades aninhadas.</li>
        <li>Foi utilizado o módulo Simple JWT para implementar autenticação no Django REST Framework.</li>
        <li>Foi utilizado a aplicação de POO;</li>
        <li>Foi utilizado a escrita de testes para APIS garantindo a implementação de endpoints;</li>
        <li>Foi utilizado o desenvolvimento de páginas Web Server Side;</li>
    </ul>
    </details>
    <summary>🐳 Como rodar o projeto em sua máquina:</summary><br>
        <details><summary>Crie um ambiente virtual:</summary>
            <pre><code class="language-bash">python3 -m venv .venv && source .venv/bin/activate</code></pre>
        </details>
        <details><summary>Instale as dependências:</summary>
            <pre><code class="language-bash">python3 -m pip install -r dev-requirements.txt</code></pre>
        </details>      
        <details><summary>Para Rodar o projeto via Docker</summary><br>
          <summary>Está sendo utilizado um banco de dados chamado `super_portfolio_database`. Já existe um script de criação do banco pronto no arquivo `database/01_create_database.sql` que será copiado para dentro do container. Não altere este script.</summary><br>
        <summary>Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto:</summary>
        <pre><code class="language-bash">docker build -t super-portfolio-db .</code></pre>
            <p>Execute o docker para criar o banco:</p>
            <pre><code class="language-bash">docker run -d -p 3306:3306 --name=super-portfolio-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=super_portfolio_database super-portfolio-db
</code></pre>            
        </details>          
         <details><summary>Para executar as migrações:</summary><br>
           <summary>Popular o banco:</summary>
            <pre><code class="language-bash">python3 manage.py makemigrations</code></pre>
            <p>Execute o migrate:</p>
            <pre><code class="language-bash">python3 manage.py migrate</code></pre>
           <p>Execute o projeto:</p>
            <pre><code class="language-bash">python3 manage.py runserver</code></pre>
    </ul>
