<h1>Sistema de Autenticação de Usuário com Firebase em Python</h1>

<p>Este projeto é um sistema simples de autenticação de usuário desenvolvido em Python, projetado para ajudar proprietários de softwares pagos a gerenciar o acesso dos usuários. O sistema permite que o proprietário informe a quantidade de dias que o usuário vai utilizar seu software, fornecendo seu nome registrado e a duração do acesso (em dias). A autenticação e o gerenciamento dos dados de usuário são realizados utilizando o Firebase, uma plataforma de desenvolvimento de aplicativos oferecida pelo Google.</p>

<h2>Funcionalidades</h2>
<ul>
    <li><strong>Registro de Usuário</strong>: Apenas o proprietário do software pode atualizar a quantidade de dias que o usuários tem acesso ao seu programa</li>
    <li><strong>Autenticação Segura</strong>: Senhas dos usuários são armazenadas de forma segura usando Firebase Authentication e Bcrypt.</li>
    <li><strong>Gerenciamento de Acesso</strong>: O sistema inclui uma verificação de validade da conta baseada na data de registro e no tempo de acesso permitido.</li>
</ul>

<h2>Prevenção de Manipulação de Data</h2>
<p>Para prevenir que usuários manipulem a data e hora do sistema operacional para estender indevidamente o período de acesso, o sistema utiliza a <a href="https://worldtimeapi.org/">WorldTimeAPI</a>. Essa API fornece a hora atual com base em fusos horários específicos, garantindo que as verificações de expiração de conta sejam feitas com um horário confiável.</p>

<h2>Como Usar</h2>
<ol>
    <li><strong>Configuração do Firebase</strong>: Certifique-se de ter uma conta no Firebase e configure o projeto para uso do Firebase Authentication e Realtime Database.</li>
    <li><strong>Arquivo de Credenciais</strong>: Utilize um arquivo de credenciais JSON para se conectar ao Firebase (esse arquivo é gerado no console do Firebase).</li>
    <li><strong>Registro de Usuários</strong>: O proprietário pode usar o código de admin para atualizar a quantidade de dias que o usuários tem acesso ao seu programa.</li>
    <li><strong>Acesso do Usuário</strong>: O usuário terá acesso ao painel de login. Se as credenciais estiverem corretas, o programa de login será fechado e o usuário será direcionado para o software principal.</li>
</ol>

<h2>Considerações de Segurança</h2>
<ul>
    <li><strong>Credenciais de Firebase</strong>: As credenciais administrativas do Firebase nunca devem ser expostas ao público ou incluídas no código do cliente final. Para garantir a segurança, utilizamos um arquivo .env para armazenar e configurar as variáveis de ambiente necessárias para a conexão com o Firebase. Certifique-se de que o arquivo .env não esteja incluído no controle de versão e que você configure as variáveis de ambiente adequadamente em seu ambiente local.</li>
    <li><strong>Compartilhamento de Conta</strong>: Para aumentar a segurança do seu aplicativo e impedir o compartilhamento de contas, é recomendável implementar um sistema de verificação que utilize o HWID (Hardware ID) ou UUID (Universally Unique Identifier) do computador do usuário que adquiriu seu software.</li>
</ul>


