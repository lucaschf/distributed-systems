Como atividade, desenvolvam em Python ou Java uma classe OperacoesMatematicas, que possua os métodos soma, produto e fatorial. O usuário da classe deverá instanciá-la informando para o construtor o endereço IP do servidor de operações (onde os cálculos serão realmente executados) e a porta. Ao chamar um método, o nome do mesmo e os argumentos passados deverão ser enviados via socket para o servidor de operações, que os executará e devolverá via rede a resposta do cálculo.

Para o usuário da classe, a comunicação de rede deverá ser **transparente**, ou seja, ele não lidará com os sockets, e terá a percepção de que o método foi executado localmente. 

Exemplo de como deverá ser o uso da classe em Python (supondo que a classe OperacoesMatematicas está implementada no arquivo rpc.py):

`````python
from rpc import OperacoesMatematicas

RPC_SERVER = "192.168.0.1"
RPC_PORT = 5050

op = OperacoesMatematicas(RPC_SERVER, RPC_PORT)
soma = op.soma(2, 3)

print(soma) # Exibe 5
`````

