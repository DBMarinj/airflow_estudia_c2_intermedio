# 🌬️ Ejercicios de Apache Airflow · Curso C2

Los DAG de Lucía y su biblioteca, para practicar Airflow sin instalar nada en tu computador.

## 🚀 Levantar Airflow en la nube (GitHub Codespaces)

1. Pulsa **Code → Codespaces → Create codespace on main**. La primera vez tarda 2 a 3 minutos.
2. En la terminal del Codespace:
   ```bash
   bash iniciar_airflow.sh
   ```
   Tarda de 3 a 5 minutos. Termina con «Airflow arrancando…».
3. Abre la pestaña **Puertos**, fila **8080**, y pulsa el ícono del globo. Si no responde, espera un minuto.
4. Usuario: `airflow` · Contraseña: `airflow`.
5. 🛑 **Al terminar, detén el Codespace** (*Codespaces → ⋯ → Stop codespace*). Si lo dejas encendido, gasta horas de tu cupo gratuito.

## 🧪 Primer DAG

En *Dags* busca `ej2_flujo_lucia`, activa el interruptor y pulsa ▶ (*Trigger*). Mira la vista *Graph*: las tareas pasan de gris a verde. Clic en una tarea → *Logs* para ver qué hizo.

## 📝 Ejercicios

Los enunciados están en [`ejercicios.md`](ejercicios.md). Los DAG están en `dags/` y los datos en `dags/datos/`.

## 🆘 Si algo falla

| Síntoma | Qué hacer |
|---|---|
| El puerto 8080 no abre | Espera un minuto y recarga; Airflow tarda en arrancar |
| Quieres saber qué contenedor cayó | `docker compose ps` |
| Quieres ver el motivo | `docker compose logs airflow-apiserver` |
| Cambiaste un DAG y no se ve | Espera menos de un minuto y recarga la página |

Airflow usa unos 3,7 GB de los 8 GB de la máquina: no abras más de un Codespace a la vez.
