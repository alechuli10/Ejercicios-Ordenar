#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Algoritmo orden_ascendente  
    # Ordenar 't[inicio .. fin]' en orden creciente.  
  
Entrada 
    t: TABLA[T -> COMPARABLE] # El objetivo de la ordenación 
    inicio, fin: ENTERO # Números de los componentes extremos a ordenar 
  
precondición  
    índice_válido(t, inicio)  
    índice_válido(t, fin) 
    inicio ≤ fin  
    está_definido(t, inicio, fin)  
  
poscondición  
    # La parte ordenada es igual a la antigua  
    es_igual_a(t, inicio, fin, antiguo(t), inicio, fin)  
  
    # Está ordenada en orden creciente  
    está_ordenada_en_orden_ascendente(t, inicio, fin)  
  
    # Las partes no ordenadas se quedan idénticas  
    índice_min(t) < inicio =>  
      son_idénticos  
        (t, índice_min(t), inicio - 1, antiguo(t), índice_min(t), inicio - 1) 
    fin < índice_max(t) =>  
      son_idénticos 
        (t, fin + 1, índice_max(t), antiguo(t), fin + 1, índice_max(t)) 
  
fin orden_ascendente
    
    
Algoritmo está_definido  
    # ¿'t[inicio .. fin]' se ha inicializado?  
  
Entrada 
    t: TABLA[T -> COMPARABLE] # La tabla a explorar 
    inicio, fin: ENTERO # Números componentes extremos a verificar 
  
Resultado: BOOLEANO  
  
precondición  
    # 'inicio' y 'fin' son índices válidos de 't'. 
    inicio ≤ fin => índice_válido(t, inicio) y índice_válido(t, fin) 
  
poscondición  
    # VERDADERO cuando los índices no están en orden 
    inicio > fin => Resultado = VERDADERO  
  
    # VERDADERO si y solo si los componentes de 't[inicio .. fin]'  
    # son no NULO, esto es, están inicializados:  
    # Resultado = VERDADERO o si no existe k natural (inicio ≤ k ≤ fin => t[k] 
= NULO)  
    inicio = fin => Resultado = (t[inicio] ≠ NULO) 
    inicio < fin => Resultado = 
        ( 
            (t[inicio] ≠ NULO)  
          y entonces  
            está_definido(t, inicio + 1, fin) 
        )  
  
fin está_definido 


Algoritmo es_igual_a  
    # ¿son iguales 't[inicio_t .. fin_t]' y 'u[inicio_u .. fin_u]'? 
  
Entrada 
    t, u: TABLA[T -> COMPARABLE] 
    inicio_t, fin_t, inicio_u, fin_u: ENTERO  
  
Resultado: BOOLEANO  
  
precondición  
    índice_válido(t, inicio_t)  
    índice_válido(t, fin_t)  
    está_definido(t, inicio_t, fin_t)  
    índice_válido(u, inicio_u)  
    índice_válido(u, fin_u)  
    está_definido(u, inicio_u, fin_u)  
  
poscondición  
    Resultado = 
        (  
            está_incluido_en(t, inicio_t, fin_t, u, inicio_u, fin_u) 
         y entonces  
            está_incluido_en(u, inicio_u, fin_u, t, inicio_t, fin_t) 
        )  
  
fin es_igual_a


Algoritmo pertenece  
    # ¿'e' pertenece a 't[inicio .. fin]'?  
  
Entrada 
    t: TABLA[T] 
    inicio, fin: ENTERO 
    e: T  
  
Resultado: BOOLEANO  
  
precondición  
    índice_válido(t, inicio)  
    índice_válido(t, fin)  
    está_definido(t, inicio, fin)  
  
poscondición 
    # Resultado = [existe k natural (inicio ≤ k ≤ fin => t[k] = e)]  
    Resultado = (posición(t, inicio, fin, e) ≠ AUSENTE)  
  
fin pertenece 


Algoritmo está_incluido_en  
    # ¿t[inicio_t .. fin_t] contenido o igual u[inicio_u .. fin_u]?  
  
Entrada  
    t, u: TABLA[T]  
    inicio_t, fin_t, inicio_u, fin_u: ENTERO  
  
Resultado: BOOLEANO  
  
precondición  
    inicio_t ≤ fin_t  
    índice_válido(t, inicio_t)  
    índice_válido(t, fin_t)  
    está_definido(t, inicio_t, fin_t)  
    inicio_u ≤ fin_u  
    índice_válido(u, inicio_u)  
    índice_válido(u, fin_u)  
    está_definido(t, inicio_u, fin_u)  
  
poscondición 
    inicio_t = fin_t => Resultado =  
                        pertenece(u, inicio_u, fin_u, t[inicio_t]) 
    inicio_t < fin_t => Resultado = 
    (  
        pertenece(u, inicio_u, fin_u, t[inicio_t])  
      y entonces  
        está_incluido_en 
            ( 
                t, inicio_t, fin_t,  
                intercambio_invariable 
                    ( 
                        u, inicio_u, fin_u,  
                        posición(u, inicio_u, fin_u, t[inicio_t]) 
                    ), 
                inicio_u+1, fin_u 
            ) 
    )  
fin está_incluido_en


Algoritmo son_idénticos, infijo '='  
    # ¿'t[inicio_t .. fin_t]' = 'u[inicio_u .. fin_u]'?  
  
Entrada 
    t, u: TABLA[T] 
    inicio_t, fin_t, inicio_u, fin_u: ENTERO  
  
