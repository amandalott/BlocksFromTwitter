# BlocksFromTwitter

Twitter-Python app using Tweepy for making a sum list of profiles who blocked yours

## Versions
- Python 3.7.3
- Tweepy  3.8.0

## Functions and Details 
* You will use Python and some libraries like Tweepy, Time and Json. You might have to install them.

* You will also need a Twitter Developer account for getting the keys and hashes.

* The app doesn't create the txt file it writes in (u gotta do it yourself, in the same directory of the file).
  * The file name is set as "sum_blocklist.txt" on the code, if u create a file with another name, you should change it on the code too.

* The list may contain double profiles for it doesnt check if they exist before appending.

* The code dumps the array result on the txt file everytime it finds a block, so if the code crashes u wont lose data.




# Tradução (PT-BR)
Aplicativo Twitter-Python que utiliza a biblioteca Tweepy para fazer uma lista de perfis que bloquearam o seu

## Funções e Detalhes
* Você vai precisar de usar Python e umas bibliotecas dele como Tweepy, Time e Json. Talvez você tenha que instalá-las.

* Você também vai precisar de uma conta de Desenvolvedor do Twitter pra pegar as chaves e hashes.

* O app não cria o arquivo txt que ele usa pra escrever (você vai ter de criar um, na mesma pasta que está o código)
  * O nome do arquivo é "sum_blocklist.txt" no código, se vc criar um arquivo com outro nome, tem de mudar no codigo também.
 
* A lista pode conter perfis duplicados porque não checa antes de adicionar no fim do array.

* O código escreve no arquivo toda vez que acha um block, assim se o código bugar no meio vc não perde os dados que já tinha.
