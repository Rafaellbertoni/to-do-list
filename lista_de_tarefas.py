from typing import Optional
import sqlite3

conexao = sqlite3.connect('to-do-list.db')
cursor = conexao.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                concluidas INTEGER NOT NULL DEFAULT 0
               )  
               ''')


def adicionar_tarefa(descricao: str):
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('INSERT INTO tarefas (descricao) VALUES (?)', (descricao, ))
    
    conexao.commit()
    conexao.close()
    
def verificar_se_a_tarefa_existe(descricao: str) -> Optional[tuple]:
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM tarefas WHERE descricao = ?', (descricao, ))
    resultado = cursor.fetchone()
    
    conexao.close()
    return resultado
    
def listar_tarefas():
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM tarefas')
    resultado = cursor.fetchall()
    
    for tarefa in resultado:
        print(tarefa)
        
    conexao.close()
    
    
def marcar_conclusao(descricao: str,):
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('UPDATE tarefas SET concluidas = 1 WHERE descricao = ?', (descricao, ))
    
    conexao.commit()
    conexao.close()
    
    
def listar_tarefas_nao_concluidas():
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM tarefas WHERE concluidas = ?', (0, ))
    resultado = cursor.fetchall()
    
    for tarefa_nao_conluida in resultado:
        print(tarefa_nao_conluida)
        
    conexao.close()
    

def listar_tarefas_concluidas():
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM tarefas WHERE concluidas = ?', (1, ))
    resultado = cursor.fetchall()
    
    for tarefas_concluida in resultado:
        print(tarefas_concluida)
        
    conexao.close()
    
    
def deletar_tarefa(descricao: str):
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('DELETE FROM tarefas WHERE descricao = ?', (descricao, ))
    
    conexao.commit()
    conexao.close()
    
    
def alterar_tarefa(descricao: str, descricao_nova: str):
    conexao = sqlite3.connect('to-do-list.db')
    cursor = conexao.cursor()
    
    cursor.execute('UPDATE tarefas SET descricao = ? WHERE descricao = ?', (descricao_nova, descricao))
    
    conexao.commit()
    conexao.close()
    
        
    
def main():
    while True:
        print('[ADICIONAR TAREFA -- 1]')
        print('[LISTAR TAREFAS] -- 2')
        print('[MARCAR CONCLUSÃO -- 3]')
        print('[TAREFAS PENDENTES -- 4]')
        print('[TAREFAS CONCLUIDAS -- 5]')
        print('[DELETAR TAREFA] -- 6')
        print('[ALTERAR TAREFA -- 7]')
        print('[SAIR] -- 0')
        
        while True:
            try:
                opcoes = int(input('o que deseja fazer? '))
                break
            except ValueError:
                print('Erro: tipo de dado incorreto')
        
        
        if opcoes == 1:
            descricao = input('Descreva sua tarefa: ').strip().lower()
            if verificar_se_a_tarefa_existe(descricao) == None:
                adicionar_tarefa(descricao)
            else:
                print('Tarefa já existe')
        
        elif opcoes == 2:
            listar_tarefas()
            
        elif opcoes == 3:
            descricao = input('qual a tarefa concluída? ').strip().lower()
            marcar_conclusao(descricao)
            
        elif opcoes == 4:
            listar_tarefas_nao_concluidas()
            
        elif opcoes == 5:
            listar_tarefas_concluidas()
        
        elif opcoes == 6:
            descricao = input('Qual a descrição da tarefa? ').strip().lower()
            deletar_tarefa(descricao)
            
        elif opcoes == 7:
            descricao = input('Qual a descrição da tarefa? ').strip().lower()
            nova_descricao = input('Qual a nova descricao? ').strip().lower()
            alterar_tarefa(descricao, nova_descricao)
            
        elif opcoes == 0:
            break
            
            
main()
            
            
            
            
            