# odoo
A equipa de marketing está a precisar de contactos para fazer uma nova campanha de email marketing. Em virtude de arranjarmos novos contatos, vamos criar um addon que nos permita ir a uma base de dados buscar contatos através de API, e que crie um novo registo no nosso sistema.

A aplicação deve cumprir os seguintes pontos:

1.1 Deve criar uma Mailing List própria de nome “NOVOS CONTATOS 2023”

1.2 Devem criar contatos que fiquem associados a esta lista de contatos.

1.3 O form de contatos deve conter os seguintes dados (usar campos existentes e criar os necessários):

gender,name,street,city,state,country,postcode,email,phone,picture (deve mostrar a imagem)

1.4 os dados são retirados da seguinte API - https://randomuser.me/api

1.5 deve existir um botão wizard que define o número de contactos que quero importar (ex. carrego no botão, indico o número de contactos que quero, faço um pedido à API e crio esse número de contatos) (usar multiple request ver docs api)

1.6 Não pode haver contactos duplicados

1.7 Criar um botão para eliminar os contactos todos dessa lista



2 - Tanto as vendas já têm um campo para o vendedor, no entanto nenhum deles tem um campo para identificar o "angariador"(acquisition agent) ou seja a pessoa que referenciou a oportunidade.

É então pedido que seja criado um campo de contacto nas oportunidades, vendas e faturas.

O valor deste campo deve ser passado da oportunidade para a venda, e de venda para a fatura

(Ou seja se criar uma venda apartir da oportunidade, a venda deve assumir o mesmo angariador que a lead, e ao criar uma fatura a partir da venda, a fatura deve assumir o mesmo valor que a venda)

Este campo deve aparecer na vista de formulário a baixo do campo do vendedor

Nas vendas e faturas o campo só deve poder ser editado se o documento estiver no estado "draft" (verem exemplos da odoo, quando usam o parâmetro "states" nos campos)

Este campo deve também aparecer no print dos orçamentos perto do campo do vendedor

3- Criar um modulo que todos os dias vá Todos os dias pelas 22h verificar se algum utilizador se esqueceu de dar checkout. Se algum user se tiver esquecido de fazer checkout, e o checkin estiver no período de trabalho, deve ser registado automaticamente checkout para o final do horário de trabalho do funcionário naquele dia.

Notas: Para conseguir ver os horários de trabalho do funcionário podem ir ao resource.calendar definido no funcionário (calendar_id). devem também analisar com cuidado os métodos existentes no resource.resource para facilitar o desenvolvimento

NOTAS: Devem ativar as variantes de artigo para este exercício nas configurações gerais. (especialmente para o extra, e devem ter atenção que product.template é uma coisa, e product.product é outra)

Nos artigos ter uma listagem para os "clientes habituais" onde podemos colocar a referencia e nome que o cliente utiliza para aquele artigo.

1- Cada artigo pode ter Vários "clientes habituais" 2- Cada cliente pode estar em vários artigos 3- Cada cliente pode ter uma referencia e nome diferente por artigo, por exemplo: O artigo [ABC] Artigo, para o cliente Jorge pode ser [001] Produto e para o cliente Armando pode ser [QWERTY] sardinha 4- Nas vendas e faturas, ao adicionar um novo artigo, caso a venda/fatura seja para um cliente habitual desse artigo, deve usar esses valores, em vez de usar os "normais"

5- Tanto nas vendas como nas faturas, estes valor deve ser carregado ao editar/adicionar artigos ao documento, ou ao alterar o partner desse documento

EXTRA:

    Adicionar um novo campo aos artigos para poder colocar os países onde o artigo é vendido. Para já este campo deve ser apenas informativo, nao afetando o funcionamento normal do odoo.

    Este campo deve ser visível tanto nos templates como nas variantes

    Caso um template tenha várias variantes, este deve apresentar todos os países presentes nas suas variantes.

    Ao adicionar um novo país no template, este deve ser adicionado a todas as variantes também, e o mesmo deve acontecer quando se remove.

    Ao adicionar um novo país à variantes este deve ser apenas adicionado à variantes que está a ser editada, e não às restantes

    Dica: Campos computados podem ter o parametro "inverse"

https://www.youtube.com/watch?v=5x2v48yjY3Y

Enquadramento:

Cliente na área alimentar, com vários equipamentos que necessitam de manutenção preventiva, higienização e aprovisionamento de uma forma recorrente ou por pedido.