Resultado: BOOLEANO  
  
precondición 
    inicio_t ≤ fin_t  
    índice_válido(t, inicio_t)  
    índice_válido(t, fin_t)  
    está_definido(t, inicio_t, fin_t)  
    inicio_u ≤ fin_u  
    índice_válido(u, inicio_u)  
    índice_válido(u, fin_u)  
    está_definido(t, inicio_u, fin_u)  
  
poscondición  
    # Mismo número de componentes 
    fin_t - inicio_t ≠ fin_u - inicio_u => Resultado = FALSO 
 
    inicio_t = fin_t => Resultado = 
        ( 
            inicio_u = fin_u  
          y entonces 
            t[inicio_t] = u[inicio_u] 
        ) 
    inicio_t < fin_t => Resultado = 
        ( 
            t[inicio_t] = u[inicio_u]  
          y entonces  
            son_idénticos  
                (t, inicio_t + 1, fin_t, u, inicio_u + 1, fin_u) 
        )  
  fin son_idénticos


# In[2]:


def ordenAscendente (t,inicio,fin):
    i= inicio+1
    while i<=fin:
        medio= (inicio+i)//2
        elemento= t[i]
        extremoInf= inicio
        extremoSup= i-1
        while medio<extremoSup:
            if elemento==t[medio]:
                t= t[inicio:medio]+[elemento]+t[medio:i]+t[i+1:fin+1]
                medio = extremoSup+1
            else:
                if elemento>t[medio]:
                    extremoInf= medio+1
                    medio= (extremoInf+extremoSup)//2
                else:
                    extremoSup= medio
                    medio= (extremoInf+extremoSup)//2
        if medio==extremoSup:
            if elemento<t[medio]:
                t= t[inicio:medio]+[elemento]+t[medio:i]+t[i+1:fin+1]
            else:
                t= t[inicio:medio+1]+[elemento]+t[medio+1:i]+t[i+1:fin+1]
        i= i+1
    return t

tabla= [5,3,9,4,2,4,5]
ordenAscendente(tabla,0,6)


# In[5]:


def ordenAscendente2 (t,inicio,fin):
    i= inicio+1
    aux= [t[inicio]]
    while i<=fin:
        medio= (inicio+i)//2
        elemento= t[i]
        extremoInf= inicio
        extremoSup= i-1
        while medio<extremoSup:
            if elemento==aux[medio]:
                aux= aux[inicio:medio]+[elemento]+aux[medio:i]
                medio = extremoSup+1
            else:
                if elemento>aux[medio]:
                    extremoInf= medio+1
                    medio= (extremoInf+extremoSup)//2
                else:
                    extremoSup= medio
                    medio= (extremoInf+extremoSup)//2
        if medio==extremoSup:
            if elemento<aux[medio]:
                aux= aux[inicio:medio]+[elemento]+aux[medio:i]
            else:
                aux= aux[inicio:medio+1]+[elemento]+aux[medio+1:i]
        i= i+1
    return aux

tabla= [5,3,9,4,2,4,5]
ordenAscendente2(tabla,0,6)


# In[4]:


#Ejercicio 2

def ordenacionTareas(lista):
    resultado = []
    tareas = []
   
    # Recuperamos todas las tareas presentes en la lista
    for prioridad in lista:
        if not prioridad[0] in tareas:
            tareas.append(prioridad[0])
        if not prioridad[1] in tareas:
            tareas.append(prioridad[1])  
   
    longitud=0  
    while len(tareas) > 0 and len(tareas)!=longitud: # El bucle se acaba cuando no quedan tareas o cuando no hemos podido eliminar ninguna (hay un ciclo en las prioridades)
        longitud = len(tareas)
        for tarea in tareas:
            sePuedeAgnadir = True
            for prioridad in lista:
                if prioridad[1] == tarea:# Hay una dependencia. No se puede agnadir esta tarea
                    sePuedeAgnadir = False
                   
            if sePuedeAgnadir:
                resultado.append(tarea)
                tareas.remove(tarea)
                # Eliminamos las prioridades en las que esta tarea aparece como necesaria, ya que las tareas
                # que dependen de ella ya se pueden asignar. Para ello, guardamos en una lista auxiliar las tareas
                # que no dependian de esta
                aux = []
                for prioridad in lista:
                    if prioridad[0] != tarea:
                        aux.append(prioridad)
                lista = aux;
               
    if len(tareas) > 0:
        resultado = []
       
    return resultado

lista = [[1,2], [1,3], [2,3], [4,1], [4,3], [4,5]]

ordenacionTareas(lista)
    


# In[ ]:


#Ejercicio 3
Algoritmo esta_explorado  
    # ¿'t[inicio .. fin]' se ha explorado?   
  
Entrada 
    t: TABLA[T -> COMPARABLE] # El objetivo de la exploración 
    inicio, fin: ENTERO # Números de los componentes extremos a explorar 
 
Resultado: BOOLEANO  
  
precondición  
    índice_válido(t, inicio)  
    índice_válido(t, fin) 
    inicio ≤ fin  
    está_definido(t, inicio, fin)
  
poscondición  
    Resultado= (
        t[inicio..fin]= [S1,..,Sk]
        (1 ≤ i ≤ k ) (Si = t[di .. fi]) 
        max 1 ≤ i ≤ k(Si) = t[fi]
        j= i+1
        Sj= t[dj .. fj]
        max 1 ≤ i ≤ k(Si) ≤ t[fj]) 
  
fin esta_explorado

