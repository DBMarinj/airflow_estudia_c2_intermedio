# 🌬️ Ejercicios de Airflow: el flujo de Lucía

Seguimos con la bibliotecaria de la historia. En la escena 3 repite su análisis en abril, el archivo trae 40 filas repetidas y nadie se da cuenta. Hoy construyes el flujo que la habría avisado.

🔒 Todo es sintético: no hay personas reales.

## 🧰 Antes de empezar

Necesitas Airflow encendido, con una de estas dos opciones:

- 💻 **En tu computador**, con Docker, siguiendo la guía de instalación.
- ☁️ **En la nube**, con GitHub Codespaces. Mira el `README.md` del repositorio.

Con Airflow encendido, abre `http://localhost:8080` e inicia sesión con usuario `airflow` y contraseña `airflow`. Verás los DAG de ejemplo de Airflow y, entre ellos, los tuyos: `ej2_flujo_lucia`, `ej3_validacion`, `ej4_programacion` y `ej5_desafio`.

▶️ **Cómo ejecutar un DAG:** primero **actívalo** (los DAG nuevos empiezan pausados) y luego pulsa **Trigger** para ejecutarlo una vez.

✏️ **Cómo editar un DAG:** abre el archivo en la carpeta `dags/` con tu editor, haz el cambio y guárdalo. Airflow lo vuelve a leer solo, en menos de un minuto. Para ver el cambio, recarga la página.

📂 Los datos están en `dags/datos/`. Las salidas de tus tareas aparecen en `dags/salida/`.

## 👀 Ejercicio 1 · Mira un flujo en marcha

Ya lo hicimos en clase, pero con calma.

1. Busca el DAG `example_bash_operator` y actívalo.
2. Pulsa **Trigger** para ejecutarlo una vez.
3. Abre la vista del DAG: ¿qué tareas ves y en qué orden?
4. Abre una tarea y entra a su **registro**: ¿qué te cuenta?

🤔 **Para pensar:** ¿cuántas tareas terminaron bien? ¿Alguna se omitió? ¿Por qué crees que ocurrió?

## 🧹 Ejercicio 2 · El flujo de Lucía, en tres pasos

Abre `dags/ej2_flujo_lucia.py`. Ya trae tres tareas encadenadas: **traer**, **limpiar** y **contar**. Pero tiene dos huecos marcados con `TODO`.

1. Ejecuta el DAG tal como está. ¿Qué dice el registro de cada tarea?
2. 🔧 **TODO 1:** en `limpiar`, quita las filas repetidas, las que tienen el mismo `prestamo_id`.
3. 🔧 **TODO 2:** en `contar`, cuenta las filas donde `libro_id` es «Dune» (usa `ID_DUNE`) e imprime el resultado.
4. Ejecuta el DAG otra vez. ¿Cuántos préstamos de «Dune» hay en abril según tu registro?

🤔 **Para pensar:** si no limpiaras, ¿qué número te daría? Compara con lo que le pasó a Lucía.

## 🚨 Ejercicio 3 · Que avise cuando algo está raro

Abre `dags/ej3_validacion.py`. Tiene una tarea `validar_sin_repetidos` que por ahora no hace nada.

1. 🛠️ **Implementa la tarea:** si hay filas repetidas, detén el flujo con `raise ValueError("...")` y un mensaje claro.
2. Ejecuta el DAG. La tarea **debería ponerse roja**. Abre su registro y lee el mensaje.
3. Mira qué pasó con la tarea `limpiar`: ¿por qué no corrió?
4. ✅ **Ahora corrígelo:** la validación está antes de limpiar, y por eso falla. Cámbiala de lugar para que revise el archivo ya limpio.
5. Ejecuta de nuevo. Todo debería quedar en verde.

🤔 **Para pensar:** ¿es mejor que el flujo falle o que siga con datos repetidos? ¿Dónde conviene poner cada control?

## ⏰ Ejercicio 4 · Que corra solo

Abre `dags/ej4_programacion.py`. Su programación está en `None`: solo corre si lo ejecutas tú.

1. Cambia `schedule` para que corra **todos los lunes a las 7 de la mañana**. La forma es `"minuto hora día-del-mes mes día-de-la-semana"`.
2. Guarda y recarga la página. Busca el campo con la **próxima ejecución** del DAG.
3. Cámbialo ahora para que corra **el primer día de cada mes, a las 7**.
4. Pregúntate para qué sirven `start_date` y `catchup=False`.

🤔 **Para pensar:** Lucía quería «el primer lunes de cada mes». Prueba escribir `"0 7 1-7 * 1"`. ¿Hace lo que esperabas? Compara con el resto de ejecuciones que Airflow te anuncia.

## 🏆 Ejercicio 5 · Desafío: dale un tercer control

Abre `dags/ej5_desafio.py`. Ya trae dos controles que pasan: sin repetidos, y fechas legibles. La tarea `mi_control` está vacía.

1. Escribe un tercer control que pueda fallar, y que le sirva a Lucía.
2. Algunas ideas: que cada `libro_id` exista en `datos/libros.csv`, que la fecha de devolución no sea anterior a la de préstamo, o que el número de filas no baje de lo esperado.
3. Ejecuta el DAG. Si tu control es bueno, pasa cuando todo está bien y falla cuando no.
4. 🧪 **Pruébalo de verdad:** estropea a propósito una copia de los datos para comprobar que tu control falla. Un control que nunca falla no sirve.

🤔 **Para pensar:** ¿qué riesgo de la ficha de Lucía cubre tu control?