Descrição:

Após configuração dos planos de prevenção por equipamento, um automatismo diário vai criar os eventos de calendário necessários de forma a que todas as próximas manutenções preventivas estejam presentes no calendário e atribuídas aos técnicos/equipas presentes na configuração.

O operador vai ter um dispositivo móvel onde pode consultar as manutenções atribuídas a si, pode criar uma nova manutenção corretiva, dentro de uma manutenção consegue fazer registos de tempo, lançar consumos de materiais e preencher uma checklist.

Estas checklists podem ser configuradas ao nível da categoria de equipamento e também ao nível do equipamento em si, havendo uma lista de checklist para ser feita durante a manutenção e outra após a manutenção a ser preenchida pelo operador do equipamento caso necessário.

Cada equipamento pode ter uma lista de materiais base para a sua manutenção, esta listagem deve estar disponível no dashboard móvel para consulta, desta forma, o técnico que irá tratar da manutenção consegue recolher do stock o material necessário para proceder à reparação do equipamento, podendo lançar o seu consumo durante o processo de manutenção.

Deve existir dentro do equipamento um histórico das suas manutenções e reparações, dentro dessas manutenções devemos conseguir ver o resultado do preenchimento das checklists, os tempos e os consumos de materiais registados, dentro dos registos de reparações devemos conseguir ver quem reparou, que materiais foram retirados/consumidos nessa reparação, e tempo consumido na reparação.

Com o módulo de compras e inventário deve ser possível configurar várias localizações para armazenar os artigos, deve ser possível configurar regras de arrumação por localização, podendo desta forma receber sugestões de arrumação ao receber material proveniente das compras.

Deve também ser possível criar regras de reabastecimento genéricas para todo o armazém e específicas por localização, mantendo desta forma níveis mínimos de stock para artigos de uso frequente.

Com a utilização da feature de replenishment é possível também gerir previsões de stock, necessidades para determinadas atividades futuras. Desta forma conseguiremos ter uma previsão do material que será necessário no futuro, podendo gerar e antecipar compras diretamente pelo menu de replenishment.

O módulo de manutenção da Odoo não tem a funcionalidade de consumir stock.

Equipamentos do cliente têm uma lista de materiais que serão consumidos sempre que se faça uma manutenção, no formato artigo e quantidade a ser consumida, esta lista de materiais é carregada para a manutenção e a quantidade consumida é depois registada pelo operador, essas listas de materiais podem ser configuradas ao nivel da categoria do equipamento mas podem ser alteradas equipamento a equipamento.

Uma manutenção, deve ter a sua lista de materiais carregada assim que seja criada, o operador regista quantidades nessa lista de materiais e pode também adicionar ou remover materiais dessa lista.

Notas:

Ver tarefa 13 para retirar contexto e enquadramento do cliente

Modelos que devem ser utilizados para a criação de lista de materiais e consumos de stocks:

(stock.move/stock.move.line/maintenance.stock.move.template)

O módulo de manutenção da Odoo não tem a funcionalidade de preencher checklists de higienização antes de começar a manutenção.

Cliente quer um desenvolvimento que permita que os seus operadores de manutenção consigam preencher uma checklist de higienização antes de começar a manutenção, essas checklists podem ser configuradas ao nivel da categoria do equipamento mas podem ser alteradas equipamento a equipamento.

Vão ter que criar um modelo novo para os templates de checklists que devem depois estar associados a equipamentos ou templates de equipamentos no formato de uma lista, ou seja, um equipamento tem uma lista de templates de checklists, um template de checklist pode estar presente em vários equipamentos, uma categoria de equipamento tem uma lista de templates de checklists, um template de checklist pode estar presente em várias categorias de equipamentos.

Ao criar a manutenção, devemos criar depois as respectivas checklists e associar à manutenção, as checklists que criamos dependem do que está configurado ao nivel dos templates de checklists na categoria do equipamento ou no equipamento em si.

Bonus points: A checklist de higienização só deve ser editavel no estado "In Progress" Criar um fluxo identico para uma checklist diferente que terá que ser preenchida no estado "Repaired"(Esta checklist é para ser preenchida depois da reparação, será preenchida por outro operador que irá validar se a máquina está OK) Adicionar novo estado nas manutenções "Done", se as reparações não tiverem uma checklist para ser preenchida no estado "Repaired" então devem passar automaticamente para o estado "Done"
