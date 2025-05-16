import csv

def obter_campos_personalizados():
    print('quais informações sobre os times você deseja cadastrar? (ex:franquia,título,cidade)')
    campos= input('separe os campos por vírgula:').split(',')
    campos= [campo.strip() for campo in campos]
    return campos

def cadastrar_times(campos):
    times = []
    
    while True:
         time = {}
         for campo in campos:
                valor = input(f'digite o valor para {campo}:')
                time[campo]= valor

         times.append(time)

         continuar=input('deseja cadastrar outro time?(s/n):').lower()
         if continuar !='s':
                break
    return times
    

def salvar_em_csv(times,campos,nome_arquivo='times.csv'):
        try:
            with open(nome_arquivo,mode='w',newline='', encording='utf-8') as arquivo:
                writer = csv.DictWriter(arquivo, fieldnames=campos)
                writer.writeheader()
                writer.writerows(times)
            print(f'/nDados salvos com sucesso em"{nome_arquivo}"')
        except Exception as e:
            print('erro ao salvar o arquivo')
def exibir_dados_csv(nome_arquivo='alunos.csv'):
                print('/n---Dados cadastrados---/n')
                try:
                    with open(nome_arquivo, mode='r',encoding='utf-8') as arquivo:
                        reader=csv.DictReader(arquivo)
                        for linha in reader:
                         print(linha)
                   
                except FileNotFoundError:
                    print('arquivo não encontrado.')
                except Exception as e:
                    print('erro ao ler arquivo', e)

def main():
      print('===sistema de cadastro de jogadores===')

      campos= obter_campos_personalizados()
      times=cadastrar_times(campos)
      salvar_em_csv(times,campos)
      exibir_dados_csv()
if __name__=='__main__':
           main()

            

        
                
    
